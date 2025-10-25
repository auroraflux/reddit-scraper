# reddit-scraper Specification

## Purpose
Provides deterministic Reddit thread scraping using Reddit's public JSON API, including full comment hierarchy extraction, FastAPI REST server, and statistics calculation. This is the core capability of the reddit-scraper package.

## Requirements

### Requirement: Reddit JSON API Scraping
The system SHALL scrape Reddit posts and comments using the public JSON API without LLM assistance or API authentication.

#### Scenario: Scrape thread with comments
- **GIVEN** a valid Reddit post URL
- **WHEN** calling `scrape_reddit_post(url)`
- **THEN** the system SHALL return post metadata (title, author, score, timestamp)
- **AND** it SHALL return all visible comments in hierarchical structure
- **AND** it SHALL preserve comment nesting depth (unlimited levels)
- **AND** it SHALL complete in 5-10 seconds

#### Scenario: Handle old.reddit.com conversion
- **GIVEN** a www.reddit.com or reddit.com URL
- **WHEN** validating the URL
- **THEN** the system SHALL automatically convert to old.reddit.com
- **AND** it SHALL append `.json?limit=500` for API access
- **AND** it SHALL use the converted URL for fetching

#### Scenario: Parse nested comment hierarchy
- **GIVEN** a Reddit post with 5+ nesting levels
- **WHEN** parsing comments
- **THEN** the system SHALL recursively extract all reply levels
- **AND** each comment SHALL include: id, author, score, text, timestamp, replies array
- **AND** it SHALL preserve parent-child relationships exactly as shown on Reddit

### Requirement: FastAPI REST Server
The system SHALL provide a REST API server for scraping Reddit threads on demand.

#### Scenario: Health check endpoint
- **GIVEN** the API server is running
- **WHEN** sending `GET /health`
- **THEN** it SHALL return HTTP 200
- **AND** response SHALL include service status and version
- **AND** it SHALL respond in under 100ms

#### Scenario: Scrape endpoint with validation
- **GIVEN** the API server is running
- **WHEN** sending `POST /scrape` with `{"url": "https://reddit.com/r/python/comments/123/test"}`
- **THEN** it SHALL validate the URL is a Reddit post
- **AND** it SHALL automatically convert to old.reddit.com
- **AND** it SHALL return structured JSON with post, comments, and statistics
- **AND** it SHALL return HTTP 500 with error details if scraping fails

#### Scenario: Web interface for testing
- **GIVEN** the API server is running
- **WHEN** navigating to `GET /` in a browser
- **THEN** it SHALL serve an HTML interface
- **AND** the interface SHALL have URL input field and scrape button
- **AND** it SHALL display results with statistics and JSON output
- **AND** it SHALL provide a "Copy JSON" button for extracted data

### Requirement: Comment Statistics Calculation
The system SHALL calculate and return statistics about scraped threads.

#### Scenario: Calculate comment counts
- **GIVEN** a scraped Reddit thread
- **WHEN** processing comments
- **THEN** it SHALL count total comments recursively
- **AND** it SHALL count top-level comments separately
- **AND** it SHALL calculate maximum nesting depth
- **AND** it SHALL provide comment counts by depth level

#### Scenario: Statistics in API response
- **GIVEN** a successful scrape
- **WHEN** returning results
- **THEN** the response SHALL include `stats` object with:
  - `total_comments`: count of all comments
  - `top_level_comments`: count of root-level comments
  - `max_depth`: deepest nesting level
  - `comments_by_depth`: histogram of comments per level

### Requirement: Error Handling and Validation
The system SHALL validate inputs and provide clear error messages for failures.

#### Scenario: Invalid URL rejection
- **GIVEN** an invalid Reddit URL
- **WHEN** calling the scrape endpoint
- **THEN** it SHALL return HTTP 400 with validation error
- **AND** error message SHALL explain expected format
- **AND** it SHALL not attempt to fetch invalid URLs

#### Scenario: Network failure handling
- **GIVEN** Reddit is unreachable or returns an error
- **WHEN** attempting to scrape
- **THEN** it SHALL return HTTP 500 with descriptive error
- **AND** error SHALL include what failed, why, and context
- **AND** it SHALL log errors to stderr for debugging

#### Scenario: Deleted content handling
- **GIVEN** a Reddit post with deleted comments
- **WHEN** parsing the JSON
- **THEN** deleted authors SHALL appear as "[deleted]"
- **AND** removed content SHALL appear as "[removed]" or empty text
- **AND** deleted comments SHALL still appear in hierarchy if replies exist

### Requirement: Server Lifecycle Management
The system SHALL provide clean startup and shutdown for the API server.

#### Scenario: Server startup
- **GIVEN** the package is installed
- **WHEN** running `python -m reddit_scraper.server`
- **THEN** the server SHALL start on port 8001
- **AND** it SHALL print startup message with URLs (server, docs, playground)
- **AND** it SHALL bind to 0.0.0.0 (all interfaces)

#### Scenario: Graceful shutdown
- **GIVEN** the server is running
- **WHEN** receiving SIGINT (Ctrl+C)
- **THEN** it SHALL print shutdown message
- **AND** it SHALL complete in-flight requests before exiting
- **AND** it SHALL clean up resources properly

### Requirement: Standalone Scraper Execution
The system SHALL support direct command-line execution of the scraper without the API server.

#### Scenario: CLI invocation via module
- **GIVEN** the package is installed
- **WHEN** running `python -m reddit_scraper.scraper <url>`
- **THEN** it SHALL scrape the URL and output JSON to stdout
- **AND** it SHALL print progress messages to stderr
- **AND** it SHALL exit with code 0 on success, non-zero on failure

#### Scenario: CLI invocation via console script
- **GIVEN** the package is installed
- **WHEN** running `reddit-scraper <url>` from anywhere
- **THEN** it SHALL execute the scraper
- **AND** it SHALL produce identical output to module execution
- **AND** it SHALL work from any directory

#### Scenario: Subprocess compatibility
- **GIVEN** the API server needs to scrape a URL
- **WHEN** it calls the scraper via subprocess: `python -m reddit_scraper.scraper <url>`
- **THEN** the scraper SHALL execute successfully
- **AND** it SHALL return valid JSON on stdout
- **AND** stderr SHALL contain progress logs only

### Requirement: Package Import API
The system SHALL provide a clean Python API for programmatic usage.

#### Scenario: Import and use scraper function
- **GIVEN** the package is installed
- **WHEN** importing: `from reddit_scraper import scrape_reddit_post`
- **THEN** the function SHALL be available
- **AND** calling `scrape_reddit_post(url)` SHALL return parsed data
- **AND** it SHALL raise exceptions on errors (not return error dicts)

#### Scenario: Version access
- **GIVEN** the package is installed
- **WHEN** importing: `import reddit_scraper`
- **THEN** `reddit_scraper.__version__` SHALL return version string (e.g., "1.0.0")
- **AND** version SHALL match `setup.py` version
- **AND** version SHALL follow semantic versioning (MAJOR.MINOR.PATCH)
