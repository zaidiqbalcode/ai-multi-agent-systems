# AI Multi-Agent System - Backend

This is the backend API for the AI Multi-Agent Content Creation System built with CrewAI framework.

## Features

- 6 Specialized AI Agents (Research, Writer, Editor, SEO, Platform, QA)
- Google Gemini API Integration
- Flask REST API
- CORS enabled for frontend integration
- Production-ready deployment configuration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Add your GOOGLE_API_KEY to .env
```

3. Run the API:
```bash
python api.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /health` - Health check
- `POST /api/content` - Generate content using AI agents

### Content Generation Request Format:
```json
{
  "topic": "Your content topic",
  "audience": "target audience",
  "content_type": "blog_post",
  "platform": "website"
}
```

## Deployment

### Railway
```bash
# Deploy to Railway
railway login
railway init
railway deploy
```

### Render
- Connect your GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `python api.py`
- Add environment variable: `GOOGLE_API_KEY`

### Heroku
```bash
# Deploy to Heroku
heroku create your-app-name
heroku config:set GOOGLE_API_KEY=your_api_key
git push heroku main
```

## Environment Variables

- `GOOGLE_API_KEY` - Your Google Gemini API key
- `PORT` - Port for the API (default: 5000)
- `FLASK_ENV` - Environment (production/development)

## Project Structure

```
backend/
├── agents/              # AI agent definitions
├── config/             # Configuration files
├── utils/              # Utility functions
├── api.py              # Main Flask API
├── main.py             # CrewAI pipeline
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment
├── railway.json       # Railway deployment
└── .env.example       # Environment template
```
