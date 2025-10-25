#!/bin/bash
# Start Reddit Scraper API Server

# Change to project root (script is in scripts/ subdirectory)
cd "$(dirname "$0")/.."

echo "🚀 Starting Reddit Scraper API..."
echo ""

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Start the server
python -m reddit_scraper.server
