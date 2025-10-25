#!/usr/bin/env python3
"""
Reddit Comment Scraper with Hierarchy Preservation
Uses Reddit JSON API - No LLM costs, gets 100% of comments!

Usage:
    python -m reddit_scraper.scraper <reddit_url>
"""

import json
import sys
import requests
from typing import Dict, List, Optional


def scrape_reddit_post(url: str) -> Dict:
    """
    Scrape a Reddit post using the JSON API and preserve full comment hierarchy.

    Args:
        url: Reddit post URL (reddit.com or old.reddit.com)

    Returns:
        Dict containing post data and hierarchical comments
    """
    # Convert to old.reddit.com if needed
    if 'reddit.com' in url:
        url = url.replace('www.reddit.com', 'old.reddit.com')
        if 'old.reddit.com' not in url:
            url = url.replace('reddit.com', 'old.reddit.com')

    # Add .json to get the JSON API
    json_url = url.rstrip('/') + '.json?limit=500'

    print(f"🌐 Fetching from JSON API: {json_url}", file=sys.stderr)

    # Fetch the JSON data
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditScraper/1.0)'}
    response = requests.get(json_url, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Reddit JSON API returns [post_listing, comments_listing]
    post_data_raw = data[0]['data']['children'][0]['data']
    comments_data_raw = data[1]['data']['children']

    print("📄 Parsing post and comments...", file=sys.stderr)

    # Extract post metadata
    post_data = {
        'title': post_data_raw.get('title', 'Unknown'),
        'author': post_data_raw.get('author', 'Unknown'),
        'subreddit': post_data_raw.get('subreddit', 'Unknown'),
        'timestamp': post_data_raw.get('created_utc', 0),
        'score': post_data_raw.get('score', 0),
        'url': url,
        'num_comments': post_data_raw.get('num_comments', 0),
        'selftext': post_data_raw.get('selftext', '')
    }

    # Parse comments recursively
    def parse_comment(comment_obj: Dict) -> Optional[Dict]:
        """Recursively parse a comment and its replies"""
        if comment_obj['kind'] != 't1':  # Not a comment (might be 'more')
            return None

        comment_data = comment_obj['data']

        # Build the comment object
        comment = {
            'id': comment_data.get('id', ''),
            'author': comment_data.get('author', '[deleted]'),
            'timestamp': comment_data.get('created_utc', 0),
            'score': comment_data.get('score', 0),
            'text': comment_data.get('body', ''),
            'replies': []
        }

        # Add flair if present
        if comment_data.get('author_flair_text'):
            comment['author'] = f"{comment['author']} ({comment_data['author_flair_text']})"

        # Parse replies recursively
        if 'replies' in comment_data and comment_data['replies']:
            if isinstance(comment_data['replies'], dict):
                reply_children = comment_data['replies'].get('data', {}).get('children', [])
                for reply_obj in reply_children:
                    reply = parse_comment(reply_obj)
                    if reply:
                        comment['replies'].append(reply)

        return comment

    # Parse all top-level comments
    comments_list = []
    for comment_obj in comments_data_raw:
        comment = parse_comment(comment_obj)
        if comment:
            comments_list.append(comment)

    # Count total comments (including replies)
    def count_all(comments):
        total = len(comments)
        for comment in comments:
            total += count_all(comment.get('replies', []))
        return total

    total_comments = count_all(comments_list)
    print(f"✅ Extracted {total_comments} total comments (including replies)", file=sys.stderr)
    print(f"📊 Post says {post_data['num_comments']} comments total", file=sys.stderr)

    return {
        'post': post_data,
        'comments': comments_list
    }


def print_comment_tree(comments: List[Dict], indent: int = 0):
    """Pretty print the comment tree"""
    for comment in comments:
        prefix = "  " * indent + "└─ " if indent > 0 else "• "
        print(f"{prefix}{comment['author']} ({comment['score']} points)", file=sys.stderr)

        if comment.get('replies'):
            print_comment_tree(comment['replies'], indent + 1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python -m reddit_scraper.scraper <reddit_url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    try:
        result = scrape_reddit_post(url)

        # Output the JSON to stdout (for API consumption)
        print(json.dumps(result, indent=2))

        # Pretty print to stderr (for human readability)
        print("\n" + "="*80, file=sys.stderr)
        print("📝 POST SUMMARY", file=sys.stderr)
        print("="*80, file=sys.stderr)
        print(f"Title: {result['post']['title']}", file=sys.stderr)
        print(f"Author: {result['post']['author']}", file=sys.stderr)
        print(f"Subreddit: r/{result['post']['subreddit']}", file=sys.stderr)
        print(f"Score: {result['post']['score']}", file=sys.stderr)
        print(f"Comments: {result['post']['num_comments']}", file=sys.stderr)

        print("\n💬 COMMENT TREE", file=sys.stderr)
        print("="*80, file=sys.stderr)
        print_comment_tree(result['comments'])

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
