# Smart Content Creation Pipeline - Setup Guide

## Full Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <your-repository-url>
cd smart-content-pipeline
```

### 2. Install Dependencies

#### Option A: Using pip
```bash
pip install -r requirements.txt
```

#### Option B: Using conda
```bash
conda create -n content-pipeline python=3.9
conda activate content-pipeline
pip install -r requirements.txt
```

### 3. Environment Configuration

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Edit `.env` and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Getting API Keys

#### OpenAI API Key (Recommended)
1. Visit [OpenAI Platform](https://platform.openai.com)
2. Create an account or sign in
3. Go to API Keys section
4. Create a new API key
5. Copy and paste into your `.env` file

#### Google Gemini API Key (Free Alternative)
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and paste into your `.env` file

### 5. Running the Application

#### Web Interface (Streamlit)
```bash
streamlit run app.py
```

#### Command Line Interface
```bash
python main.py
```

## Project Structure

```
smart-content-pipeline/
├── agents/                 # AI agent implementations
│   ├── __init__.py
│   ├── research_agent.py   # Research and fact-gathering
│   ├── writer_agent.py     # Content creation
│   ├── editor_agent.py     # Content editing and improvement
│   ├── seo_agent.py       # SEO optimization
│   ├── platform_agent.py  # Platform-specific adaptation
│   └── qa_agent.py        # Quality assurance
├── config/                 # Configuration files
│   └── agent_config.yaml  # Agent settings and parameters
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── helpers.py         # Helper functions and utilities
├── output/                 # Generated content (created automatically)
├── app.py                 # Streamlit web interface
├── main.py                # Main pipeline orchestrator
├── api.py                 # Flask API backend
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # Project documentation
```

## Usage Examples

### Web Interface
1. Run `streamlit run app.py`
2. Open your browser to the displayed URL
3. Configure your API key in the sidebar
4. Fill in the content creation form
5. Click "Generate Content"
6. View results in the Results tab

### Command Line
```python
from main import SmartContentPipeline

pipeline = SmartContentPipeline(llm_provider="openai")

results = pipeline.create_content(
    topic="Machine Learning for Beginners",
    content_type="blog_post",
    target_audience="students",
    tone="casual",
    platforms=["linkedin", "twitter"],
    target_keywords=["machine learning", "AI basics", "beginner guide"]
)

print("Content created successfully!")
print(f"Processing time: {results['processing_time']:.2f} seconds")
```

## Configuration Options

### LLM Providers
- **OpenAI**: `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`
- **Google**: `gemini-1.5-flash`

### Content Types
- `blog_post` - Long-form blog content
- `article` - News/magazine style articles
- `whitepaper` - Technical documentation
- `social_media_post` - Short-form social content
- `newsletter` - Email newsletter content

### Target Audiences
- `general audience` - Broad appeal content
- `professionals` - Business/industry focused
- `students` - Educational content
- `entrepreneurs` - Startup/business focused
- `technical experts` - Deep technical content

### Platforms
- `twitter` - 280 character limit, hashtag optimization
- `linkedin` - Professional networking focus
- `facebook` - Engagement-focused formatting
- `instagram` - Visual-first storytelling
- `blog` - Long-form, SEO-optimized content

## Troubleshooting

### Common Issues

1. **Import Error: crewai not found**
   ```bash
   pip install crewai
   ```

2. **API Key Not Working**
   - Verify the key is correctly set in `.env`
   - Check that you have credits/quota remaining
   - Ensure the key has the correct permissions

3. **Streamlit Not Starting**
   ```bash
   pip install streamlit
   streamlit run app.py
   ```

4. **Permission Errors**
   - Ensure you have write permissions in the project directory
   - Try running as administrator (Windows) or with sudo (Linux/Mac)

### Performance Optimization

1. **Faster Processing**: Use `gpt-3.5-turbo` instead of `gpt-4`
2. **Lower Costs**: Use Google Gemini (free tier available)
3. **Batch Processing**: Create multiple content pieces in sequence

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes as part of the CODING NINJAS assignment.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the main.py file for working examples
3. Ensure all dependencies are properly installed
4. Verify API keys are correctly configured

## Next Steps

After setting up the project:
1. Run the main pipeline to understand the workflow
2. Try the web interface with your own topics
3. Experiment with different content types and platforms
4. Customize agent behaviors in the config files
5. Extend the system with additional agents or features
