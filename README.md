# ⚔️ ArsenalX — Your Cyber Tool Arsenal

A fast, minimal, hacker-themed CLI to store, search, browse, and install cybersecurity tools.
Comes preloaded with **100+ real ethical hacking tools** organized into a clean category → subcategory hierarchy.

![Python 3.8+](https://img.shields.io/badge/python-3.8+-green)
![Tools](https://img.shields.io/badge/tools-100%2B-cyan)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

---

## Quick Start

```bash
# 1. Install the only dependency
pip install colorama

# 2. Run ArsenalX
python arsenalx.py
```

Colorama is auto-installed on first run if missing.

---

## Features

| Feature               | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| **100+ Default Tools**| Preloaded real ethical hacking tools, ready to browse/install   |
| **Hierarchical Browse**| Category → Subcategory → Paginated tool list (no endless scroll)|
| **Fuzzy Search**      | Smart keyword search across name, description, and category     |
| **My Tools**          | Add and manage your own tools saved to `tools.json`             |
| **Custom Tags**       | Tag tools with one or more labels when adding them              |
| **OS-Aware Install**  | Detects Linux/macOS/Windows and runs the right install command  |
| **Import / Export**   | Share your tool collections as portable JSON files              |
| **Dual Input**        | Menu numbers **or** inline typed commands — both work anywhere  |
| **Help Command**      | Built-in `help` screen with purpose, workflow, and examples     |

---

## Tool Categories

Tools are organized into **10 categories**, each split into **logical subcategories**:

| Category    | Subcategories                          | Tools |
|-------------|----------------------------------------|-------|
| **Recon**   | Subdomain · OSINT · Network            | 16    |
| **Scan**    | Port · Vulnerability · Web             | 10    |
| **Web**     | Fuzzing · Proxy · CMS · API            | 13    |
| **Exploit** | Framework · SQLi · XSS · Network       | 14    |
| **Post**    | PrivEsc · Creds · Lateral · Persistence| 12    |
| **Password**| Cracking · Brute · Wordlist            | 12    |
| **Network** | Sniff · MitM · Wireless · Tunnel       | 14    |
| **Forensics**| Disk · Memory · Traffic · Malware     | 11    |
| **Crypto**  | Encoding · Stego                       | 7     |
| **Misc**    | Utility · Reporting                    | 9     |

> **Total: 118+ preloaded tools** — all real, commonly used ethical hacking tools.

---

## Commands

### Menu Mode
| Key | Action                |
|-----|-----------------------|
| `1` | Search Tools          |
| `2` | All Tools (flat list) |
| `3` | Default Tools (browse)|
| `4` | My Tools              |
| `5` | Add Tool              |
| `6` | Install Tool          |
| `7` | Import / Export       |
| `8` | Help                  |
| `0` | Exit                  |

### Inline Commands
Type commands directly at the `arsenalx>` prompt:

```
arsenalx> search nmap
arsenalx> search wireless
arsenalx> install sqlmap
arsenalx> install nuclei
arsenalx> add
arsenalx> list
arsenalx> import backup.json
arsenalx> export mytools.json
arsenalx> help
arsenalx> exit
```

---

## Browsing Default Tools

Option `3` opens a **3-level interactive browser**:

```
DEFAULT TOOLS — Categories
  [1] Recon         16 tools
  [2] Scan          10 tools
  [3] Web           13 tools
  ...
  [a] All tools (flat list)
  [0] Back

> Select category: 1

Recon — Subcategories
  [1] Subdomain      6 tools
  [2] OSINT          7 tools
  [3] Network        5 tools
  [a] All in Recon
  [0] Back

> Select subcategory: 2

Recon / OSINT
  theHarvester  → Gather emails, subdomains, and names from public sources
  shodan        → CLI for the Shodan internet device search engine
  ...
```

Large subcategories paginate automatically (10 tools per page).

---

## Adding a Custom Tool

```
arsenalx> add

[>] Add a new tool to your arsenal
[?] Tool name: mytool
[?] Description: My custom recon script
[?] Category (or press Enter for 'Misc'): Recon
[?] Tags (comma-separated, optional): ctf, osint, bugbounty
[?] Linux install cmd:   git clone https://github.com/me/mytool
[?] macOS install cmd:   git clone https://github.com/me/mytool
[?] Windows install cmd: git clone https://github.com/me/mytool
[?] Note (optional): Requires Python 3.10+

[+] Tool 'mytool' added to your arsenal!  Tags: #ctf #osint #bugbounty
```

Tags appear in **My Tools** and are searchable.

---

## Tool Format (`tools.json`)

Each tool in `tools.json` follows this structure:

```json
{
  "name": "mytool",
  "description": "Short one-line description",
  "category": "Recon",
  "tags": ["ctf", "osint"],
  "install": {
    "linux":   "sudo apt install mytool -y",
    "mac":     "brew install mytool",
    "windows": "choco install mytool -y"
  },
  "note": "Optional note (e.g. requires API key)"
}
```

Default tools also include a `"subcategory"` field used by the hierarchical browser.

---

## Beginner Workflow

1. Run `python arsenalx.py`
2. Press **`3`** → browse Default Tools by category and subcategory
3. Find a tool you want, note its name (e.g. `nmap`)
4. Type **`install nmap`** → confirm → installs for your OS
5. Press **`5`** or type **`add`** to add your own tools with custom tags
6. Use **`search <keyword>`** any time to find tools fast
7. Type **`help`** for a full reference screen

---

## Project Structure

```
ArsenalX/
├── arsenalx.py     # Main CLI application (all logic, 100+ tools)
├── tools.json      # Your custom tools (My Tools) — auto-created
├── requirements.txt
└── README.md
```

---

## Requirements

- **Python 3.8+**
- `colorama` — auto-installed on first run if missing

```bash
pip install colorama
```

---

## Import / Export

Share or backup your custom tool collection:

```bash
# Export My Tools
arsenalx> export backup.json

# Import from a JSON file
arsenalx> import backup.json
```

The JSON file is a list of tool objects (see Tool Format above).

---

## Created by DJ

- GitHub: [DeeeeJayy](https://github.com/DeeeeJayy)
- LinkedIn: [jagadeeswar-m](https://linkedin.com/in/jagadeeswar-m)
- TryHackMe: [Deeeejayy](https://tryhackme.com/p/Deeeejayy)
