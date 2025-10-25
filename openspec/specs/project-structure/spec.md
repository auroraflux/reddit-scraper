# Project Structure Specification

## Purpose
Defines the standard directory layout and file organization for the reddit-scraper Python package to ensure consistency, discoverability, and maintainability.

## Requirements

### Requirement: Standard Directory Layout
The project SHALL maintain a standard Python package directory structure that separates source code, tests, documentation, and development tooling.

#### Scenario: Developer navigates project structure
- **GIVEN** a new developer clones the repository
- **WHEN** they list the root directory contents
- **THEN** they SHALL see: `reddit_scraper/`, `docs/`, `scripts/`, `tests/`, `openspec/`, `setup.py`, `requirements.txt`, `.gitignore`, `README.md`, `LICENSE`
- **AND** they SHALL understand this is a Reddit scraper package in under 30 seconds
- **AND** the structure SHALL follow standard Python package conventions

#### Scenario: Source code organization
- **GIVEN** the reddit-scraper package
- **WHEN** looking for executable Python code
- **THEN** all package code SHALL be in `reddit_scraper/` directory
- **AND** `reddit_scraper/__init__.py` SHALL define package exports
- **AND** core logic SHALL be in `reddit_scraper/scraper.py`
- **AND** API server SHALL be in `reddit_scraper/server.py`

#### Scenario: Documentation discovery
- **GIVEN** a developer needs documentation
- **WHEN** they navigate the project
- **THEN** `README.md` SHALL provide package overview and quickstart
- **AND** detailed guides SHALL be organized in `docs/` by topic
- **AND** `docs/README.md` SHALL serve as documentation index

### Requirement: Pip-Installable Package Structure
The repository SHALL be structured as a pip-installable Python package with proper metadata and dependencies.

#### Scenario: Package installation
- **GIVEN** the repository is cloned
- **WHEN** running `pip install -e .`
- **THEN** the package SHALL install successfully
- **AND** `reddit-scraper` console script SHALL be available
- **AND** `reddit-scraper-server` console script SHALL be available
- **AND** all dependencies SHALL install automatically

#### Scenario: Package imports
- **GIVEN** the package is installed
- **WHEN** importing in Python: `from reddit_scraper import scrape_reddit_post`
- **THEN** the function SHALL be available
- **AND** imports SHALL work from anywhere in the system
- **AND** version SHALL be accessible via `reddit_scraper.__version__`

#### Scenario: Module execution
- **GIVEN** the package is installed
- **WHEN** running `python -m reddit_scraper.scraper <url>`
- **THEN** the scraper SHALL execute as a module
- **AND** `python -m reddit_scraper.server` SHALL start the API server
- **AND** both SHALL work with proper imports

### Requirement: Script Organization
Utility scripts SHALL be organized in the `scripts/` directory with executable permissions and proper documentation.

#### Scenario: Server startup script
- **GIVEN** the `scripts/start_server.sh` script exists
- **WHEN** a user runs `./scripts/start_server.sh`
- **THEN** it SHALL activate `.venv/` if present
- **AND** it SHALL start the server using `python -m reddit_scraper.server`
- **AND** it SHALL print startup messages to guide the user

#### Scenario: Script discoverability
- **GIVEN** a user needs to run scripts
- **WHEN** they check the `scripts/` directory
- **THEN** all scripts SHALL have descriptive names
- **AND** each script SHALL have a comment header explaining purpose
- **AND** scripts SHALL have executable permissions (`chmod +x`)

### Requirement: Virtual Environment Isolation
The project SHALL use `.venv/` for Python dependency isolation, gitignored to prevent accidental commits.

#### Scenario: Virtual environment setup
- **GIVEN** a new developer clones the repository
- **WHEN** they create a virtual environment: `python -m venv .venv`
- **THEN** dependencies SHALL install into `.venv/`
- **AND** `.venv/` SHALL be gitignored
- **AND** `requirements.txt` SHALL list all runtime dependencies

#### Scenario: Development dependencies
- **GIVEN** a developer wants to run tests
- **WHEN** they install dev dependencies: `pip install -e ".[dev]"`
- **THEN** test frameworks SHALL install (pytest, pytest-cov)
- **AND** all runtime dependencies SHALL also install
- **AND** package SHALL be editable (changes reflected immediately)

### Requirement: Version Control Hygiene
The repository SHALL exclude generated files, dependencies, and secrets from version control.

#### Scenario: Gitignore coverage
- **GIVEN** the `.gitignore` file
- **WHEN** checking what is ignored
- **THEN** it SHALL ignore: `.venv/`, `*.pyc`, `__pycache__/`, `.env`, `*.egg-info/`, `dist/`, `build/`
- **AND** it SHALL NOT ignore: `README.md`, `docs/`, `scripts/`, `openspec/`
- **AND** no dependency directories SHALL be committed

#### Scenario: No debug files committed
- **GIVEN** the repository
- **WHEN** running `git status`
- **THEN** NO `.pyc` files SHALL appear
- **AND** NO `__pycache__/` directories SHALL appear
- **AND** NO test outputs SHALL be committed

### Requirement: Documentation Organization
Documentation SHALL be centralized in `docs/` with clear separation of concerns and a README index.

#### Scenario: Documentation structure
- **GIVEN** the `docs/` directory
- **WHEN** a user explores documentation
- **THEN** they SHALL find: `api-guide.md`, `scraping-guide.md`, `comparison.md`, `guidelines.md`
- **AND** `docs/README.md` SHALL provide an index with descriptions
- **AND** each guide SHALL focus on a single topic

#### Scenario: API documentation
- **GIVEN** a user wants to use the REST API
- **WHEN** they read `docs/api-guide.md`
- **THEN** they SHALL find endpoint documentation
- **AND** they SHALL find request/response examples
- **AND** they SHALL find integration examples (Python, JavaScript, curl)

#### Scenario: Implementation details
- **GIVEN** a developer wants to understand internals
- **WHEN** they read `docs/scraping-guide.md`
- **THEN** they SHALL find implementation details
- **AND** they SHALL find usage patterns
- **AND** they SHALL find troubleshooting tips

### Requirement: OpenSpec Integration
The repository SHALL use OpenSpec for spec-driven development with clear separation of specs and changes.

#### Scenario: OpenSpec structure
- **GIVEN** the `openspec/` directory
- **WHEN** exploring OpenSpec files
- **THEN** they SHALL find: `project.md`, `AGENTS.md`, `specs/`, `changes/`
- **AND** `specs/` SHALL contain current specifications (what IS built)
- **AND** `changes/` SHALL contain proposed changes (what SHOULD change)

#### Scenario: Specification discovery
- **GIVEN** a developer wants to understand requirements
- **WHEN** they run `openspec list --specs`
- **THEN** they SHALL see: `project-structure`, `reddit-scraper`
- **AND** each spec SHALL have `spec.md` with requirements and scenarios

#### Scenario: Change proposals
- **GIVEN** a developer wants to propose a change
- **WHEN** they create a proposal in `changes/<change-id>/`
- **THEN** they SHALL include: `proposal.md`, `tasks.md`, `specs/`
- **AND** `openspec validate <change-id> --strict` SHALL pass before implementation
- **AND** after deployment, changes SHALL be archived to `changes/archive/`

### Requirement: Package Metadata
The repository SHALL provide complete package metadata via `setup.py` for distribution and installation.

#### Scenario: Setup.py completeness
- **GIVEN** the `setup.py` file
- **WHEN** checking metadata
- **THEN** it SHALL define: name, version, description, author, license, python_requires
- **AND** it SHALL list all dependencies in `install_requires`
- **AND** it SHALL define console scripts for `reddit-scraper` and `reddit-scraper-server`
- **AND** it SHALL specify `packages=find_packages()` to discover package

#### Scenario: Dependency declaration
- **GIVEN** the package dependencies
- **WHEN** reviewing `requirements.txt` and `setup.py`
- **THEN** both SHALL list the same runtime dependencies
- **AND** `setup.py` SHALL include version constraints (>=X.Y.Z)
- **AND** development dependencies SHALL be in `extras_require["dev"]`

### Requirement: Licensing and Attribution
The repository SHALL include clear license and attribution information.

#### Scenario: License file
- **GIVEN** the repository root
- **WHEN** checking for license
- **THEN** `LICENSE` file SHALL exist
- **AND** it SHALL contain full MIT License text
- **AND** README SHALL reference the license

#### Scenario: Package attribution
- **GIVEN** the package metadata
- **WHEN** checking `setup.py` and `__init__.py`
- **THEN** `__author__` SHALL be defined
- **AND** `__version__` SHALL match `setup.py` version
- **AND** README SHALL include acknowledgments section
