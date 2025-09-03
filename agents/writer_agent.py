from crewai import Agent, Task

class WriterAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role="Content Writer",
            goal="Create engaging, well-structured, and informative content based on research",
            backstory="""You are a skilled content writer with expertise in various writing styles 
            and formats. You can adapt your writing to different audiences and platforms. You excel 
            at creating compelling narratives, clear explanations, and engaging content that 
            resonates with the target audience.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def create_writing_task(self, agent, research_data, content_type, target_audience, tone):
        return Task(
            description=f"""Create {content_type} content based on the research data provided.
            
            Research Data: {research_data}
            Content Type: {content_type}
            Target Audience: {target_audience}
            Tone: {tone}
            
            Your content should:
            1. Be engaging and well-structured
            2. Include relevant information from the research
            3. Match the specified tone and style
            4. Be appropriate for the target audience
            5. Have a clear introduction, body, and conclusion
            6. Include compelling headlines and subheadings
            7. Be between 800-1200 words for blog posts, 
               or appropriate length for other content types""",
            expected_output=f"""High-quality {content_type} content that includes:
            - Compelling headline/title
            - Engaging introduction that hooks the reader
            - Well-structured body with clear sections and subheadings
            - Relevant information from research incorporated naturally
            - Strong conclusion with call-to-action
            - Appropriate tone and style for {target_audience}
            - Proper formatting and structure""",
            agent=agent
        )
    
    def create_blog_post(self, research_data, topic, target_audience="general audience", tone="professional"):
        """Create a blog post based on research data"""
        prompt = f"""
        Write a comprehensive blog post about {topic} for {target_audience} with a {tone} tone.
        
        Use this research data: {research_data}
        
        Structure:
        1. Compelling headline
        2. Engaging introduction
        3. 3-5 main sections with subheadings
        4. Conclusion with key takeaways
        5. Call to action
        
        Make it informative, engaging, and well-researched.
        """
        return prompt
    
    def create_social_media_post(self, research_data, platform, topic):
        """Create platform-specific social media content"""
        platform_specs = {
            "twitter": {"limit": 280, "style": "concise, hashtags"},
            "linkedin": {"limit": 1300, "style": "professional, thought leadership"},
            "facebook": {"limit": 500, "style": "engaging, conversational"},
            "instagram": {"limit": 2200, "style": "visual, storytelling"}
        }
        
        spec = platform_specs.get(platform.lower(), platform_specs["twitter"])
        
        prompt = f"""
        Create a {platform} post about {topic} using this research: {research_data}
        
        Requirements:
        - Maximum {spec['limit']} characters
        - Style: {spec['style']}
        - Include relevant hashtags
        - Engaging and shareable
        """
        return prompt
