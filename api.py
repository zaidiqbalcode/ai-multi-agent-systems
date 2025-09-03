from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import json
from datetime import datetime

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our demo pipeline
from demo import DemoContentPipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the demo pipeline
pipeline = DemoContentPipeline()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'Smart Content Pipeline API is running'
    })

@app.route('/api/create-content', methods=['POST'])
def create_content():
    """Create content using the multi-agent pipeline"""
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        if 'topic' not in data or not data['topic'].strip():
            return jsonify({'error': 'Topic is required'}), 400
        
        # Extract parameters with defaults
        topic = data['topic']
        content_type = data.get('contentType', 'blog_post')
        target_audience = data.get('targetAudience', 'professionals')
        tone = data.get('tone', 'professional')
        platforms = data.get('platforms', ['blog'])
        keywords = data.get('keywords', [])
        
        # Create content using the pipeline
        results = pipeline.create_content(
            topic=topic,
            content_type=content_type,
            target_audience=target_audience,
            tone=tone,
            platforms=platforms,
            keywords=keywords
        )
        
        # Format response for frontend
        response = {
            'success': True,
            'data': {
                'topic': results['topic'],
                'contentType': results['content_type'],
                'targetAudience': results['target_audience'],
                'tone': results['tone'],
                'platforms': results['platforms'],
                'processingTime': results['processing_time'],
                'finalContent': results['final_content'],
                'seoData': results.get('seo_data', {}),
                'platformVersions': results.get('platform_versions', {}),
                'qaReport': results.get('qa_report', {}),
                'createdAt': results['created_at']
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents', methods=['GET'])
def get_agents():
    """Get information about available agents"""
    agents = [
        {
            'type': 'research',
            'name': 'Research Agent',
            'description': 'Gathers comprehensive information and insights',
            'capabilities': ['Web search', 'Data collection', 'Fact verification', 'Trend analysis']
        },
        {
            'type': 'writer',
            'name': 'Content Writer Agent',
            'description': 'Creates engaging, well-structured content',
            'capabilities': ['Creative writing', 'Audience adaptation', 'Content structuring', 'Narrative development']
        },
        {
            'type': 'editor',
            'name': 'Editor Agent',
            'description': 'Improves clarity, grammar, and flow',
            'capabilities': ['Grammar correction', 'Style improvement', 'Flow optimization', 'Readability enhancement']
        },
        {
            'type': 'seo',
            'name': 'SEO Optimizer Agent',
            'description': 'Optimizes content for search engines',
            'capabilities': ['Keyword integration', 'Meta tag generation', 'Content structure optimization', 'SEO best practices']
        },
        {
            'type': 'platform',
            'name': 'Platform Adapter Agent',
            'description': 'Adapts content for different platforms',
            'capabilities': ['Platform-specific formatting', 'Character limit compliance', 'Hashtag optimization', 'Engagement strategies']
        },
        {
            'type': 'qa',
            'name': 'Quality Assurance Agent',
            'description': 'Ensures content meets quality standards',
            'capabilities': ['Quality scoring', 'Compliance checking', 'Final approval', 'Improvement recommendations']
        }
    ]
    
    return jsonify({
        'success': True,
        'data': agents
    })

@app.route('/api/content-types', methods=['GET'])
def get_content_types():
    """Get available content types"""
    content_types = [
        {
            'value': 'blog_post',
            'label': 'Blog Post',
            'description': 'Long-form content for websites'
        },
        {
            'value': 'article',
            'label': 'Article',
            'description': 'News or magazine-style content'
        },
        {
            'value': 'social_media',
            'label': 'Social Media',
            'description': 'Short-form social content'
        },
        {
            'value': 'newsletter',
            'label': 'Newsletter',
            'description': 'Email newsletter content'
        },
        {
            'value': 'whitepaper',
            'label': 'Whitepaper',
            'description': 'Technical documentation'
        }
    ]
    
    return jsonify({
        'success': True,
        'data': content_types
    })

@app.route('/api/platforms', methods=['GET'])
def get_platforms():
    """Get available platforms"""
    platforms = [
        {
            'value': 'blog',
            'label': 'Blog/Website',
            'icon': '📝',
            'description': 'Long-form content with SEO optimization'
        },
        {
            'value': 'twitter',
            'label': 'Twitter',
            'icon': '🐦',
            'description': 'Short-form tweets and threads'
        },
        {
            'value': 'linkedin',
            'label': 'LinkedIn',
            'icon': '💼',
            'description': 'Professional networking content'
        },
        {
            'value': 'facebook',
            'label': 'Facebook',
            'icon': '📘',
            'description': 'Engaging social media posts'
        },
        {
            'value': 'instagram',
            'label': 'Instagram',
            'icon': '📸',
            'description': 'Visual-first storytelling'
        }
    ]
    
    return jsonify({
        'success': True,
        'data': platforms
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("🚀 Starting Smart Content Pipeline API...")
    print("📍 API Endpoints:")
    print("   GET  /api/health          - Health check")
    print("   POST /api/create-content  - Create content")
    print("   GET  /api/agents          - Get agent information")
    print("   GET  /api/content-types   - Get content types")
    print("   GET  /api/platforms       - Get platform information")
    print("\n🌐 Server running at: http://localhost:8000")
    
    app.run(debug=True, host='0.0.0.0', port=8000)
