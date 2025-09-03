# 🔑 API Keys Setup Guide

## Quick Setup

### 1. Get Your API Keys

#### OpenAI API Key (Recommended)
1. Visit: https://platform.openai.com/api-keys
2. Sign up/login to your OpenAI account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

#### Google Gemini API Key (Alternative)
1. Visit: https://aistudio.google.com/app/apikey
2. Sign up/login to your Google account
3. Click "Create API Key"
4. Copy the key

### 2. Add Keys to Your Project

Edit the `.env` file in your project root:

```bash
# Replace with your actual keys
OPENAI_API_KEY=sk-your-actual-openai-key-here
GOOGLE_API_KEY=your-actual-google-key-here
```

### 3. Test Your Setup

```bash
python test_api_keys.py
```

## 💰 Cost Information

### OpenAI Pricing (Most Popular)
- **GPT-3.5 Turbo**: $0.0015/1K input tokens, $0.002/1K output tokens
- **GPT-4**: $0.03/1K input tokens, $0.06/1K output tokens
- **Free tier**: $5 credit for new accounts

### Google Gemini Pricing
- **Gemini Pro**: Free up to 60 requests/minute
- Very generous free tier for development

## 🚀 Running Your AI Agents

### Option 1: Demo Mode (No API required)
```bash
python demo.py
```

### Option 2: Full Pipeline with APIs
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

# Or run React frontend
cd frontend
npm start
```

### Option 3: Test Individual Components
```bash
# Test main pipeline
python main.py

# Test API backend
python api.py
```

## 🔒 Security Tips

1. **Never commit `.env` file** - it's already in `.gitignore`
2. **Use environment variables** in production
3. **Rotate keys regularly**
4. **Monitor usage** on provider dashboards
5. **Set spending limits** to avoid unexpected charges

## 🎯 Recommended Setup for Assignment

For your CODING NINJAS assignment, I recommend:

1. **Start with OpenAI GPT-3.5 Turbo** (cheapest, fastest)
2. **Get $5 free credit** with new account
3. **Test with demo first** to see the system working
4. **Add API keys only when ready** to showcase live functionality

## 📞 Support

If you need help:
- Check the test script output
- Verify your API keys are correct
- Ensure you have credits/quota remaining
- Contact the provider support if needed

## 🎉 You're Ready!

Once your API keys are set up, your AI Multi-Agent system will:
- Generate real content using 6 specialized agents
- Create professional blog posts, social media content
- Optimize for SEO and different platforms
- Provide a complete content creation pipeline
