from crewai import Agent, Task

class QualityAssuranceAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role="Quality Assurance Specialist",
            goal="Ensure final content meets all quality standards and requirements",
            backstory="""You are a quality assurance expert who ensures all content meets the 
            highest standards before publication. You have a comprehensive checklist for content 
            quality, including accuracy, readability, SEO optimization, and platform compliance.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def create_qa_task(self, agent, content, requirements):
        return Task(
            description=f"""Perform comprehensive quality assurance on the content:
            
            Content: {content}
            Requirements: {requirements}
            
            Check for:
            1. Content accuracy and factual correctness
            2. Grammar and spelling errors
            3. Tone and style consistency
            4. SEO optimization compliance
            5. Platform-specific requirements
            6. Brand voice alignment
            7. Call-to-action effectiveness
            8. Overall readability and engagement
            9. Legal and compliance issues
            10. Final formatting and presentation""",
            expected_output="""Quality assurance report including:
            - Overall quality score (1-10)
            - Detailed checklist with pass/fail status
            - List of identified issues and recommendations
            - Content approval status
            - Suggested improvements for future content
            - Final approved content (if passed)
            - Publication readiness assessment""",
            agent=agent
        )
    
    def quality_checklist(self):
        """Comprehensive quality checklist"""
        return {
            'content_quality': [
                'Factual accuracy verified',
                'No spelling or grammar errors',
                'Consistent tone and style',
                'Clear and logical structure',
                'Engaging and valuable content'
            ],
            'seo_compliance': [
                'Target keywords properly integrated',
                'Meta title and description optimized',
                'Proper header structure',
                'Internal linking implemented',
                'Image alt texts provided'
            ],
            'platform_optimization': [
                'Platform-specific formatting applied',
                'Character/word limits respected',
                'Appropriate hashtags included',
                'Visual content suggestions provided',
                'Call-to-action optimized'
            ],
            'brand_compliance': [
                'Brand voice maintained',
                'Style guide followed',
                'Legal requirements met',
                'Disclaimer included if needed',
                'Copyright compliance verified'
            ],
            'technical_aspects': [
                'Proper formatting applied',
                'Links are functional',
                'Mobile-friendly presentation',
                'Loading speed optimized',
                'Accessibility standards met'
            ]
        }
    
    def assess_content_quality(self, content):
        """Assess overall content quality"""
        issues = []
        score = 10
        
        # Check content length
        word_count = len(content.split())
        if word_count < 100:
            issues.append("Content may be too short for meaningful value")
            score -= 1
        elif word_count > 3000:
            issues.append("Content may be too long for optimal engagement")
            score -= 0.5
        
        # Check for common quality issues
        if content.count('!') > word_count * 0.02:
            issues.append("Excessive exclamation marks detected")
            score -= 0.5
        
        # Check for repetitive words
        words = content.lower().split()
        word_freq = {}
        for word in words:
            if len(word) > 4:  # Only check longer words
                word_freq[word] = word_freq.get(word, 0) + 1
        
        repetitive_words = [word for word, freq in word_freq.items() if freq > len(words) * 0.03]
        if repetitive_words:
            issues.append(f"Repetitive words detected: {', '.join(repetitive_words[:3])}")
            score -= 0.5
        
        # Check sentence variety
        sentences = content.split('.')
        avg_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        if avg_length > 25:
            issues.append("Average sentence length is too long")
            score -= 0.5
        
        return max(1, score), issues
    
    def generate_qa_report(self, content, platform_versions, seo_data):
        """Generate comprehensive QA report"""
        content_score, content_issues = self.assess_content_quality(content)
        
        report = {
            'overall_score': content_score,
            'content_issues': content_issues,
            'platform_compliance': self._check_platform_compliance(platform_versions),
            'seo_compliance': self._check_seo_compliance(seo_data),
            'recommendations': self._generate_recommendations(content_issues),
            'approval_status': 'APPROVED' if content_score >= 7 and len(content_issues) <= 2 else 'NEEDS_REVISION'
        }
        
        return report
    
    def _check_platform_compliance(self, platform_versions):
        """Check if platform versions meet requirements"""
        compliance = {}
        platform_specs = {
            'twitter': 280,
            'linkedin': 3000,
            'instagram': 2200,
            'facebook': 500
        }
        
        for platform, content in platform_versions.items():
            if platform in platform_specs:
                char_count = len(content)
                compliance[platform] = char_count <= platform_specs[platform]
        
        return compliance
    
    def _check_seo_compliance(self, seo_data):
        """Check SEO compliance"""
        compliance = {
            'meta_title_length': 50 <= len(seo_data.get('meta_title', '')) <= 60,
            'meta_description_length': 150 <= len(seo_data.get('meta_description', '')) <= 160,
            'keywords_integrated': len(seo_data.get('keywords', [])) > 0,
            'headers_structured': len(seo_data.get('headers', [])) > 0
        }
        return compliance
    
    def _generate_recommendations(self, issues):
        """Generate recommendations based on identified issues"""
        recommendations = []
        
        for issue in issues:
            if "too short" in issue:
                recommendations.append("Add more detailed explanations and examples")
            elif "too long" in issue:
                recommendations.append("Consider breaking into multiple posts or sections")
            elif "exclamation marks" in issue:
                recommendations.append("Reduce exclamation marks for more professional tone")
            elif "repetitive" in issue:
                recommendations.append("Use synonyms to vary vocabulary")
            elif "sentence length" in issue:
                recommendations.append("Break long sentences into shorter, clearer ones")
        
        return recommendations
