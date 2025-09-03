from crewai import Agent, Task

class PlatformAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role="Platform Specialist",
            goal="Adapt content for specific platforms and formats",
            backstory="""You are a social media and platform expert who understands the unique 
            requirements and best practices for different platforms like Twitter, LinkedIn, Instagram, 
            and blogs. You know how to optimize content for each platform's audience and format.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def create_adaptation_task(self, agent, content, platforms):
        return Task(
            description=f"""Adapt the following content for these platforms: {', '.join(platforms)}
            
            Original Content: {content}
            
            For each platform, create optimized versions considering:
            1. Character/word limits
            2. Platform-specific best practices
            3. Audience expectations
            4. Formatting requirements
            5. Hashtag strategies
            6. Call-to-action optimization
            7. Visual content suggestions""",
            expected_output=f"""Platform-optimized content versions for {', '.join(platforms)} including:
            - Content adapted for each platform's requirements
            - Appropriate length and formatting
            - Platform-specific hashtags and mentions
            - Optimized calls-to-action
            - Visual content suggestions
            - Best posting time recommendations
            - Engagement optimization tips""",
            agent=agent
        )
    
    def get_platform_specs(self):
        """Get specifications for different platforms"""
        return {
            'twitter': {
                'char_limit': 280,
                'best_practices': [
                    'Use relevant hashtags (2-3 max)',
                    'Include engaging visuals',
                    'Keep it concise and punchy',
                    'Use threads for longer content'
                ],
                'optimal_posting_times': 'Weekdays 9 AM - 3 PM',
                'hashtag_strategy': 'Use trending and niche hashtags'
            },
            'linkedin': {
                'char_limit': 3000,
                'best_practices': [
                    'Professional tone',
                    'Share insights and expertise',
                    'Use industry-specific hashtags',
                    'Encourage professional discussion'
                ],
                'optimal_posting_times': 'Weekdays 8 AM - 10 AM, 12 PM - 2 PM',
                'hashtag_strategy': 'Use 3-5 professional hashtags'
            },
            'instagram': {
                'char_limit': 2200,
                'best_practices': [
                    'Visual-first content',
                    'Tell stories',
                    'Use relevant hashtags (20-30)',
                    'Engage with community'
                ],
                'optimal_posting_times': 'Weekdays 11 AM - 1 PM, 7 PM - 9 PM',
                'hashtag_strategy': 'Mix popular and niche hashtags'
            },
            'facebook': {
                'char_limit': 63206,
                'best_practices': [
                    'Encourage engagement',
                    'Use native video when possible',
                    'Share valuable content',
                    'Use Facebook Groups'
                ],
                'optimal_posting_times': 'Weekdays 1 PM - 3 PM',
                'hashtag_strategy': 'Use 1-2 relevant hashtags'
            },
            'blog': {
                'word_count': '800-2000 words',
                'best_practices': [
                    'SEO optimization',
                    'Compelling headlines',
                    'Use subheadings',
                    'Include internal/external links'
                ],
                'optimal_posting_times': 'Tuesday - Thursday mornings',
                'seo_strategy': 'Focus on long-tail keywords'
            }
        }
    
    def adapt_for_twitter(self, content, topic):
        """Adapt content specifically for Twitter"""
        # Extract key points for tweet thread
        sentences = content.split('.')[:5]  # First 5 sentences
        tweets = []
        
        for i, sentence in enumerate(sentences, 1):
            if len(sentence.strip()) > 0:
                tweet = f"{i}/{len(sentences)} {sentence.strip()}."
                if len(tweet) <= 280:
                    tweets.append(tweet)
        
        return tweets
    
    def adapt_for_linkedin(self, content, topic):
        """Adapt content specifically for LinkedIn"""
        # Create professional post with insights
        return f"""🔍 Insights on {topic}

{content[:1000]}...

Key takeaways:
• [Point 1]
• [Point 2] 
• [Point 3]

What's your experience with {topic}? Share your thoughts below!

#Industry #Innovation #Growth"""
    
    def generate_hashtags(self, topic, platform):
        """Generate platform-appropriate hashtags"""
        platform_specs = self.get_platform_specs()
        
        if platform not in platform_specs:
            return []
        
        # Generate topic-based hashtags
        base_hashtags = [
            f"#{topic.replace(' ', '')}",
            f"#{topic.replace(' ', '')}Tips",
            "#Innovation",
            "#Technology"
        ]
        
        # Platform-specific additions
        if platform == 'linkedin':
            base_hashtags.extend(["#Professional", "#Industry", "#Growth"])
        elif platform == 'instagram':
            base_hashtags.extend(["#Inspiration", "#Lifestyle", "#Community"])
        
        return base_hashtags[:5]  # Limit to 5 hashtags
