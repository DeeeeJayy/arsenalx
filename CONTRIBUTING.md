# Contributing to ArsenalX

Thank you for your interest in contributing! ⚔️  
All contributions are welcome — from tool additions to bug fixes to documentation.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Adding a Tool to the Database](#adding-a-tool-to-the-database)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)

---

## Code of Conduct

Be respectful. This project is for ethical security research and education only.
Contributions that facilitate unauthorized access or illegal activity will be rejected.

---

## Ways to Contribute

| Type | Description |
|------|-------------|
| 🛠 **Add a tool** | Submit a new ethical hacking tool to `DEFAULT_TOOLS` |
| 🐛 **Bug fix** | Fix incorrect behavior, crashes, or edge cases |
| 📝 **Docs** | Improve README, CHANGELOG, or inline comments |
| 🎨 **UX / output** | Improve CLI display, formatting, or navigation |
| 🧪 **Tests** | Add automated tests |
| 💡 **Feature** | Propose or implement a new feature |

---

## Getting Started

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/ArsenalX.git
cd ArsenalX

# 2. Create a branch
git checkout -b feat/add-my-tool

# 3. Install the only dependency
pip install colorama>=0.4.6

# 4. Run ArsenalX to verify it works
python arsenalx.py

# 5. Make your changes, then open a Pull Request
```

---

## Adding a Tool to the Database

New tools go in the `DEFAULT_TOOLS` list inside `arsenalx.py`.

### Rules

1. **Real tools only** — must be publicly available and actively maintained.
2. **Ethical hacking only** — no pure malware, stalkerware, or illegal tools.
3. **One-line description** — factual, concise, no marketing language.
4. **Correct category + subcategory** — see the hierarchy in the file header comment.
5. **All three OS install commands** — use `"echo Not available on <OS>"` if unsupported.
6. **No duplicates** — search the list before adding.

### Template

```python
{
    "name": "toolname",
    "description": "One-line, factual description of what the tool does",
    "category": "Recon",          # top-level category
    "subcategory": "Subdomain",   # logical subgroup within the category
    "install": {
        "linux":   "sudo apt install toolname -y",
        "mac":     "brew install toolname",
        "windows": "choco install toolname -y"
    },
    "note": ""   # optional: e.g. "Requires Go" or "API key needed"
},
```

### Category Hierarchy

```
Recon      → Subdomain · OSINT · Network
Scan       → Port · Vulnerability · Web
Web        → Fuzzing · Proxy · CMS · API
Exploit    → Framework · SQLi · XSS · Network
Post       → PrivEsc · Creds · Lateral · Persistence
Password   → Cracking · Brute · Wordlist
Network    → Sniff · MitM · Wireless · Tunnel
Forensics  → Disk · Memory · Traffic · Malware
Crypto     → Encoding · Stego
Misc       → Utility · Reporting
```

---

## Code Style

- **Python 3.8+** compatible (no walrus operator, no 3.10+ match/case)
- Follow existing formatting — 4-space indentation, f-strings
- Keep functions focused and documented with a one-line docstring
- Do not introduce new runtime dependencies without discussion
- Run `python -c "import ast; ast.parse(open('arsenalx.py').read())"` before submitting

---

## Pull Request Process

1. **Branch from `main`** using a descriptive name:
   - `feat/add-volatility3` for tool additions
   - `fix/search-crash-on-empty` for bug fixes
   - `docs/update-readme` for documentation

2. **Keep PRs focused** — one logical change per PR.

3. **Fill out the PR template** — describe what you changed and why.

4. **Verify it runs** — `python arsenalx.py` must launch without errors.

5. **Update `CHANGELOG.md`** — add an entry under `[Unreleased]`.

6. A maintainer will review and merge. Feedback may be requested.

---

## Reporting Bugs

Use the **Bug Report** issue template on GitHub.

Please include:
- Operating system and Python version
- Steps to reproduce
- What you expected vs. what actually happened
- Any error output or tracebacks

For **security vulnerabilities**, see [SECURITY.md](SECURITY.md) — do **not** file a public issue.
