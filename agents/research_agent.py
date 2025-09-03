from crewai import Agent, Task
from langchain.tools import DuckDuckGoSearchRun
import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def __init__(self, llm):
        self.llm = llm
        self.search_tool = DuckDuckGoSearchRun()
    
    def create_agent(self):
        return Agent(
            role="Content Researcher",
            goal="Gather comprehensive, accurate, and up-to-date information on given topics",
            backstory="""You are an expert researcher with years of experience in fact-checking 
            and information gathering. You excel at finding reliable sources and extracting key insights.
            You always verify information from multiple sources and provide credible references.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool]
        )
    
    def create_research_task(self, agent, topic):
        return Task(
            description=f"""Research the topic: {topic}
            
            Your research should include:
            1. Key facts and statistics
            2. Current trends and developments
            3. Expert opinions and insights
            4. Relevant examples and case studies
            5. Target audience considerations
            
            Provide a comprehensive research report that will be used by other agents
            to create high-quality content.""",
            expected_output="""A detailed research report containing:
            - Executive summary of key findings
            - Important facts and statistics with sources
            - Current trends and market insights
            - Expert quotes and opinions
            - Relevant examples and case studies
            - Target audience analysis
            - Recommended content angles and approaches""",
            agent=agent
        )
    
    def search_web(self, query):
        """Enhanced web search functionality"""
        try:
            results = self.search_tool.run(query)
            return results
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def extract_webpage_content(self, url):
        """Extract content from a webpage"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text content
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Limit to first 5000 characters
        except Exception as e:
            return f"Error extracting content: {str(e)}"
