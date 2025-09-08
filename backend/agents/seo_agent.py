from crewai import Agent, Task

class SEOAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role="SEO Specialist",
            goal="Optimize content for search engines while maintaining readability and engagement",
            backstory="""You are an SEO expert who understands how to optimize content for search 
            engines without compromising quality. You know the latest SEO best practices, keyword 
            research, and how to structure content for both users and search engines.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def create_seo_task(self, agent, content, target_keywords):
        return Task(
            description=f"""Optimize the following content for SEO:
            
            Content: {content}
            Target Keywords: {target_keywords}
            
            Your SEO optimization should include:
            1. Keyword integration (natural placement)
            2. Meta title and description
            3. Header structure (H1, H2, H3)
            4. Internal linking suggestions
            5. Image alt text suggestions
            6. URL slug recommendation
            7. Featured snippet optimization
            8. Content length optimization""",
            expected_output="""SEO-optimized content package including:
            - Optimized content with natural keyword integration
            - Meta title (50-60 characters)
            - Meta description (150-160 characters)
            - Suggested header structure
            - Internal linking opportunities
            - Image alt text suggestions
            - Recommended URL slug
            - Featured snippet optimization notes
            - SEO checklist with recommendations""",
            agent=agent
        )
    
    def generate_keywords(self, topic):
        """Generate relevant keywords for a topic"""
        # This would typically use a keyword research tool
        # For demo purposes, we'll create basic keyword suggestions
        base_keywords = [
            topic,
            f"{topic} guide",
            f"how to {topic}",
            f"{topic} tips",
            f"best {topic}",
            f"{topic} 2024"
        ]
        return base_keywords
    
    def create_meta_title(self, topic, keywords):
        """Create SEO-optimized meta title"""
        primary_keyword = keywords[0] if keywords else topic
        return f"{primary_keyword.title()}: Complete Guide & Best Practices"
    
    def create_meta_description(self, topic, content_preview):
        """Create SEO-optimized meta description"""
        preview = content_preview[:120] if len(content_preview) > 120 else content_preview
        return f"{preview}... Learn more about {topic} with expert insights and practical tips."
    
    def analyze_keyword_density(self, content, keywords):
        """Analyze keyword density in content"""
        content_lower = content.lower()
        word_count = len(content.split())
        
        keyword_analysis = {}
        for keyword in keywords:
            count = content_lower.count(keyword.lower())
            density = (count / word_count) * 100 if word_count > 0 else 0
            keyword_analysis[keyword] = {
                'count': count,
                'density': round(density, 2)
            }
        
        return keyword_analysis
    
    def suggest_headers(self, content):
        """Suggest header structure for better SEO"""
        # Simple header suggestion based on content length
        paragraphs = content.split('\n\n')
        suggestions = []
        
        if len(paragraphs) > 1:
            suggestions.append("H1: Main title")
            
        if len(paragraphs) > 3:
            suggestions.append("H2: Introduction")
            
        if len(paragraphs) > 5:
            suggestions.extend([
                "H2: Main Topic 1",
                "H3: Subtopic 1.1",
                "H3: Subtopic 1.2"
            ])
            
        return suggestions
