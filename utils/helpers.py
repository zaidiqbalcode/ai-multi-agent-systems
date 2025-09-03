import os
import yaml
from typing import Dict, Any, List
import json
from datetime import datetime

class ConfigManager:
    """Manage configuration settings for the multi-agent system"""
    
    def __init__(self, config_path: str = "config/agent_config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration if file not found"""
        return {
            'agents': {},
            'tasks': {},
            'llm_settings': {
                'temperature': 0.7,
                'max_tokens': 2000
            }
        }
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get configuration for a specific agent"""
        return self.config.get('agents', {}).get(agent_name, {})
    
    def get_task_config(self, task_name: str) -> Dict[str, Any]:
        """Get configuration for a specific task"""
        return self.config.get('tasks', {}).get(task_name, {})

class ContentFormatter:
    """Format content for different outputs and platforms"""
    
    @staticmethod
    def format_blog_post(title: str, content: str, meta_data: Dict[str, Any] = None) -> str:
        """Format content as a blog post"""
        formatted = f"# {title}\n\n"
        
        if meta_data:
            formatted += f"*Published: {meta_data.get('date', datetime.now().strftime('%Y-%m-%d'))}*\n"
            if meta_data.get('author'):
                formatted += f"*Author: {meta_data['author']}*\n"
            formatted += "\n"
        
        formatted += content
        return formatted
    
    @staticmethod
    def format_social_post(content: str, platform: str, hashtags: List[str] = None) -> str:
        """Format content for social media platforms"""
        if platform.lower() == 'twitter':
            # Ensure Twitter character limit
            if len(content) > 240:  # Leave room for hashtags
                content = content[:237] + "..."
        
        if hashtags:
            hashtag_str = " ".join([f"#{tag}" for tag in hashtags])
            content += f"\n\n{hashtag_str}"
        
        return content
    
    @staticmethod
    def format_seo_report(seo_data: Dict[str, Any]) -> str:
        """Format SEO analysis report"""
        report = "# SEO Analysis Report\n\n"
        
        if 'meta_title' in seo_data:
            report += f"**Meta Title:** {seo_data['meta_title']}\n"
        
        if 'meta_description' in seo_data:
            report += f"**Meta Description:** {seo_data['meta_description']}\n"
        
        if 'keywords' in seo_data:
            report += f"**Target Keywords:** {', '.join(seo_data['keywords'])}\n"
        
        if 'keyword_density' in seo_data:
            report += "\n## Keyword Density Analysis\n"
            for keyword, data in seo_data['keyword_density'].items():
                report += f"- {keyword}: {data['count']} occurrences ({data['density']}%)\n"
        
        return report

class FileManager:
    """Manage file operations for the content creation system"""
    
    @staticmethod
    def save_content(content: str, filename: str, directory: str = "output") -> str:
        """Save content to a file"""
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return filepath
    
    @staticmethod
    def save_json(data: Dict[str, Any], filename: str, directory: str = "output") -> str:
        """Save data as JSON file"""
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        return filepath
    
    @staticmethod
    def load_json(filepath: str) -> Dict[str, Any]:
        """Load data from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

class ValidationUtils:
    """Utility functions for content validation"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Validate URL format"""
        import re
        pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def check_profanity(text: str) -> bool:
        """Basic profanity check (simplified)"""
        # This is a basic implementation - in production, use a proper profanity filter
        profane_words = ['spam', 'scam', 'fake']  # Add more as needed
        text_lower = text.lower()
        return any(word in text_lower for word in profane_words)
    
    @staticmethod
    def validate_content_length(content: str, min_length: int = 100, max_length: int = 5000) -> bool:
        """Validate content length"""
        return min_length <= len(content) <= max_length

class MetricsCollector:
    """Collect and manage metrics for the content creation process"""
    
    def __init__(self):
        self.metrics = {
            'content_created': 0,
            'agents_used': set(),
            'processing_time': 0,
            'success_rate': 0,
            'errors': []
        }
    
    def record_agent_usage(self, agent_name: str):
        """Record usage of an agent"""
        self.metrics['agents_used'].add(agent_name)
    
    def record_content_creation(self):
        """Record successful content creation"""
        self.metrics['content_created'] += 1
    
    def record_error(self, error: str):
        """Record an error"""
        self.metrics['errors'].append({
            'error': error,
            'timestamp': datetime.now().isoformat()
        })
    
    def record_processing_time(self, time_seconds: float):
        """Record processing time"""
        self.metrics['processing_time'] = time_seconds
    
    def calculate_success_rate(self, total_attempts: int):
        """Calculate success rate"""
        if total_attempts > 0:
            self.metrics['success_rate'] = (self.metrics['content_created'] / total_attempts) * 100
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get summary of all metrics"""
        return {
            'content_created': self.metrics['content_created'],
            'agents_used': list(self.metrics['agents_used']),
            'processing_time': self.metrics['processing_time'],
            'success_rate': self.metrics['success_rate'],
            'error_count': len(self.metrics['errors']),
            'latest_errors': self.metrics['errors'][-5:] if self.metrics['errors'] else []
        }

class PromptTemplates:
    """Collection of prompt templates for different content types"""
    
    @staticmethod
    def research_prompt(topic: str, focus_areas: List[str] = None) -> str:
        """Generate research prompt template"""
        base_prompt = f"Research the topic: {topic}"
        
        if focus_areas:
            base_prompt += f"\n\nFocus on these specific areas: {', '.join(focus_areas)}"
        
        base_prompt += """
        
        Provide comprehensive information including:
        1. Key facts and statistics
        2. Current trends and developments
        3. Expert opinions and insights
        4. Relevant examples and case studies
        5. Target audience considerations
        
        Ensure all information is accurate and from reliable sources.
        """
        
        return base_prompt
    
    @staticmethod
    def writing_prompt(topic: str, content_type: str, audience: str, tone: str) -> str:
        """Generate writing prompt template"""
        return f"""
        Create {content_type} content about {topic} for {audience} with a {tone} tone.
        
        Requirements:
        - Engaging and well-structured content
        - Appropriate for the target audience
        - Consistent tone throughout
        - Clear introduction, body, and conclusion
        - Include relevant examples and insights
        
        Make it informative, engaging, and valuable to the reader.
        """
    
    @staticmethod
    def editing_prompt(content: str) -> str:
        """Generate editing prompt template"""
        return f"""
        Edit and improve the following content:
        
        {content}
        
        Focus on:
        - Grammar and spelling corrections
        - Improving clarity and readability
        - Enhancing flow and structure
        - Ensuring consistent tone
        - Making it more engaging
        
        Provide the edited version with explanations for major changes.
        """
