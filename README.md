# reddit-scraper

Extracts Reddit threads with full comment hierarchy using the public JSON API.

## Requirements

- Python 3.8+
- Internet connection

## Installation

```bash
git clone https://github.com/auroraflux/reddit-scraper.git
cd reddit-scraper
pip install -e .
```

## Usage

Start the API server:
```bash
python -m reddit_scraper.server
```

Server runs at http://localhost:8001

Scrape from command line:
```bash
python -m reddit_scraper.scraper https://reddit.com/r/python/comments/abc123/example
```

Use as Python module:
```python
from reddit_scraper import scrape_reddit_post

result = scrape_reddit_post('https://reddit.com/r/python/comments/abc123/example')
print(result['stats']['total_comments'])
```

## API

### POST /scrape

Request:
```json
{
  "url": "https://reddit.com/r/python/comments/abc123/example"
}
```

Response:
```json
{
  "success": true,
  "url": "https://old.reddit.com/r/python/comments/abc123/example",
  "post": {
    "title": "Example Post",
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
      "replies": []
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

### GET /health

Returns server status.

### GET /

Web interface for testing.

### GET /docs

OpenAPI documentation.

## Configuration

The scraper automatically converts reddit.com URLs to old.reddit.com and appends `.json?limit=500`.

No authentication required. No API keys needed.

## Performance

Typical thread: 5-8 seconds (network-bound)

Extracts 100% of visible comments with unlimited nesting depth. Doesn't expand "load more comments" links.

## Limitations

- Reddit only
- Public posts only
- No "load more comments" expansion
- No rate limiting protection

## Development

Run tests:
```bash
pip install -e ".[dev]"
pytest
```

Code must follow docs/guidelines.md:
- Maximum 20 lines per function
- Type hints required
- No magic numbers

## Troubleshooting

Port 8001 already in use:
```bash
# Change port in reddit_scraper/server.py
# Find: port=8001
# Change to: port=8002
```

Module import errors:
```bash
pip install -e .
```

## Documentation

- docs/api-guide.md - Complete API documentation
- docs/scraping-guide.md - Implementation details
- docs/comparison.md - Comparison with alternatives
- docs/guidelines.md - Code standards

## Related

General web scraping with LLM: https://github.com/auroraflux/crawlai-integration

## License

MIT
