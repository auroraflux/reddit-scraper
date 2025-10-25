# reddit-scraper Documentation

Complete documentation for the reddit-scraper package.

## Quick Links

- **[Main README](../README.md)** - Package overview and quick start
- **[API Guide](./api-guide.md)** - REST API server documentation
- **[Scraping Guide](./scraping-guide.md)** - Implementation details and usage patterns
- **[Comparison](./comparison.md)** - reddit-scraper vs other scraping approaches
- **[Code Guidelines](./guidelines.md)** - Code quality standards and conventions

## Documentation Structure

### For Users

**Getting Started:**
1. Read the [Main README](../README.md) for installation and quick start
2. Choose your usage mode:
   - REST API: See [API Guide](./api-guide.md)
   - CLI: See main README CLI section
   - Python module: See main README Python section

**Integration Examples:**
- Python requests: [API Guide - Python Examples](./api-guide.md#python)
- JavaScript/Node.js: [API Guide - JavaScript Examples](./api-guide.md#javascript-nodejs)
- Shell scripts: [Scraping Guide - Shell Scripts](./scraping-guide.md#shell-script)
- LLM integration: [Scraping Guide - Integration with LLMs](./scraping-guide.md#integration-with-llms)

**Troubleshooting:**
- See [Scraping Guide - Troubleshooting](./scraping-guide.md#troubleshooting)

### For Developers

**Code Quality:**
- Follow [Code Guidelines](./guidelines.md) strictly
- Maximum 20 lines per function (Section III)
- Type hints required (Section VI)
- Comprehensive docstrings (Section VII)

**Architecture:**
- Package structure: [Scraping Guide - Architecture](./scraping-guide.md#architecture)
- Reddit JSON API: See [Scraping Guide](./scraping-guide.md)
- OpenSpec workflow: See `../openspec/AGENTS.md`

**Contributing:**
1. Read [Code Guidelines](./guidelines.md)
2. Create OpenSpec proposal for significant changes
3. Follow the proposal → implementation → archive workflow
4. Validate with `openspec validate --strict`

## File Descriptions

### [api-guide.md](./api-guide.md)
**Purpose:** REST API server documentation and integration examples

**Contains:**
- API endpoint documentation (`POST /scrape`, `GET /health`, `GET /`)
- Request/response schemas
- Integration examples (Python, JavaScript, curl, shell)
- Error handling
- Server configuration

**Target Audience:** Users integrating reddit-scraper into applications

### [scraping-guide.md](./scraping-guide.md)
**Purpose:** Implementation details and advanced usage patterns

**Contains:**
- Quick start instructions
- API endpoint details
- Usage examples in multiple languages
- LLM integration patterns (Claude, ChatGPT)
- Batch processing
- Comment analysis
- Troubleshooting
- Configuration options

**Target Audience:** Users and developers needing detailed implementation knowledge

### [comparison.md](./comparison.md)
**Purpose:** Comparison of reddit-scraper vs alternative approaches

**Contains:**
- JSON API scraping (this tool)
- LLM-based web scraping
- Browser automation
- When to use each approach

**Target Audience:** Users choosing between scraping tools

### [guidelines.md](./guidelines.md)
**Purpose:** Code quality standards and development conventions

**Contains:**
- Function size limits (20 lines max)
- Naming conventions
- Documentation requirements
- Error handling patterns
- Directory structure rules
- Testing standards

**Target Audience:** Contributors and developers

## OpenSpec Documentation

OpenSpec files are in `../openspec/`:

- **[project.md](../openspec/project.md)** - Project overview, tech stack, conventions
- **[AGENTS.md](../openspec/AGENTS.md)** - OpenSpec workflow for AI assistants
- **[specs/](../openspec/specs/)** - Current specifications
  - `project-structure/spec.md` - Directory layout requirements
  - `reddit-scraper/spec.md` - Core scraping requirements

## Additional Resources

### External Links

- **GitHub Repository**: [https://github.com/YOUR_USERNAME/reddit-scraper](https://github.com/YOUR_USERNAME/reddit-scraper)
- **PyPI Package** (when published): `pip install reddit-scraper`
- **Related Project**: [crawlai-integration](https://github.com/YOUR_USERNAME/crawlai-integration) - General web scraping with LLM support

### Community

- **Issues**: Report bugs or request features on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Contributing**: See CONTRIBUTING.md (if it exists) or Code Guidelines

## Documentation Maintenance

When adding new documentation:

1. Add file to `docs/` directory
2. Update this README with link and description
3. Update main README if it affects quick start
4. Run `openspec validate --strict` if changing specs

When updating existing docs:

1. Keep examples up-to-date with code
2. Update version references
3. Test all code examples
4. Update "Last Updated" date in relevant files

---

**Last Updated**: 2025-10-25
**Version**: 1.0.0
