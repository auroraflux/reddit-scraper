# reddit-scraper

Lightweight Reddit thread scraper with full comment hierarchy. **FREE**, **fast** (5-8s), **100% extraction**.

## Features

- ✅ **FREE** - No LLM costs, no API authentication required
- ✅ **Complete** - Extracts 100% of comments with unlimited nesting depth
- ✅ **Fast** - 5-8 seconds per thread
- ✅ **Simple** - Uses Reddit's public JSON API
- ✅ **REST API** - FastAPI server with web interface
- ✅ **CLI Tool** - Standalone command-line usage
- ✅ **Pip-installable** - Easy installation and integration

## Quick Start

### Installation

```bash
# Install from source
git clone https://github.com/auroraflux/reddit-scraper.git
cd reddit-scraper
pip install -e .
```

### Usage

**Option 1: API Server (Recommended)**

```bash
# Start the server
./scripts/start_server.sh
# Or: python -m reddit_scraper.server

# Open web interface
open http://localhost:8001
```

**Option 2: CLI**

```bash
python -m reddit_scraper.scraper https://reddit.com/r/python/comments/...
```

**Option 3: Python Module**

```python
from reddit_scraper import scrape_reddit_post

result = scrape_reddit_post('https://reddit.com/r/python/comments/...')
print(f"Found {len(result['comments'])} top-level comments")
```

## API Documentation

### REST API Endpoints

**Start Server:** `python -m reddit_scraper.server`
**Server URL:** `http://localhost:8001`

#### `POST /scrape`

Scrape a Reddit thread and return structured JSON.

**Request:**
```json
{
  "url": "https://reddit.com/r/python/comments/abc123/test"
}
```

**Response:**
```json
{
  "success": true,
  "url": "https://old.reddit.com/r/python/comments/abc123/test",
  "post": {
    "title": "Post title",
    "author": "username",
    "score": 123,
    "timestamp": 1234567890,
    "subreddit": "python",
    "num_comments": 37
  },
  "comments": [
    {
      "id": "abc",
      "author": "user1",
      "score": 45,
      "text": "Comment text",
      "timestamp": 1234567890,
      "replies": [
        {
          "author": "user2",
          "text": "Reply text",
          "replies": [...]
        }
      ]
    }
  ],
  "stats": {
    "total_comments": 37,
    "top_level_comments": 13,
    "max_depth": 5,
    "comments_by_depth": {"0": 13, "1": 18, "2": 6}
  }
}
```

#### `GET /health`

Health check endpoint.

#### `GET /`

Web interface for interactive testing.

#### `GET /docs`

Swagger UI documentation.

## Features in Detail

### Complete Comment Extraction

- Extracts **100% of visible comments** (not just partial)
- Preserves **unlimited nesting depth** (5+ levels)
- Maintains **exact hierarchy** as shown on Reddit
- Includes comment metadata: author, score, timestamp, text

### Automatic URL Handling

Automatically converts any Reddit URL format:
- `reddit.com` → `old.reddit.com`
- `www.reddit.com` → `old.reddit.com`
- Works with any post URL format

### Fast & Reliable

- **5-8 seconds** per thread (network-bound)
- Uses Reddit's official JSON API
- No browser automation needed
- Deterministic results (always same output)

### FREE

- **No API costs** (unlike LLM-based scrapers)
- **No authentication** required
- **No rate limits** for personal use
- Just respectful HTTP requests

## Use Cases

**Perfect for:**
- Providing Reddit discussion context to LLMs (Claude, ChatGPT)
- Understanding community sentiment before posting
- Researching technical discussions
- Archiving important threads
- Analyzing comment patterns

**Not for:**
- Mass scraping thousands of threads
- Commercial data collection
- Training LLMs or ML models
- Systematic data harvesting

## Architecture

```
reddit-scraper/
├── reddit_scraper/          # Package directory
│   ├── __init__.py         # Package initialization
│   ├── scraper.py          # Core scraping logic
│   └── server.py           # FastAPI REST server
├── docs/                    # Documentation
│   ├── api-guide.md        # API server guide
│   ├── scraping-guide.md   # Implementation details
│   ├── comparison.md       # vs other approaches
│   └── guidelines.md       # Code standards
├── scripts/                 # Utility scripts
│   └── start_server.sh     # Server startup script
├── tests/                   # Test files
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
└── README.md                # This file
```

## Requirements

- **Python 3.8+**
- Dependencies (auto-installed):
  - `fastapi>=0.100.0`
  - `uvicorn>=0.20.0`
  - `pydantic>=2.0.0`
  - `requests>=2.28.0`

## Documentation

- **[API Guide](./docs/api-guide.md)** - Complete API server documentation
- **[Scraping Guide](./docs/scraping-guide.md)** - Implementation details and usage patterns
- **[Comparison](./docs/comparison.md)** - reddit-scraper vs other approaches
- **[Guidelines](./docs/guidelines.md)** - Code quality standards

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest
```

### Code Standards

This project follows strict code quality standards defined in [docs/guidelines.md](./docs/guidelines.md):
- Maximum 20 lines per function
- Type hints required
- Comprehensive docstrings
- No magic numbers or duplicated code

## Comparison

| Feature | reddit-scraper | LLM-based scrapers |
|---------|----------------|-------------------|
| **Cost** | FREE | ~$0.002/page |
| **Speed** | 5-8 seconds | 10-15 seconds |
| **Accuracy** | 100% (deterministic) | ~95% (LLM) |
| **Comments** | All (unlimited depth) | Partial (token limits) |
| **Sites** | Reddit only | Any website |

**For Reddit:** Use reddit-scraper
**For other websites:** Use LLM-based tools like Crawl4AI

## Contributing

1. Follow [docs/guidelines.md](./docs/guidelines.md) standards
2. Add tests for new features
3. Update documentation
4. Submit pull requests

## License

[Add license here - MIT recommended]

## Acknowledgments

Extracted from the [crawlAI](https://github.com/auroraflux/crawlai-integration) project to provide a focused, single-purpose tool for Reddit scraping.

For general web scraping with LLM support, see [crawlai-integration](https://github.com/auroraflux/crawlai-integration).

---

**Last Updated:** 2025-10-25
