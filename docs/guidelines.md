
## PRIMARY DIRECTIVE

You are to generate code that represents the pinnacle of software craftsmanship: simple, elegant, maintainable, and robust. Every single line must be defensible in a code review by the most demanding senior architect. You operate under a zero-tolerance policy for technical debt, code smells, and lazy implementations. Your code must be production-ready, not proof-of-concept quality.

---

### I. Core Principles: Non-Negotiable Standards

1. **KISS (Keep It Simple, Stupid) - Enforced Standards:**
   * **Cyclomatic Complexity:** No function may exceed a complexity of 5. If it does, refactor immediately.
   * **Nesting Depth:** Maximum nesting level is 3. Deeper nesting indicates a design failure.
   * **Line Length:** Hard limit of 80 characters (120 absolute maximum with justification).
   * **File Length:** No file should exceed 300 lines. If it does, it's doing too much.
   * **Class Responsibilities:** A class should have 5 or fewer public methods. More indicates violation of SRP.

2. **DRY (Don't Repeat Yourself) - Zero Tolerance:**
   * **Rule of Three:** If code appears twice, note it. If it appears three times, refactor it immediately.
   * **Magic Numbers:** Every number except 0, 1, and -1 must be a named constant.
   * **String Literals:** Any string used more than once must be a constant.
   * **Similar Functions:** Functions with >30% similar code must share a common abstraction.
   * **Copy-Paste Detection:** If you copy-paste more than 3 lines, you're doing it wrong.

3. **YAGNI (You Ain't Gonna Need It) - Strict Enforcement:**
   * **No Speculative Generality:** Zero unused parameters, methods, or classes.
   * **No "Just In Case" Code:** Every line must serve the current requirement.
   * **No Commented-Out Code:** Delete it. Version control exists for a reason.
   * **No Dead Code Paths:** Every branch must be reachable and testable.

4. **SOLID Principles - Mandatory Compliance:**
   * **Single Responsibility:** One reason to change per class/function. Period.
   * **Open/Closed:** Extending behavior requires zero modification to existing code.
   * **Liskov Substitution:** Subclasses must be perfectly substitutable for their base classes.
   * **Interface Segregation:** No client should depend on methods it doesn't use.
   * **Dependency Inversion:** Depend on abstractions, never on concretions.

---

### II. Code Quality Standards: Measurable Requirements

1. **Naming Convention Enforcement:**
   ```
   Variables:
   - Booleans: is/has/can/should/will prefix (isValid, hasAccess, canEdit)
   - Collections: Plural nouns (users, items, orderLines)
   - Counts: suffix with Count (userCount, retryCount)
   - Indices: prefix with idx or suffix with Index (idxCurrent, startIndex)
   - Temporary: prefix with temp only if lifetime < 5 lines
   
   Functions:
   - Commands: Verb (calculateTotal, validateInput, sendEmail)
   - Queries: Verb + Noun (getUserById, findActiveOrders)
   - Predicates: is/has/can prefix returning boolean (isValid, hasPermission)
   - Factories: create/build/make prefix (createUser, buildQuery)
   - Converters: to/from/as prefix (toString, fromJson, asInteger)
   ```

2. **Function Constraints:**
   * **Line Limit:** 20 lines maximum, 10 lines preferred
   * **Parameter Limit:** 3 parameters maximum (use parameter objects beyond that)
   * **Return Points:** Single return preferred, 3 maximum with guard clauses
   * **Cognitive Complexity:** Should be understandable in 30 seconds
   * **Dependencies:** Maximum 3 external dependencies per function

3. **Error Handling Mandates:**
   * **No Silent Failures:** Every error must be explicitly handled or propagated
   * **Fail Fast:** Validate inputs at function boundaries immediately
   * **Specific Exceptions:** Never catch generic Exception/Error without re-throwing
   * **Error Messages:** Must include: what failed, why it failed, how to fix it
   * **Null Handling:** Explicitly handle null/undefined. Use Optional/Maybe patterns where applicable

4. **Documentation Requirements:**
   ```
   /**
    * Function documentation template (mandatory for all public methods):
    * 
    * @description Clear, one-line description of what the function does
    * @param {Type} paramName - What this parameter represents and valid ranges/values
    * @returns {Type} Description of return value and possible states
    * @throws {ErrorType} When this error occurs and why
    * @example
    * // Concrete usage example with expected output
    * const result = functionName(validInput);
    * console.log(result); // Expected output
    * 
    * @complexity O(n) - Time and space complexity when non-trivial
    * @pure true/false - Whether function has side effects
    */
   ```

---

### III. Architectural Mandates: Design Patterns & Structure

1. **Layered Architecture Requirements:**
   ```
   Presentation Layer → Business Logic Layer → Data Access Layer
   
   Rules:
   - Each layer only knows about the layer directly below it
   - No cross-layer dependencies
   - DTOs for layer communication, never raw domain objects
   - Each layer has its own error types
   ```

2. **Module Design Specifications:**
   * **Public API Surface:** Maximum 5 public functions/methods per module
   * **Module Size:** 100-200 lines optimal, 300 absolute maximum
   * **Internal Complexity:** Hide all complexity behind a simple interface
   * **Dependency Direction:** Dependencies flow inward (Clean Architecture)
   * **Circular Dependencies:** Absolutely forbidden. Immediate refactor required.

3. **Data Structure Selection Matrix:**
   ```
   Use Array when: Order matters, need index access, size < 10,000
   Use Set when: Uniqueness matters, frequent lookups, no order requirement
   Use Map when: Key-value pairs with non-string keys, frequent updates
   Use Object when: Static structure, string keys, configuration data
   Use Queue when: FIFO processing, task scheduling
   Use Stack when: LIFO processing, recursion unwinding
   ```

4. **Pattern Usage Guidelines:**
   * **Factory Pattern:** When object creation logic is complex (>3 parameters)
   * **Repository Pattern:** All data access must go through repositories
   * **Strategy Pattern:** When you have 3+ similar algorithms
   * **Observer Pattern:** For decoupled event handling
   * **Builder Pattern:** For objects with >5 optional parameters

---

### IV. Performance & Optimization: Mandatory Considerations

1. **Algorithm Complexity Requirements:**
   * Document O(n²) or worse algorithms with justification
   * Prefer O(n log n) over O(n²) even for small datasets
   * Use appropriate data structures (hash maps for lookups, not arrays)
   * Lazy evaluation for expensive computations
   * Memoization for pure functions with repeated calls

2. **Memory Management:**
   * **No Memory Leaks:** Clear all event listeners, intervals, and subscriptions
   * **Bounded Collections:** All collections must have a maximum size
   * **Resource Cleanup:** Use finally blocks or equivalent for resource disposal
   * **Circular Reference Prevention:** Weak references where appropriate

3. **Database Interaction Rules:**
   * **N+1 Query Prevention:** Use eager loading or batch fetching
   * **Connection Pooling:** Never create connections per request
   * **Prepared Statements:** Always use parameterized queries
   * **Transaction Boundaries:** Explicit transaction management for multi-step operations
   * **Index Awareness:** Comment queries that would benefit from indexing

---

### V. Security Requirements: Zero-Compromise Standards

1. **Input Validation:**
   * Whitelist validation only (never blacklist)
   * Validate type, format, length, and range
   * Sanitize all user input before processing
   * Escape output based on context (HTML, SQL, shell, etc.)

2. **Authentication & Authorization:**
   * Never store passwords in plain text
   * Use established libraries for crypto (never roll your own)
   * Principle of least privilege for all operations
   * Time-constant comparison for secrets

3. **Secure Defaults:**
   * Fail closed (deny by default)
   * No sensitive data in logs
   * No credentials in code (use environment variables)
   * HTTPS/TLS for all network communication

---

### VI. Testing Requirements: Non-Optional

1. **Test Coverage Mandates:**
   * **Unit Tests:** Every public method must have tests
   * **Edge Cases:** Explicitly test boundaries, nulls, and empty collections
   * **Error Paths:** Every error condition must be tested
   * **Test Naming:** `test_MethodName_StateUnderTest_ExpectedBehavior()`

2. **Test Quality Standards:**
   * **Arrange-Act-Assert:** Every test follows this pattern
   * **Single Assertion:** One logical assertion per test
   * **No Test Interdependence:** Tests must run in any order
   * **Fast Tests:** Unit tests must complete in <100ms

---

### VII. Code Review Checklist: Mandatory Self-Review

Before considering code complete, verify:

```
□ Functions under 20 lines
□ Cyclomatic complexity ≤ 5
□ No duplicated code blocks
□ All magic numbers extracted to constants
□ Descriptive names for everything
□ Error handling at all boundaries
□ No commented-out code
□ No console.log/print statements (use proper logging)
□ All TODOs addressed or ticketed
□ Security considerations addressed
□ Performance implications documented
□ Tests written and passing
□ Documentation complete
□ No linting warnings
□ Dependencies justified
```

---

### VIII. Anti-Patterns: Absolutely Forbidden

1. **God Objects:** Classes that do everything
2. **Spaghetti Code:** Tangled control flow
3. **Copy-Paste Programming:** Duplicated code blocks
4. **Magic Numbers/Strings:** Unexplained literals
5. **Long Parameter Lists:** More than 3 parameters
6. **Feature Envy:** Methods that use another class more than their own
7. **Inappropriate Intimacy:** Classes that know too much about each other
8. **Primitive Obsession:** Using primitives instead of objects for domain concepts
9. **Shotgun Surgery:** Changes require edits in multiple places
10. **Speculative Generality:** "We might need this someday" code

---

### IX. Commit & Version Control Standards

1. **Commit Message Format:**
   ```
   type(scope): subject (max 50 chars)
   
   Body: What and why (not how) - wrap at 72 chars
   
   Types: feat|fix|docs|style|refactor|test|chore
   ```

2. **Commit Hygiene:**
   * One logical change per commit
   * No mixing refactoring with features
   * All commits must pass tests
   * No merge commits in feature branches (rebase instead)

---

### X. Final Verification Protocol

Every piece of code must pass this interrogation:

1. **Can a junior developer understand this in 2 minutes?**
2. **Can this be tested in isolation?**
3. **Will this scale to 10x the current load?**
4. **Is this the simplest solution that works?**
5. **Would I be proud to show this in a job interview?**

If any answer is "no", the code is not ready.

---

## ENFORCEMENT

Failure to comply with these standards is not a matter of preference or style. It's a matter of professional competence. Code that violates these principles is broken code, regardless of whether it "works." The standard is perfection; we accept excellence as a compromise.


Let me examine that directory to understand the organizational challenges you're dealing with, then create a comprehensive addendum.Looking at that crawlAI directory, I can see exactly the kind of chaos you're dealing with. That's a perfect example of project drift - started as one thing, morphed into something else, and now you've got a virtual environment sitting next to debug files, multiple versions of test outputs, and documentation scattered everywhere. Let me create an addendum that addresses this mess.


### XI. Directory Structure: Zero-Tolerance Organization
Your filesystem is your codebase's first impression. A messy directory structure indicates messy thinking. Period.

1. **Project Root Hygiene:**
   ```
   project-root/
   ├── src/               # ALL source code goes here
   ├── tests/             # ALL tests go here  
   ├── docs/              # ALL documentation goes here
   ├── scripts/           # Build/deploy/utility scripts
   ├── data/              # Data files (gitignored)
   ├── outputs/           # Generated outputs (gitignored)
   ├── .archive/          # Old code quarantine (gitignored)
   ├── README.md          # Single source of truth
   ├── requirements.txt   # Dependencies
   └── .gitignore         # Properly configured
   ```

2. **Forbidden at Root Level:**
   * Test files (test_*.py, *.test.js)
   * Debug outputs (debug_*.*, *.debug)
   * Multiple versions of the same file
   * Virtual environments (venv/, reddit-scraper/)
   * Cache directories (__pycache__/, .cache/)
   * Build artifacts (*.pyc, *.o, dist/)
   * Data dumps (*.json, *.csv) unless config files
   * Multiple README variants

---

### XII. File Naming: Semantic Clarity

1. **Version Control is NOT in Filenames:**
   ```
   FORBIDDEN:
   test_gemini.json
   test_gemini_fixed.json
   test_gemini_final.json
   test_gemini_final_FINAL.json
   test_gemini_working.json
   
   REQUIRED:
   Use Git. One filename. Period.
   ```

2. **Naming Hierarchy:**
   ```
   domain_function_variant.extension
   
   Examples:
   reddit_scraper_async.py    ✓
   reddit_api_client.py        ✓
   test_reddit_scraper.py      ✓
   
   NOT:
   reddit_scraper.py AND reddit_api.py AND reddit_clean.py
   ```

3. **Output File Rules:**
   * Timestamps in ISO format: `output_2024-01-15T14-30-00.json`
   * Environment prefixes: `dev_output.json`, `prod_output.json`
   * Never "final", "latest", "new", "old" in filenames

---

### XIII. Project Evolution Management

1. **When Projects Drift (like crawlAI → Reddit scraper):**

   **Immediate Actions:**
   ```bash
   # 1. Create new clean structure
   mkdir reddit-scraper-clean
   cd reddit-scraper-clean
   
   # 2. Initialize properly from the start
   mkdir -p src/{core,utils,models} tests docs data outputs
   
   # 3. Cherry-pick ONLY active code
   cp ../crawlAI/reddit_scraper.py src/core/scraper.py
   cp ../crawlAI/reddit_api.py src/core/api.py
   
   # 4. Archive the old mess
   mv ../crawlAI ../.archived_crawlAI_$(date +%Y%m%d)
   ```

2. **The Extraction Protocol:**
   
   When extracting functionality from a larger project:
   ```
   Phase 1: Identify Core
   - List files actually being used (git log --follow)
   - Identify entry points
   - Map dependencies
   
   Phase 2: Isolate
   - Create new repository
   - Copy ONLY required files
   - Rewrite imports
   
   Phase 3: Cleanup
   - Remove all debug code
   - Consolidate similar files
   - Unify naming conventions
   
   Phase 4: Document
   - Write fresh README
   - Document the extraction
   - Archive the original
   ```

---

### XIV. Debug & Temporary File Management

1. **Debug Files Policy:**
   ```python
   # FORBIDDEN: Permanent debug files
   with open('debug_output.html', 'w') as f:  # ❌
       f.write(debug_content)
   
   # REQUIRED: Timestamped, isolated debug files
   from pathlib import Path
   import datetime
   
   debug_dir = Path('outputs/debug')
   debug_dir.mkdir(parents=True, exist_ok=True)
   
   timestamp = datetime.datetime.now().isoformat()
   debug_file = debug_dir / f'debug_{timestamp}.html'
   
   # Auto-cleanup old debug files
   for old_debug in debug_dir.glob('debug_*.html'):
       if (datetime.datetime.now() - datetime.datetime.fromtimestamp(
           old_debug.stat().st_mtime)).days > 7:
           old_debug.unlink()
   ```

2. **Temporary File Rules:**
   * Use proper temp directories (`tempfile.mkdtemp()`)
   * Never create temp files in project root
   * Always use context managers for cleanup
   * Prefix with `.` and add to .gitignore

---

### XV. Multi-Purpose Project Splitting

1. **Split Trigger Conditions:**
   * Different deployment targets
   * Conflicting dependencies  
   * Separate versioning needs
   * Different team ownership
   * Divergent functionality (>30% unshared code)

2. **The Split Procedure:**
   ```
   Original: crawlAI/
   ├── crawl_engine.py
   ├── reddit_scraper.py    # <-- Divergent functionality
   ├── reddit_api.py        # <-- Divergent functionality  
   └── shared_utils.py      # <-- Shared code
   
   Result:
   crawl-core/
   ├── src/
   │   ├── engine.py
   │   └── utils.py
   
   reddit-tools/
   ├── src/
   │   ├── scraper.py
   │   ├── api.py
   │   └── utils.py      # <-- Copied, not shared
   
   # Shared code becomes a package if >3 projects need it
   common-utils/
   ├── src/
   │   └── utils.py
   ├── setup.py
   ```

---

### XVI. Documentation Consolidation

1. **README Proliferation Prevention:**
   ```
   FORBIDDEN:
   README.md
   README_REDDIT_API.md
   REDDIT_API_GUIDE.md
   REDDIT_COMPARISON.md
   REDDIT_SCRAPING_GUIDE.md
   QUICKSTART.md
   
   REQUIRED:
   README.md               # Overview + quickstart
   docs/
   ├── api-guide.md       # Detailed API documentation
   ├── scraping-guide.md  # Implementation details
   └── comparison.md      # Architecture decisions
   ```

2. **Documentation Hierarchy:**
   * README.md: What, why, and quick how
   * docs/: Deep how and why
   * Code comments: Implementation why
   * Never duplicate between levels

---

### XVII. Virtual Environment Discipline

1. **Environment Isolation:**
   ```bash
   # FORBIDDEN: venv in project directory
   python -m venv reddit-scraper  # ❌
   
   # REQUIRED: Consistent, gitignored location
   python -m venv .venv           # ✓
   echo ".venv/" >> .gitignore
   
   # OR: System-wide environments
   python -m venv ~/.venvs/reddit-scraper
   ```

2. **Requirements Management:**
   ```bash
   # Development captures
   pip freeze > requirements.txt           # ❌ Captures everything
   
   # Production requirements
   pip-compile requirements.in              # ✓ Explicit dependencies
   pip-compile dev-requirements.in         # ✓ Dev-only deps separate
   ```

---

### XVIII. The Cleanup Checklist

When inheriting or discovering a messy project:

```bash
#!/bin/bash
# cleanup-assessment.sh

echo "=== Project Cleanup Assessment ==="

# 1. Find all unique file types
echo "File types present:"
find . -type f -name '*.*' | sed 's/.*\.//' | sort -u

# 2. Find duplicate-looking files
echo "Potential duplicates:"
find . -type f -name '*.py' | xargs -I {} basename {} | sort | uniq -d

# 3. Find debug/test artifacts
echo "Debug/test files:"
find . -type f \( -name '*debug*' -o -name '*test*' -o -name '*tmp*' \)

# 4. Check for multiple versions
echo "Versioned files:"
find . -type f -name '*final*' -o -name '*_v[0-9]*' -o -name '*_old*'

# 5. Find large files that shouldn't be committed
echo "Large files (>1MB):"
find . -type f -size +1M -exec ls -lh {} \;

# 6. Identify active vs dead code
echo "Recently modified files (active):"
find . -type f -name '*.py' -mtime -30

echo "Stale files (>90 days):"
find . -type f -name '*.py' -mtime +90
```

---

### XIX. Migration Path for Chaotic Projects

1. **The Quarantine Method:**
   ```python
   """
   For projects too messy to refactor immediately
   """
   
   import shutil
   from pathlib import Path
   from datetime import datetime
   
   def quarantine_chaos():
       # Create structure
       Path("src/legacy").mkdir(parents=True, exist_ok=True)
       Path("src/clean").mkdir(parents=True, exist_ok=True)
       
       # Move everything to legacy
       chaos_files = ["reddit_scraper.py", "reddit_api.py", 
                      "test_gemini.py", "debug_reddit.py"]
       
       for chaos in chaos_files:
           if Path(chaos).exists():
               shutil.move(chaos, f"src/legacy/{chaos}")
       
       # Create clean entry point
       with open("src/clean/main.py", "w") as f:
           f.write("""
   '''Clean entry point - gradually migrate from legacy'''
   import sys
   sys.path.insert(0, 'src/legacy')
   
   # Gradually move cleaned code here
   from reddit_scraper import main as legacy_main
   
   def main():
       # Wrapper with proper error handling
       try:
           legacy_main()
       except Exception as e:
           logging.error(f"Legacy code failed: {e}")
           raise
   
   if __name__ == "__main__":
       main()
   """)
   ```

2. **Incremental Cleanup Strategy:**
   * Week 1: Structure and move files
   * Week 2: Consolidate duplicate functionality
   * Week 3: Extract shared utilities
   * Week 4: Unify naming conventions
   * Week 5: Remove dead code
   * Week 6: Document the clean structure

---

### XX. Enforcement & Prevention

1. **Pre-commit Hooks:**
   ```yaml
   # .pre-commit-config.yaml
   repos:
     - repo: local
       hooks:
         - id: no-debug-files
           name: Block debug files
           entry: 'debug_|test_output|_final\.|_fixed\.'
           language: pygrep
           types: [file]
           exclude: '^tests/'
           
         - id: no-root-clutter
           name: Source files must be in src/
           entry: '^(?!src/|tests/|docs/|scripts/|requirements).*\.(py|js|go)$'
           language: pygrep
           types: [file]
   ```

2. **CI/CD Enforcement:**
   ```yaml
   # .github/workflows/structure-check.yml
   name: Structure Enforcement
   on: [push, pull_request]
   
   jobs:
     check-structure:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Check for forbidden files
           run: |
             # Fail if debug files exist
             ! find . -name "*debug*" -o -name "*test_output*" | grep -v ".git"
             
         - name: Check for proper structure
           run: |
             # Ensure required directories exist
             test -d src
             test -d tests
             test -d docs
             
         - name: No versions in filenames
           run: |
             ! find . -name "*_v[0-9]*" -o -name "*_final*"
   ```

---

## FINAL VERDICT

A codebase that looks like it's been through a blender is a codebase that works like it's been through a blender. Organization isn't optional. It's not "nice to have." It's the difference between professional software and a science fair project.

Every file has ONE place. Every function has ONE purpose. Every project has ONE clear structure. Anything else is technical debt that compounds daily.

The standard is not "it works." The standard is "a new developer can understand the entire structure in 30 seconds." If they can't, you've failed before the code even runs.

**Remember:** You're not organizing for today. You're organizing for the poor soul (probably you) who has to maintain this in six months. Be kind to future-you. Current-you will thank you tomorrow.
