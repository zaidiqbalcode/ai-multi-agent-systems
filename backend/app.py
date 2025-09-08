import streamlit as st
import os
import sys
from datetime import datetime
import json

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import SmartContentPipeline
    from utils.helpers import ContentFormatter, FileManager
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.error("Please ensure all dependencies are installed: pip install -r requirements.txt")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Smart Content Creation Pipeline",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.25rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 0.25rem;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 Smart Content Creation Pipeline</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2em; color: #666;">AI Multi-Agent System for Automated Content Creation</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # LLM Selection
        llm_provider = st.selectbox(
            "Choose LLM Provider",
            ["OpenAI", "Google"],
            help="Select your preferred AI model provider"
        )
        
        if llm_provider == "OpenAI":
            model_name = st.selectbox(
                "OpenAI Model",
                ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
                help="Choose the OpenAI model for content generation"
            )
        else:
            model_name = "gemini-1.5-flash"
            st.info("Using Google Gemini 1.5 Flash")
        
        # API Key Setup
        st.header("🔑 API Configuration")
        
        if llm_provider == "OpenAI":
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                help="Enter your OpenAI API key"
            )
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
        else:
            api_key = st.text_input(
                "Google API Key",
                type="password",
                help="Enter your Google AI API key"
            )
            if api_key:
                os.environ["GOOGLE_API_KEY"] = api_key
        
        # Agent Information
        st.header("🤖 Active Agents")
        agents = [
            "📊 Research Agent",
            "✍️ Content Writer Agent", 
            "📝 Editor Agent",
            "🔍 SEO Optimizer Agent",
            "📱 Platform Adapter Agent",
            "✅ Quality Assurance Agent"
        ]
        
        for agent in agents:
            st.markdown(f'<div class="agent-card">{agent}</div>', unsafe_allow_html=True)
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["📝 Create Content", "📊 Agent Workflow", "📈 Results"])
    
    with tab1:
        create_content_interface()
    
    with tab2:
        show_agent_workflow()
    
    with tab3:
        show_results_interface()

def create_content_interface():
    """Interface for creating new content"""
    
    st.header("📝 Content Creation")
    
    # Content creation form
    with st.form("content_creation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input(
                "Content Topic *",
                placeholder="e.g., Artificial Intelligence in Healthcare",
                help="Enter the main topic for your content"
            )
            
            content_type = st.selectbox(
                "Content Type",
                ["blog_post", "article", "whitepaper", "social_media_post", "newsletter"],
                help="Select the type of content to create"
            )
            
            target_audience = st.selectbox(
                "Target Audience",
                ["general audience", "professionals", "students", "entrepreneurs", "technical experts"],
                help="Choose your target audience"
            )
        
        with col2:
            tone = st.selectbox(
                "Content Tone",
                ["professional", "casual", "formal", "conversational", "authoritative"],
                help="Select the tone for your content"
            )
            
            platforms = st.multiselect(
                "Target Platforms",
                ["twitter", "linkedin", "facebook", "instagram", "blog"],
                default=["blog"],
                help="Select platforms to optimize content for"
            )
            
            keywords = st.text_area(
                "Target Keywords (optional)",
                placeholder="Enter keywords separated by commas",
                help="Enter SEO keywords for optimization"
            )
        
        # Advanced options
        with st.expander("🔧 Advanced Options"):
            include_research = st.checkbox("Include detailed research", value=True)
            include_seo = st.checkbox("Include SEO optimization", value=True)
            include_qa = st.checkbox("Include quality assurance", value=True)
            
            content_length = st.slider(
                "Preferred Content Length (words)",
                min_value=300,
                max_value=3000,
                value=1000,
                step=100
            )
        
        submitted = st.form_submit_button("🚀 Generate Content", use_container_width=True)
        
        if submitted:
            if not topic:
                st.error("Please enter a content topic.")
                return
            
            # Check for API key
            provider_key = "OPENAI_API_KEY" if st.session_state.get('llm_provider', 'OpenAI') == "OpenAI" else "GOOGLE_API_KEY"
            if not os.getenv(provider_key):
                st.error(f"Please provide your API key in the sidebar.")
                return
            
            # Process keywords
            keyword_list = []
            if keywords:
                keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
            
            # Show progress
            progress_container = st.container()
            
            with progress_container:
                st.info("🚀 Initializing content creation pipeline...")
                
                try:
                    # Initialize pipeline
                    pipeline = SmartContentPipeline(
                        llm_provider=st.session_state.get('llm_provider', 'OpenAI').lower(),
                        model_name=st.session_state.get('model_name', 'gpt-3.5-turbo')
                    )
                    
                    # Create content
                    with st.spinner("Creating content... This may take a few minutes."):
                        results = pipeline.create_content(
                            topic=topic,
                            content_type=content_type,
                            target_audience=target_audience,
                            tone=tone,
                            platforms=platforms,
                            target_keywords=keyword_list
                        )
                    
                    # Store results in session state
                    st.session_state['last_results'] = results
                    
                    # Display success message
                    st.markdown('<div class="success-box">✅ Content creation completed successfully!</div>', unsafe_allow_html=True)
                    
                    # Show brief summary
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Processing Time", f"{results['processing_time']:.1f}s")
                    with col2:
                        st.metric("QA Status", results['qa_report']['approval_status'])
                    with col3:
                        st.metric("Platforms", len(results.get('platform_versions', {})))
                    
                    # Quick preview
                    st.subheader("📄 Content Preview")
                    preview_text = results['final_content'][:500] + "..." if len(results['final_content']) > 500 else results['final_content']
                    st.text_area("Generated Content (Preview)", preview_text, height=150, disabled=True)
                    
                    st.info("💡 View the complete results in the 'Results' tab!")
                    
                except Exception as e:
                    st.error(f"❌ Error creating content: {str(e)}")
                    st.error("Please check your API key and try again.")

def show_agent_workflow():
    """Show the agent workflow and process"""
    
    st.header("🤖 Multi-Agent Workflow")
    
    st.markdown("""
    <div class="info-box">
    <h4>🔄 Content Creation Process</h4>
    <p>Our AI multi-agent system follows a structured workflow to ensure high-quality content creation:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Workflow visualization
    workflow_steps = [
        {
            "agent": "📊 Research Agent",
            "task": "Information Gathering",
            "description": "Conducts comprehensive research on the given topic, gathering facts, statistics, trends, and expert insights.",
            "output": "Research report with key findings and insights"
        },
        {
            "agent": "✍️ Content Writer Agent",
            "task": "Content Creation",
            "description": "Creates engaging, well-structured content based on research findings and user requirements.",
            "output": "Initial content draft with proper structure"
        },
        {
            "agent": "📝 Editor Agent",
            "task": "Content Editing",
            "description": "Reviews and improves content for clarity, grammar, flow, and overall readability.",
            "output": "Polished, error-free content"
        },
        {
            "agent": "🔍 SEO Optimizer Agent",
            "task": "SEO Optimization",
            "description": "Optimizes content for search engines while maintaining quality and readability.",
            "output": "SEO-optimized content with metadata"
        },
        {
            "agent": "📱 Platform Adapter Agent",
            "task": "Platform Adaptation",
            "description": "Adapts content for different platforms (social media, blogs) with platform-specific formatting.",
            "output": "Platform-specific content versions"
        },
        {
            "agent": "✅ Quality Assurance Agent",
            "task": "Quality Check",
            "description": "Performs final quality assurance, ensuring all standards and requirements are met.",
            "output": "Quality report and final approval"
        }
    ]
    
    for i, step in enumerate(workflow_steps, 1):
        with st.expander(f"Step {i}: {step['agent']} - {step['task']}"):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"**Agent:** {step['agent']}")
                st.markdown(f"**Task:** {step['task']}")
            
            with col2:
                st.markdown(f"**Description:** {step['description']}")
                st.markdown(f"**Output:** {step['output']}")
        
        if i < len(workflow_steps):
            st.markdown("⬇️", unsafe_allow_html=True)
    
    # Agent collaboration benefits
    st.subheader("🌟 Benefits of Multi-Agent Collaboration")
    
    benefits = [
        "**Specialization**: Each agent focuses on their area of expertise",
        "**Quality Assurance**: Multiple layers of review and improvement",
        "**Scalability**: Can handle multiple content requests simultaneously",
        "**Consistency**: Maintains quality standards across all content",
        "**Efficiency**: Parallel processing reduces overall creation time"
    ]
    
    for benefit in benefits:
        st.markdown(f"• {benefit}")

def show_results_interface():
    """Show results from the last content creation"""
    
    st.header("📈 Content Creation Results")
    
    if 'last_results' not in st.session_state:
        st.info("No content has been created yet. Go to the 'Create Content' tab to generate your first content!")
        return
    
    results = st.session_state['last_results']
    
    # Results overview
    st.subheader("📊 Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Topic", results['topic'])
    with col2:
        st.metric("Content Type", results['content_type'])
    with col3:
        st.metric("Processing Time", f"{results['processing_time']:.1f}s")
    with col4:
        st.metric("QA Status", results['qa_report']['approval_status'])
    
    # Content tabs
    content_tab1, content_tab2, content_tab3, content_tab4 = st.tabs(["📄 Final Content", "🔍 SEO Data", "📱 Platform Versions", "📋 QA Report"])
    
    with content_tab1:
        st.subheader("📄 Final Content")
        st.text_area("Generated Content", results['final_content'], height=400)
        
        # Download button
        st.download_button(
            label="📥 Download Content",
            data=results['final_content'],
            file_name=f"{results['topic'].replace(' ', '_')}_content.txt",
            mime="text/plain"
        )
    
    with content_tab2:
        st.subheader("🔍 SEO Optimization Data")
        seo_data = results.get('seo_data', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Meta Title:**")
            st.code(seo_data.get('meta_title', 'N/A'))
            
            st.markdown("**Target Keywords:**")
            keywords = seo_data.get('keywords', [])
            st.write(", ".join(keywords) if keywords else "None")
        
        with col2:
            st.markdown("**Meta Description:**")
            st.code(seo_data.get('meta_description', 'N/A'))
            
            st.markdown("**Keyword Density:**")
            density = seo_data.get('keyword_density', {})
            if density:
                for keyword, data in density.items():
                    st.write(f"• {keyword}: {data['count']} occurrences ({data['density']}%)")
    
    with content_tab3:
        st.subheader("📱 Platform-Specific Versions")
        platform_versions = results.get('platform_versions', {})
        
        if platform_versions:
            for platform, content in platform_versions.items():
                with st.expander(f"{platform.title()} Version"):
                    if isinstance(content, list):
                        for i, item in enumerate(content, 1):
                            st.write(f"**Tweet {i}:** {item}")
                    else:
                        st.text_area(f"{platform} content", content, height=150, key=f"platform_{platform}")
        else:
            st.info("No platform-specific versions were created.")
    
    with content_tab4:
        st.subheader("📋 Quality Assurance Report")
        qa_report = results.get('qa_report', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Overall Score", f"{qa_report.get('overall_score', 0)}/10")
            st.metric("Approval Status", qa_report.get('approval_status', 'Unknown'))
        
        with col2:
            issues = qa_report.get('content_issues', [])
            st.markdown("**Issues Found:**")
            if issues:
                for issue in issues:
                    st.write(f"• {issue}")
            else:
                st.write("✅ No issues found")
        
        # Recommendations
        recommendations = qa_report.get('recommendations', [])
        if recommendations:
            st.markdown("**Recommendations:**")
            for rec in recommendations:
                st.write(f"• {rec}")
    
    # Export options
    st.subheader("📤 Export Options")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Complete results as JSON
        json_data = json.dumps({k: v for k, v in results.items() if k != 'metrics'}, indent=2)
        st.download_button(
            label="📊 Download Complete Results (JSON)",
            data=json_data,
            file_name=f"{results['topic'].replace(' ', '_')}_complete_results.json",
            mime="application/json"
        )
    
    with col2:
        # SEO report
        seo_report = ContentFormatter.format_seo_report(results.get('seo_data', {}))
        st.download_button(
            label="🔍 Download SEO Report",
            data=seo_report,
            file_name=f"{results['topic'].replace(' ', '_')}_seo_report.md",
            mime="text/markdown"
        )
    
    with col3:
        # Blog post format
        blog_content = ContentFormatter.format_blog_post(results['topic'], results['final_content'])
        st.download_button(
            label="📝 Download Blog Post",
            data=blog_content,
            file_name=f"{results['topic'].replace(' ', '_')}_blog_post.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()
