import os
import sys
from dotenv import load_dotenv
from typing import Dict, List, Any
import time

# Load environment variables
load_dotenv()

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from crewai import Crew, Process
    from langchain_openai import ChatOpenAI
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    print("CrewAI not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)

from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.editor_agent import EditorAgent
from agents.seo_agent import SEOAgent
from agents.platform_agent import PlatformAgent
from agents.qa_agent import QualityAssuranceAgent
from utils.helpers import ConfigManager, FileManager, MetricsCollector, ContentFormatter

class SmartContentPipeline:
    """Main orchestrator for the multi-agent content creation system"""
    
    def __init__(self, llm_provider="openai", model_name="gpt-3.5-turbo"):
        self.config_manager = ConfigManager()
        self.file_manager = FileManager()
        self.metrics = MetricsCollector()
        self.content_formatter = ContentFormatter()
        
        # Initialize LLM
        self.llm = self._initialize_llm(llm_provider, model_name)
        
        # Initialize agents
        self._initialize_agents()
    
    def _initialize_llm(self, provider, model_name):
        """Initialize the language model"""
        if provider.lower() == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file")
            return ChatOpenAI(
                model=model_name,
                temperature=0.7,
                api_key=api_key
            )
        elif provider.lower() == "google":
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in your .env file")
            return ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                temperature=0.7,
                google_api_key=api_key
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
    
    def _initialize_agents(self):
        """Initialize all agents"""
        self.research_agent = ResearchAgent(self.llm)
        self.writer_agent = WriterAgent(self.llm)
        self.editor_agent = EditorAgent(self.llm)
        self.seo_agent = SEOAgent(self.llm)
        self.platform_agent = PlatformAgent(self.llm)
        self.qa_agent = QualityAssuranceAgent(self.llm)
    
    def create_content(self, 
                      topic: str, 
                      content_type: str = "blog_post",
                      target_audience: str = "general audience",
                      tone: str = "professional",
                      platforms: List[str] = None,
                      target_keywords: List[str] = None) -> Dict[str, Any]:
        """
        Main content creation pipeline
        
        Args:
            topic: The topic for content creation
            content_type: Type of content (blog_post, article, etc.)
            target_audience: Target audience for the content
            tone: Tone of the content (professional, casual, etc.)
            platforms: List of platforms to optimize for
            target_keywords: Keywords for SEO optimization
        
        Returns:
            Dictionary containing all generated content and metadata
        """
        start_time = time.time()
        
        try:
            print(f"🚀 Starting content creation for topic: {topic}")
            
            # Step 1: Research
            print("📊 Step 1: Research Phase")
            research_results = self._conduct_research(topic)
            self.metrics.record_agent_usage("research")
            
            # Step 2: Content Writing
            print("✍️ Step 2: Writing Phase")
            initial_content = self._write_content(
                research_results, topic, content_type, target_audience, tone
            )
            self.metrics.record_agent_usage("writer")
            
            # Step 3: Content Editing
            print("📝 Step 3: Editing Phase")
            edited_content = self._edit_content(initial_content)
            self.metrics.record_agent_usage("editor")
            
            # Step 4: SEO Optimization
            print("🔍 Step 4: SEO Optimization Phase")
            if not target_keywords:
                target_keywords = self.seo_agent.generate_keywords(topic)
            
            seo_optimized_content, seo_data = self._optimize_seo(
                edited_content, target_keywords
            )
            self.metrics.record_agent_usage("seo")
            
            # Step 5: Platform Adaptation
            print("📱 Step 5: Platform Adaptation Phase")
            platform_versions = {}
            if platforms:
                platform_versions = self._adapt_for_platforms(
                    seo_optimized_content, platforms, topic
                )
                self.metrics.record_agent_usage("platform")
            
            # Step 6: Quality Assurance
            print("✅ Step 6: Quality Assurance Phase")
            qa_report = self._quality_assurance(
                seo_optimized_content, platform_versions, seo_data
            )
            self.metrics.record_agent_usage("qa")
            
            # Compile final results
            processing_time = time.time() - start_time
            self.metrics.record_processing_time(processing_time)
            self.metrics.record_content_creation()
            
            results = {
                'topic': topic,
                'content_type': content_type,
                'target_audience': target_audience,
                'tone': tone,
                'research_data': research_results,
                'initial_content': initial_content,
                'edited_content': edited_content,
                'final_content': seo_optimized_content,
                'seo_data': seo_data,
                'platform_versions': platform_versions,
                'qa_report': qa_report,
                'processing_time': processing_time,
                'metrics': self.metrics.get_metrics_summary()
            }
            
            # Save results
            self._save_results(results, topic)
            
            print(f"✨ Content creation completed in {processing_time:.2f} seconds!")
            return results
            
        except Exception as e:
            self.metrics.record_error(str(e))
            print(f"❌ Error in content creation: {str(e)}")
            raise
    
    def _conduct_research(self, topic: str) -> str:
        """Conduct research on the topic"""
        agent = self.research_agent.create_agent()
        task = self.research_agent.create_research_task(agent, topic)
        
        # Create a simple crew for research
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return str(result)
    
    def _write_content(self, research_data: str, topic: str, content_type: str, 
                      target_audience: str, tone: str) -> str:
        """Write initial content based on research"""
        agent = self.writer_agent.create_agent()
        task = self.writer_agent.create_writing_task(
            agent, research_data, content_type, target_audience, tone
        )
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return str(result)
    
    def _edit_content(self, content: str) -> str:
        """Edit and improve the content"""
        agent = self.editor_agent.create_agent()
        task = self.editor_agent.create_editing_task(agent, content)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return str(result)
    
    def _optimize_seo(self, content: str, keywords: List[str]) -> tuple:
        """Optimize content for SEO"""
        agent = self.seo_agent.create_agent()
        task = self.seo_agent.create_seo_task(agent, content, keywords)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        
        # Generate SEO metadata
        seo_data = {
            'keywords': keywords,
            'meta_title': self.seo_agent.create_meta_title(content[:100], keywords),
            'meta_description': self.seo_agent.create_meta_description(content[:100], content[:200]),
            'keyword_density': self.seo_agent.analyze_keyword_density(content, keywords),
            'headers': self.seo_agent.suggest_headers(content)
        }
        
        return str(result), seo_data
    
    def _adapt_for_platforms(self, content: str, platforms: List[str], topic: str) -> Dict[str, str]:
        """Adapt content for different platforms"""
        agent = self.platform_agent.create_agent()
        task = self.platform_agent.create_adaptation_task(agent, content, platforms)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        
        # Create platform-specific versions
        platform_versions = {}
        for platform in platforms:
            if platform.lower() == 'twitter':
                platform_versions[platform] = self.platform_agent.adapt_for_twitter(content, topic)
            elif platform.lower() == 'linkedin':
                platform_versions[platform] = self.platform_agent.adapt_for_linkedin(content, topic)
            else:
                platform_versions[platform] = content[:1000]  # Generic truncation
        
        return platform_versions
    
    def _quality_assurance(self, content: str, platform_versions: Dict[str, str], 
                          seo_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform quality assurance on the content"""
        agent = self.qa_agent.create_agent()
        
        requirements = f"""
        Content must be:
        - High quality and engaging
        - SEO optimized with keywords: {seo_data.get('keywords', [])}
        - Suitable for platforms: {list(platform_versions.keys())}
        - Error-free and professional
        """
        
        task = self.qa_agent.create_qa_task(agent, content, requirements)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        
        # Generate detailed QA report
        qa_report = self.qa_agent.generate_qa_report(content, platform_versions, seo_data)
        qa_report['agent_feedback'] = str(result)
        
        return qa_report
    
    def _save_results(self, results: Dict[str, Any], topic: str):
        """Save the results to files"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_topic = safe_topic.replace(' ', '_')
        
        # Save main content
        filename = f"{safe_topic}_{timestamp}.md"
        content = self.content_formatter.format_blog_post(
            results['topic'], 
            results['final_content']
        )
        self.file_manager.save_content(content, filename)
        
        # Save SEO report
        seo_filename = f"{safe_topic}_seo_{timestamp}.md"
        seo_report = self.content_formatter.format_seo_report(results['seo_data'])
        self.file_manager.save_content(seo_report, seo_filename)
        
        # Save complete results as JSON
        json_filename = f"{safe_topic}_complete_{timestamp}.json"
        # Remove non-serializable objects
        serializable_results = {k: v for k, v in results.items() 
                               if k not in ['metrics']}
        self.file_manager.save_json(serializable_results, json_filename)
        
        print(f"💾 Results saved: {filename}, {seo_filename}, {json_filename}")

def main():
    """Main function for testing the pipeline"""
    # Example usage
    pipeline = SmartContentPipeline(llm_provider="openai", model_name="gpt-3.5-turbo")
    
    # Test content creation
    results = pipeline.create_content(
        topic="Artificial Intelligence in Healthcare",
        content_type="blog_post",
        target_audience="healthcare professionals",
        tone="professional",
        platforms=["linkedin", "twitter"],
        target_keywords=["AI healthcare", "medical AI", "healthcare technology"]
    )
    
    print("\n📋 Content Creation Summary:")
    print(f"Topic: {results['topic']}")
    print(f"Processing Time: {results['processing_time']:.2f} seconds")
    print(f"QA Status: {results['qa_report']['approval_status']}")
    print(f"Platform Versions: {list(results['platform_versions'].keys())}")

if __name__ == "__main__":
    main()
