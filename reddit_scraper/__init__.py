"""
reddit_scraper - Lightweight Reddit thread scraper with full comment hierarchy

A Python package for scraping Reddit threads using the public JSON API.
Features:
- 100% comment extraction with unlimited nesting depth
- FREE (no LLM costs, no API authentication needed)
- Fast (5-8 seconds per thread)
- FastAPI REST server with web interface
- CLI tool for standalone usage

Usage:
    # As a module
    from reddit_scraper.scraper import scrape_reddit_post
    result = scrape_reddit_post('https://reddit.com/r/python/comments/...')

    # CLI
    python -m reddit_scraper.scraper <reddit_url>

    # API Server
    python -m reddit_scraper.server
"""

__version__ = '1.0.0'
__author__ = 'reddit-scraper contributors'

from reddit_scraper.scraper import scrape_reddit_post

__all__ = ['scrape_reddit_post']
