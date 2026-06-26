# Security Policy

## Supported Versions

ArsenalX is a single-file CLI tool. Only the **latest version** on the `main` branch receives security fixes.

| Version | Supported |
|---------|-----------|
| latest (`main`) | ✅ |
| older commits   | ❌ |

---

## Scope

ArsenalX itself is a **local tool manager** — it stores, searches, and installs
references to third-party security tools. It does **not**:

- Make outbound network requests on its own
- Store credentials or sensitive user data
- Run any code automatically without explicit user confirmation

Install commands shown in the tool database are executed **only** when the user
explicitly types `y` at the confirmation prompt.

**Out of scope:**
- Vulnerabilities in third-party tools listed in the database (report those upstream)
- Issues arising from running ArsenalX with elevated/root privileges unnecessarily
- Social-engineering attacks targeting end users

---

## Reporting a Vulnerability

Please **do not** file a public GitHub issue for security vulnerabilities.

Instead, report privately via **GitHub's private security advisory**:

1. Go to the repository on GitHub
2. Click **Security** → **Advisories** → **Report a vulnerability**
3. Fill in the form with as much detail as possible

Or email directly: **`jagadeeswar.sec@proton.me`** *(replace with your real address)*

### What to include

- A clear description of the vulnerability
- Steps to reproduce
- Potential impact / attack scenario
- Any suggested fix (optional but appreciated)

### Response timeline

| Milestone | Target |
|-----------|--------|
| Acknowledgement | Within **48 hours** |
| Initial assessment | Within **5 business days** |
| Fix / advisory published | Within **30 days** (critical), 90 days otherwise |

---

## Ethical Use

ArsenalX is designed strictly for **authorized penetration testing, CTF competitions,
security research, and education**. Misuse against systems you do not own or have
explicit written permission to test is illegal and unethical.

By using ArsenalX, you agree to comply with all applicable laws and to use the tool
responsibly.
