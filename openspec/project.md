# Project Overview

## Purpose
reddit-scraper is a lightweight Python package for extracting Reddit threads with complete comment hierarchy using Reddit's public JSON API. It provides both a CLI tool and REST API server for deterministic, cost-free Reddit scraping.

**Key Value Propositions:**
- **FREE**: No API costs, no authentication required
- **Complete**: Extracts 100% of comments with unlimited nesting depth
- **Fast**: 5-8 seconds per thread
- **Simple**: Uses Reddit's public JSON API (append `.json` to URL)
- **Pip-installable**: Standard Python package with console scripts

## Tech Stack

### Runtime Environment
- **Python**: 3.8+ (3.14 tested)
- **Virtual Environment**: `.venv/` (gitignored, managed with uv or venv)
- **Package Manager**: pip (requirements.txt) or uv

### Core Dependencies
- **fastapi** (>=0.100.0): REST API server framework
- **uvicorn** (>=0.20.0): ASGI server for FastAPI
- **pydantic** (>=2.0.0): Data validation and settings
- **requests** (>=2.28.0): HTTP client for Reddit JSON API

### Development Tools
- **pytest**: Testing framework (dev dependency)
- **OpenSpec**: Spec-driven development workflow

## Project Structure

```
reddit-scraper/
├── reddit_scraper/          # Package directory
│   ├── __init__.py         # Package initialization and exports
│   ├── scraper.py          # Core scraping logic (CLI)
│   └── server.py           # FastAPI REST server
├── docs/                    # Documentation
│   ├── api-guide.md        # API server documentation
│   ├── scraping-guide.md   # Implementation details
│   ├── comparison.md       # vs other approaches
│   ├── guidelines.md       # Code quality standards
│   └── README.md           # Documentation index
├── scripts/                 # Utility scripts
│   └── start_server.sh     # Server startup script
├── tests/                   # Test files (pytest)
├── openspec/                # Spec-driven development
│   ├── project.md          # This file
│   ├── AGENTS.md           # OpenSpec workflow instructions
│   ├── specs/              # Current specifications
│   └── changes/            # Proposed changes
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
├── .gitignore              # Python-specific patterns
├── MANIFEST.in             # Include non-Python files
├── README.md               # Package documentation
└── LICENSE                 # MIT License
```

## Code Conventions

### Code Quality Standards
Strictly follow `docs/guidelines.md` for all code:
- **Maximum 20 lines per function** (Section III)
- **No magic numbers** - use named constants (Section V)
- **Type hints required** for all functions (Section VI)
- **Comprehensive docstrings** (Section VII)
- **No duplicated code** (Section VIII)
- **Single responsibility** per function (Section IX)
- **Proper error handling** (Section X)

### Module Structure
- **Package imports**: Use `from reddit_scraper import scrape_reddit_post`
- **Module execution**: Run as `python -m reddit_scraper.scraper` or `python -m reddit_scraper.server`
- **Entry points**: Console scripts defined in setup.py:
  - `reddit-scraper` → CLI scraper
  - `reddit-scraper-server` → API server

### Naming Conventions
- **Functions**: `snake_case` (e.g., `scrape_reddit_post()`)
- **Classes**: `PascalCase` (e.g., `ScrapeRequest`)
- **Constants**: `UPPER_CASE` (e.g., `DEFAULT_PORT`)
- **Private functions**: `_leading_underscore`

### File Organization
- Keep functions ≤20 lines
- One primary class/concept per file
- Group related utilities in private functions
- Validate with pylint/mypy for quality

## Domain Context

### Reddit JSON API
- **Endpoint pattern**: Append `.json` to any Reddit URL
- **URL normalization**: Always convert to `old.reddit.com` format
- **Data structure**: Nested JSON with `children` arrays for comments
- **Rate limits**: Respectful requests (no authentication needed for public data)

### Comment Hierarchy
- **Top-level comments**: Direct replies to post (depth 0)
- **Nested replies**: Recursive structure (unlimited depth)
- **More comments**: Handled via `kind: "more"` objects (currently limits to visible comments)
- **Metadata**: author, score, timestamp, text for each comment

### API Response Structure
```json
{
  "success": true,
  "url": "https://old.reddit.com/r/python/...",
  "post": {
    "title": "...",
    "author": "...",
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
      "text": "...",
      "timestamp": 1234567890,
      "replies": [...]
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

## Constraints

### Technical Constraints
- **Reddit only**: Does not work for other websites
- **Public data only**: Cannot access private subreddits without authentication
- **Visible comments only**: Does not expand "load more comments" links
- **No authentication**: Intentionally avoids Reddit API keys to stay free

### Design Constraints
- **No browser automation**: Uses direct HTTP requests
- **No external APIs**: No LLM or third-party services
- **No database**: Stateless scraping (no caching)
- **Synchronous scraping**: Sequential requests to Reddit

### Performance Constraints
- **Network-bound**: 5-8 seconds per thread (Reddit response time)
- **Memory**: Entire thread loaded into memory
- **Concurrency**: Server uses subprocess to avoid async/sync conflicts

## Dependencies

### Runtime Dependencies
```
fastapi>=0.100.0      # REST API framework
uvicorn>=0.20.0       # ASGI server
pydantic>=2.0.0       # Data validation
requests>=2.28.0      # HTTP client
```

### Development Dependencies
```
pytest>=7.0.0         # Testing framework
pytest-cov>=4.0.0     # Coverage reporting
```

### System Requirements
- Python 3.8+ (tested on 3.14)
- No additional system dependencies

## Use Cases

### Primary Use Cases
1. **LLM Context**: Provide Reddit discussion context to Claude/ChatGPT
2. **Research**: Analyze technical discussions and community sentiment
3. **Archiving**: Save important threads for reference
4. **Personal Tools**: Build custom Reddit analysis tools

### Anti-Use Cases (DO NOT USE FOR)
- Mass scraping thousands of threads
- Commercial data collection
- Training LLMs or ML models
- Systematic data harvesting
- Violating Reddit's Terms of Service

## Development Workflow

### OpenSpec Integration
- **Spec-driven development**: Create proposals before implementation
- **Validation**: `openspec validate --strict` before commits
- **Change management**: Track all changes in `openspec/changes/`
- **Archiving**: Move completed changes to `changes/archive/`

### Testing
```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=reddit_scraper
```

### Version Management
- **Semantic versioning**: MAJOR.MINOR.PATCH
- **Version location**: `reddit_scraper/__init__.py`
- **Release process**: Tag commits with `vX.Y.Z`

## Comparison with Other Tools

| Feature | reddit-scraper | LLM-based scrapers | Browser automation |
|---------|----------------|-------------------|-------------------|
| **Cost** | FREE | ~$0.002/page | FREE |
| **Speed** | 5-8 seconds | 10-15 seconds | 30-60 seconds |
| **Accuracy** | 100% (deterministic) | ~95% (LLM) | 100% |
| **Completeness** | All visible comments | Partial (token limits) | All comments |
| **Sites** | Reddit only | Any website | Any website |
| **Reliability** | High (JSON API) | Medium (LLM) | Low (fragile) |

**When to use reddit-scraper:**
- Scraping Reddit threads
- Need 100% accuracy
- Want zero cost
- Building automated tools

**When to use alternatives:**
- Need to scrape non-Reddit websites → Use LLM-based tools (Crawl4AI, etc.)
- Need authenticated Reddit access → Use PRAW library
- Need "load more comments" → Use PRAW library

## Contributing

### Code Quality
1. Follow `docs/guidelines.md` strictly
2. Add tests for new features
3. Update documentation
4. Run `openspec validate --strict` before submitting

### Pull Request Process
1. Create OpenSpec proposal for significant changes
2. Implement changes following proposal
3. Archive proposal after deployment
4. Update specs in `openspec/specs/`

## License
MIT License (see LICENSE file)

## Related Projects
- **crawlai-integration**: General web scraping with LLM support (Crawl4AI + Gemini)
- **PRAW**: Official Reddit API wrapper (requires authentication)
- **Crawl4AI**: Universal web scraper with LLM extraction

---

**Last Updated**: 2025-10-25
**OpenSpec Version**: 1.0
