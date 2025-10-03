# CPG Labs APIs - Deployment Guide

## 🚀 Quick Deploy to Render.com

### 1. Repository Setup

1. **Create GitHub Repository**
   - Repository name: `cpg-labs_apis`
   - Make it public or private (your choice)
   - Push the code to GitHub

2. **Repository Structure**
   ```
   cpg-labs_apis/
   ├── main.py                 # Main FastAPI application
   ├── requirements.txt        # Python dependencies
   ├── Dockerfile             # Docker configuration
   ├── docker-compose.yml     # Local development
   ├── apis/
   │   └── seo_lab/           # SEO Lab API
   │       ├── api_service.py
   │       ├── context_chunking.py
   │       ├── src/
   │       └── requirements.txt
   └── README.md
   ```

### 2. Render.com Deployment

#### 2.1 Create New Web Service

1. Go to [Render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository `cpg-labs_apis`

#### 2.2 Configure Service Settings

- **Name**: `cpg-labs-apis` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python main.py`

#### 2.3 Environment Variables

Add these environment variables in Render.com:

**Required:**
```
OPENAI_API_KEY=your-openai-api-key-here
EDGE_API_KEY=your-secret-api-key-here
```

**Optional:**
```
ANTHROPIC_API_KEY=your-anthropic-key-here
SHOPIFY_SHOP_NAME=your-shop-name
SHOPIFY_ACCESS_TOKEN=your-shopify-token
```

#### 2.4 Deploy

1. Click **"Create Web Service"**
2. Wait for deployment to complete
3. Your API will be available at: `https://your-app-name.onrender.com`

### 3. API Endpoints

Once deployed, your API will have these endpoints:

- **Health Check**: `GET /health`
- **API Info**: `GET /`
- **SEO Lab**: `POST /api/seo/generate`
- **Documentation**: `GET /docs` (Swagger UI)

### 4. Testing the API

#### 4.1 Health Check
```bash
curl https://your-app-name.onrender.com/health
```

#### 4.2 Generate Blog Content
```bash
curl -X POST "https://your-app-name.onrender.com/api/seo/generate" \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-secret-api-key-here" \
  -d '{
    "brand": "Nami Works",
    "topic": "The Future of AI in Content Creation",
    "keywords": ["AI content", "future tech", "content marketing"],
    "language": "en-US",
    "wordCount": 1000,
    "additionalContext": "Focus on benefits for small businesses."
  }'
```

### 5. Local Development

#### 5.1 Run Locally
```bash
# Clone repository
git clone https://github.com/your-username/cpg-labs_apis.git
cd cpg-labs_apis

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp env.example .env
# Edit .env with your API keys

# Run the application
python main.py
```

#### 5.2 Docker Development
```bash
# Build and run with Docker
docker-compose up --build

# Or run individual API
cd apis/seo_lab
python api_service.py
```

### 6. Monitoring and Logs

#### 6.1 Render.com Logs
- Go to your service dashboard
- Click **"Logs"** tab
- Monitor real-time logs and errors

#### 6.2 Health Monitoring
- Use the `/health` endpoint for monitoring
- Set up uptime monitoring with services like UptimeRobot

### 7. Scaling and Performance

#### 7.1 Render.com Scaling
- **Free Tier**: 750 hours/month, sleeps after 15 minutes of inactivity
- **Starter Plan**: $7/month, always on, better performance
- **Professional Plan**: $25/month, auto-scaling, better resources

#### 7.2 Performance Optimization
- Use connection pooling for database connections
- Implement caching for frequently requested data
- Monitor memory usage and optimize accordingly

### 8. Troubleshooting

#### 8.1 Common Issues

**Build Failures:**
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Check for missing system dependencies

**Runtime Errors:**
- Verify all environment variables are set
- Check API key validity
- Monitor logs for specific error messages

**Timeout Issues:**
- Increase timeout settings in Render.com
- Optimize CrewAI execution time
- Consider implementing async processing

#### 8.2 Debug Mode

Enable debug mode locally:
```bash
export DEBUG=True
python main.py
```

### 9. Security Considerations

#### 9.1 API Key Security
- Never commit API keys to version control
- Use environment variables for all secrets
- Rotate API keys regularly

#### 9.2 CORS Configuration
- Update CORS settings for production
- Restrict origins to your frontend domains
- Remove wildcard (*) origins in production

### 10. Next Steps

1. **Deploy to Render.com** following this guide
2. **Test the API** with your frontend application
3. **Monitor performance** and optimize as needed
4. **Add more APIs** as your project grows
5. **Set up monitoring** and alerting

## 📞 Support

If you encounter any issues:
1. Check the logs in Render.com dashboard
2. Verify environment variables are set correctly
3. Test the API endpoints individually
4. Check the CrewAI documentation for specific errors

## 🔗 Useful Links

- [Render.com Documentation](https://render.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
