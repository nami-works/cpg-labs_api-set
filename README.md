# CPG Labs APIs

AI-powered APIs for content generation using CrewAI.

## 🚀 Available APIs

- **SEO Lab** (`/api/seo`) - SEO content generation using CrewAI multi-agent system

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/nami-works/cpg-labs_apis.git
cd cpg-labs_apis

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your API keys

# Run locally
python main.py
```

## 🔧 Development

```bash
# Run with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run individual API
python apis/seo_lab/api_service.py
```

## 📚 API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 🎯 SEO Lab API

### Endpoints

- `POST /api/seo/generate` - Generate SEO blog content
- `GET /api/seo/health` - Health check

### Request Format

```json
{
  "brand": "Your Brand Name",
  "topic": "Content Topic",
  "keywords": ["keyword1", "keyword2"],
  "outline": ["point1", "point2"],
  "tone": "informative",
  "wordCount": 1500,
  "language": "pt-BR",
  "additionalContext": "Additional context"
}
```

### Response Format

```json
{
  "html": "<h1>Generated Content</h1><p>...</p>",
  "meta": {
    "title": "SEO Title",
    "description": "Meta description",
    "keywords": ["keyword1", "keyword2"]
  },
  "stats": {
    "tokens": 1500,
    "durationMs": 30000
  },
  "traceId": "uuid-trace-id"
}
```

## 🚀 Deployment

### Render.com

1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python main.py`
4. Add environment variables from `env.example`

### Environment Variables

Required:
- `OPENAI_API_KEY` - OpenAI API key for CrewAI
- `EDGE_API_KEY` - API key for authentication

Optional:
- `ANTHROPIC_API_KEY` - Anthropic API key
- `SHOPIFY_SHOP_NAME` - Shopify shop name
- `SHOPIFY_ACCESS_TOKEN` - Shopify access token

## 🏗️ Architecture

```
cpg-labs_apis/
├── main.py                 # Main FastAPI application
├── requirements.txt        # Python dependencies
├── apis/
│   └── seo_lab/           # SEO Lab API module
│       ├── api_service.py # FastAPI service
│       ├── src/           # CrewAI source code
│       └── requirements.txt
└── README.md
```

## 📝 License

MIT License
