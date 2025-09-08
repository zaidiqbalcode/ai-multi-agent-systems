# 🚀 Backend Deployment Guide

## Quick Deploy to Railway (Recommended)

### Step 1: Railway Setup
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account and select `ai-multi-agent-systems`

### Step 2: Configure Railway
1. **Build Command**: `pip install -r requirements.txt`
2. **Start Command**: `python api.py`
3. **Port**: Railway will auto-detect from the code

### Step 3: Environment Variables
Add these environment variables in Railway dashboard:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 4: Deploy
1. Click "Deploy"
2. Wait for build to complete
3. Copy the generated URL (e.g., `https://your-app.railway.app`)

---

## Alternative: Deploy to Render

### Step 1: Render Setup
1. Go to [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repo

### Step 2: Configure Render
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python api.py`
- **Environment**: Python 3

### Step 3: Environment Variables
Add in Render dashboard:
```
GOOGLE_API_KEY=your_google_api_key_here
```

---

## Alternative: Deploy to Heroku

### Step 1: Heroku Setup
```bash
# Install Heroku CLI first
heroku create your-app-name
```

### Step 2: Deploy
```bash
git push heroku main
```

### Step 3: Set Environment Variables
```bash
heroku config:set GOOGLE_API_KEY=your_google_api_key_here
```

---

## After Deployment

### Update Frontend
Once deployed, update your frontend to use the new backend URL:

1. Get your deployed backend URL (e.g., `https://your-app.railway.app`)
2. Update the frontend code (this will be done automatically)

### Test Your API
Test these endpoints:
- `GET https://your-app.railway.app/api/health` - Should return status
- `POST https://your-app.railway.app/api/create-content` - Content creation

---

## Troubleshooting

### Common Issues:
1. **Build fails**: Check requirements.txt has all dependencies
2. **API errors**: Verify GOOGLE_API_KEY is set correctly
3. **CORS errors**: Make sure your Netlify domain is in CORS origins

### Check Logs:
- **Railway**: View logs in Railway dashboard
- **Render**: Check logs in Render dashboard
- **Heroku**: `heroku logs --tail`

---

## 🎯 Success Metrics

Once deployed, you should have:
✅ Backend API running on cloud platform  
✅ Health check endpoint responding  
✅ Content creation API working  
✅ Frontend connecting to deployed backend  
✅ Full AI multi-agent system operational  

Your backend URL will be something like:
- Railway: `https://ai-multi-agent-systems-production.up.railway.app`
- Render: `https://your-service-name.onrender.com`
- Heroku: `https://your-app-name.herokuapp.com`
