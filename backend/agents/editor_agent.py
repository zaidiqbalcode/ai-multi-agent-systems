from crewai import Agent, Task

class EditorAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role="Content Editor",
            goal="Review, improve, and polish content for clarity, grammar, and engagement",
            backstory="""You are an experienced editor with a keen eye for detail. You excel at 
            improving content flow, fixing grammar issues, and enhancing readability. You understand 
            how to make content more engaging while maintaining its original intent and message.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def create_editing_task(self, agent, content):
        return Task(
            description=f"""Edit and improve the following content:
            
            {content}
            
            Your editing should focus on:
            1. Grammar and spelling corrections
            2. Improving sentence structure and flow
            3. Enhancing readability and clarity
            4. Ensuring consistent tone and style
            5. Improving transitions between paragraphs
            6. Making the content more engaging
            7. Fact-checking for accuracy
            8. Ensuring proper formatting""",
            expected_output="""Polished, error-free content with:
            - Corrected grammar and spelling
            - Improved sentence structure and flow
            - Enhanced readability and clarity
            - Consistent tone and style throughout
            - Better transitions and coherence
            - More engaging language where appropriate
            - Proper formatting and structure
            - Editor's notes on major changes made""",
            agent=agent
        )
    
    def grammar_check(self, text):
        """Basic grammar and style check"""
        issues = []
        
        # Check for common issues
        if text.count('!') > 3:
            issues.append("Consider reducing exclamation marks for professional tone")
        
        sentences = text.split('.')
        long_sentences = [s for s in sentences if len(s.split()) > 25]
        if long_sentences:
            issues.append(f"Found {len(long_sentences)} potentially long sentences")
        
        # Check for passive voice indicators
        passive_indicators = ['was', 'were', 'been', 'being']
        passive_count = sum(text.lower().count(word) for word in passive_indicators)
        if passive_count > len(sentences) * 0.3:
            issues.append("Consider reducing passive voice usage")
        
        return issues
    
    def readability_score(self, text):
        """Simple readability assessment"""
        sentences = text.split('.')
        words = text.split()
        
        if len(sentences) == 0 or len(words) == 0:
            return "Unable to calculate"
        
        avg_sentence_length = len(words) / len(sentences)
        
        if avg_sentence_length < 15:
            return "Good readability"
        elif avg_sentence_length < 20:
            return "Moderate readability"
        else:
            return "Consider shorter sentences for better readability"
