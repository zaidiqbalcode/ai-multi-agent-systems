# 🚀 Backend Deployment Guide

## Deploy Python Backend to Railway

### Step 1: Prepare for Deployment
Your backend is now ready for Railway deployment with:
- `railway.json` - Railway configuration
- `Procfile` - Process file for deployment
- Updated `api.py` with production port handling

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up/login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `ai-multi-agent-systems` repository
5. Railway will auto-detect it's a Python project

### Step 3: Set Environment Variables
In Railway dashboard, add these environment variables:
- `GOOGLE_API_KEY` = your Google API key
- `OPENAI_API_KEY` = your OpenAI API key (optional)

### Step 4: Get Your API URL
After deployment, Railway will give you a URL like:
`https://your-app-name.railway.app`

### Step 5: Update Frontend
In Netlify, add environment variable:
- `REACT_APP_API_URL` = `https://your-app-name.railway.app`

## Alternative: Render Deployment
1. Go to [render.com](https://render.com)
2. Connect your GitHub repo
3. Choose "Web Service"
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python api.py`
5. Add environment variables in Render dashboard

## Alternative: Quick Demo Fix
If you just need the demo to work for assignment submission, you can temporarily add a fallback to mock data when the API fails.
