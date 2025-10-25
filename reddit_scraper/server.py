#!/usr/bin/env python3
"""
Reddit Scraper API Server
A lightweight FastAPI server for scraping Reddit threads with full comment hierarchy.

Usage:
    python -m reddit_scraper.server

API Endpoints:
    POST /scrape - Scrape a Reddit URL
    GET /health - Health check
    GET / - Simple web interface
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, List
import re
from contextlib import asynccontextmanager

# Import scraper components
import subprocess
import json as json_module
import sys


# Startup/shutdown logic
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for the API"""
    print("🚀 Reddit Scraper API starting...")
    print("📍 Server running at: http://localhost:8001")
    print("📖 API docs at: http://localhost:8001/docs")
    print("🌐 Web interface at: http://localhost:8001")
    yield
    print("👋 Reddit Scraper API shutting down...")


app = FastAPI(
    title="Reddit Scraper API",
    description="Extract Reddit threads with full comment hierarchy - NO LLM costs!",
    version="1.0.0",
    lifespan=lifespan
)


class ScrapeRequest(BaseModel):
    """Request model for scraping Reddit URLs"""
    url: str = Field(..., description="Reddit post URL (reddit.com or old.reddit.com)")

    @field_validator('url')
    @classmethod
    def validate_reddit_url(cls, v: str) -> str:
        """Validate and normalize Reddit URLs"""
        # Convert to old.reddit.com automatically
        if 'reddit.com' in v:
            # Remove www. if present
            v = v.replace('www.reddit.com', 'reddit.com')
            # Convert to old.reddit.com
            if 'old.reddit.com' not in v:
                v = v.replace('reddit.com', 'old.reddit.com')

        # Basic validation
        if not re.match(r'https?://old\.reddit\.com/r/\w+/comments/', v):
            raise ValueError(
                "Invalid Reddit URL. Expected format: "
                "https://reddit.com/r/subreddit/comments/post_id/..."
            )

        return v


class ScrapeResponse(BaseModel):
    """Response model for scraped Reddit data"""
    success: bool
    url: str
    post: Dict
    comments: List[Dict]
    stats: Dict = Field(default_factory=dict)


def count_comments_recursive(comments: List[Dict], depth: int = 0, stats: Optional[Dict] = None) -> int:
    """Count total comments and calculate stats"""
    if stats is None:
        stats = {'max_depth': 0, 'by_depth': {}}

    total = 0
    for comment in comments:
        total += 1
        stats['max_depth'] = max(stats['max_depth'], depth)
        stats['by_depth'][depth] = stats['by_depth'].get(depth, 0) + 1

        if comment.get('replies'):
            total += count_comments_recursive(comment['replies'], depth + 1, stats)

    return total


@app.get("/", response_class=HTMLResponse)
async def root():
    """Simple web interface for testing the API"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reddit Scraper</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f5f5f5;
                min-height: 100vh;
                padding: 40px 20px;
            }
            .container {
                background: white;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                padding: 32px;
                max-width: 900px;
                margin: 0 auto;
            }
            h1 {
                color: #1a1a1a;
                margin-bottom: 8px;
                font-size: 24px;
                font-weight: 600;
            }
            .subtitle {
                color: #666;
                margin-bottom: 32px;
                font-size: 14px;
            }
            .input-group {
                margin-bottom: 24px;
            }
            label {
                display: block;
                margin-bottom: 6px;
                color: #333;
                font-weight: 500;
                font-size: 14px;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px 12px;
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                font-size: 14px;
                transition: border-color 0.2s;
                font-family: monospace;
            }
            input[type="text"]:focus {
                outline: none;
                border-color: #4a5568;
            }
            .button-group {
                display: flex;
                gap: 12px;
            }
            button {
                background: #2d3748;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: 500;
                cursor: pointer;
                transition: background 0.2s;
            }
            button:hover {
                background: #1a202c;
            }
            button:active {
                background: #000;
            }
            button:disabled {
                background: #9ca3af;
                cursor: not-allowed;
            }
            button.primary {
                flex: 1;
            }
            .result {
                margin-top: 32px;
                padding: 0;
                display: none;
            }
            .result.show {
                display: block;
            }
            .result h3 {
                color: #1a1a1a;
                margin-bottom: 16px;
                font-size: 16px;
                font-weight: 600;
            }
            .result-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
            }
            .copy-button {
                background: #4a5568;
                color: white;
                border: none;
                padding: 8px 14px;
                border-radius: 4px;
                font-size: 13px;
                font-weight: 500;
                cursor: pointer;
                transition: background 0.2s;
            }
            .copy-button:hover {
                background: #2d3748;
            }
            .copy-button:active {
                background: #1a202c;
            }
            .copy-button.copied {
                background: #059669;
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 12px;
                margin-bottom: 16px;
                padding: 16px;
                background: #f9fafb;
                border: 1px solid #e5e7eb;
                border-radius: 4px;
            }
            .stat {
                text-align: left;
            }
            .stat-value {
                font-size: 20px;
                font-weight: 600;
                color: #1a1a1a;
            }
            .stat-label {
                font-size: 12px;
                color: #6b7280;
                margin-top: 2px;
            }
            pre {
                background: #f9fafb;
                color: #1a1a1a;
                padding: 16px;
                border: 1px solid #e5e7eb;
                border-radius: 4px;
                overflow-x: auto;
                font-size: 12px;
                font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
                max-height: 500px;
                overflow-y: auto;
                line-height: 1.5;
            }
            .error pre {
                background: #fef2f2;
                border-color: #fecaca;
                color: #991b1b;
            }
            .example {
                font-size: 12px;
                color: #9ca3af;
                margin-top: 4px;
            }
            .footer {
                margin-top: 32px;
                padding-top: 24px;
                border-top: 1px solid #e5e7eb;
                text-align: center;
            }
            .footer a {
                color: #4a5568;
                text-decoration: none;
                margin: 0 12px;
                font-size: 13px;
            }
            .footer a:hover {
                color: #1a202c;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Reddit Scraper</h1>
            <p class="subtitle">Extract Reddit threads with full comment hierarchy</p>

            <div class="input-group">
                <label for="url">Thread URL</label>
                <input
                    type="text"
                    id="url"
                    placeholder="https://reddit.com/r/subreddit/comments/..."
                    value=""
                />
                <div class="example">
                    Paste any reddit.com or old.reddit.com thread URL
                </div>
            </div>

            <button onclick="scrape()" class="primary">Scrape Thread</button>

            <div id="result" class="result">
                <div class="result-header">
                    <h3>Results</h3>
                    <button class="copy-button" onclick="copyJSON()" id="copyBtn">Copy JSON</button>
                </div>
                <div class="stats" id="stats"></div>
                <pre id="output"></pre>
            </div>

            <div class="footer">
                <a href="/docs" target="_blank">API Documentation</a>
                <a href="/health" target="_blank">Health Check</a>
            </div>
        </div>

        <script>
            async function scrape() {
                const button = document.querySelector('button');
                const resultDiv = document.getElementById('result');
                const outputPre = document.getElementById('output');
                const statsDiv = document.getElementById('stats');
                const urlInput = document.getElementById('url');

                const url = urlInput.value.trim();
                if (!url) {
                    alert('Please enter a Reddit URL');
                    return;
                }

                button.disabled = true;
                button.textContent = 'Scraping...';
                resultDiv.classList.remove('show', 'error');

                try {
                    const response = await fetch('/scrape', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ url })
                    });

                    const data = await response.json();

                    if (response.ok && data.success) {
                        // Show stats
                        const stats = data.stats;
                        statsDiv.innerHTML = `
                            <div class="stat">
                                <div class="stat-value">${stats.total_comments}</div>
                                <div class="stat-label">Total Comments</div>
                            </div>
                            <div class="stat">
                                <div class="stat-value">${stats.top_level_comments}</div>
                                <div class="stat-label">Top-Level</div>
                            </div>
                            <div class="stat">
                                <div class="stat-value">${stats.max_depth}</div>
                                <div class="stat-label">Max Depth</div>
                            </div>
                            <div class="stat">
                                <div class="stat-value">${data.post.score}</div>
                                <div class="stat-label">Post Score</div>
                            </div>
                        `;

                        // Show full JSON
                        const displayData = {
                            success: data.success,
                            url: data.url,
                            post: data.post,
                            comments: data.comments,
                            stats: stats
                        };

                        // Store for copying
                        window.lastScrapedData = displayData;

                        outputPre.textContent = JSON.stringify(displayData, null, 2);
                        resultDiv.classList.add('show');
                    } else {
                        throw new Error(data.detail || 'Scraping failed');
                    }
                } catch (error) {
                    statsDiv.innerHTML = '';
                    outputPre.textContent = `Error: ${error.message}`;
                    resultDiv.classList.add('show', 'error');
                } finally {
                    button.disabled = false;
                    button.textContent = 'Scrape Thread';
                }
            }

            // Copy JSON to clipboard
            async function copyJSON() {
                const copyBtn = document.getElementById('copyBtn');
                const outputPre = document.getElementById('output');

                if (!window.lastScrapedData) {
                    alert('No data to copy. Scrape a thread first!');
                    return;
                }

                try {
                    const jsonText = JSON.stringify(window.lastScrapedData, null, 2);
                    await navigator.clipboard.writeText(jsonText);

                    // Show success feedback
                    const originalText = copyBtn.textContent;
                    copyBtn.textContent = 'Copied';
                    copyBtn.classList.add('copied');

                    setTimeout(() => {
                        copyBtn.textContent = originalText;
                        copyBtn.classList.remove('copied');
                    }, 2000);
                } catch (error) {
                    alert('Failed to copy: ' + error.message);
                }
            }

            // Allow Enter key to submit
            document.getElementById('url').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') scrape();
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        "status": "healthy",
        "service": "Reddit Scraper API",
        "version": "1.0.0",
        "endpoints": {
            "scrape": "POST /scrape",
            "health": "GET /health",
            "docs": "GET /docs"
        }
    })


@app.post("/scrape", response_model=ScrapeResponse)
async def scrape_reddit(request: ScrapeRequest):
    """
    Scrape a Reddit post and return structured data with full comment hierarchy.

    **Automatically converts reddit.com URLs to old.reddit.com**

    Returns:
    - Post metadata (title, author, score, etc.)
    - Complete comment tree with unlimited nesting depth
    - Statistics about the thread

    Example:
    ```json
    {
        "url": "https://reddit.com/r/python/comments/abc123/..."
    }
    ```
    """
    try:
        # Run the scraper as a module to avoid async/sync conflicts
        python_exe = sys.executable

        # Call the scraper module
        result = subprocess.run(
            [python_exe, '-m', 'reddit_scraper.scraper', request.url],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            raise Exception(f"Scraper failed: {result.stderr}")

        # Parse the JSON output
        data = json_module.loads(result.stdout)

        # Calculate statistics
        stats_info = {'max_depth': 0, 'by_depth': {}}
        total_comments = count_comments_recursive(data['comments'], stats=stats_info)

        return ScrapeResponse(
            success=True,
            url=request.url,
            post=data['post'],
            comments=data['comments'],
            stats={
                'total_comments': total_comments,
                'top_level_comments': len(data['comments']),
                'max_depth': stats_info['max_depth'],
                'comments_by_depth': stats_info['by_depth']
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to scrape Reddit post: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    # Run the server
    uvicorn.run(
        "reddit_scraper.server:app",
        host="0.0.0.0",
        port=8001,
        reload=False,
        log_level="info"
    )
