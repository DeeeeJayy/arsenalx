#!/usr/bin/env python3
"""
ArsenalX — Your Cyber Tool Arsenal
A fast, minimal, hacker-themed CLI to store, search, and install cybersecurity tools.
Created by DJ
"""

import json
import os
import platform
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

# ─── Colorama Setup ──────────────────────────────────────────────────────────

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("[!] colorama not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "-q"])
    from colorama import init, Fore, Style
    init(autoreset=True)

# ─── Color Shortcuts ─────────────────────────────────────────────────────────

GREEN  = Fore.GREEN
CYAN   = Fore.CYAN
YELLOW = Fore.YELLOW
RED    = Fore.RED
GREY   = Fore.LIGHTBLACK_EX
WHITE  = Fore.WHITE
BOLD   = Style.BRIGHT
RESET  = Style.RESET_ALL

# ─── Paths ────────────────────────────────────────────────────────────────────

TOOLS_JSON = Path(__file__).parent / "tools.json"

# ─── Symbols ──────────────────────────────────────────────────────────────────

SYM_OK   = f"{GREEN}[+]{RESET}"
SYM_ERR  = f"{RED}[!]{RESET}"
SYM_ASK  = f"{YELLOW}[?]{RESET}"
SYM_ACT  = f"{CYAN}[>]{RESET}"

# ─── Default Tools Database ──────────────────────────────────────────────────
#
# Category hierarchy:
#   Recon      → Subdomain, OSINT, Network
#   Scan       → Port, Vuln, Web
#   Web        → Fuzzing, Proxy, CMS, API
#   Exploit    → Framework, SQLi, XSS, Network
#   Post       → PrivEsc, Lateral, Persistence, Creds
#   Password   → Cracking, Brute, Wordlist
#   Network    → Sniff, MitM, Wireless, Tunnel
#   Forensics  → Disk, Memory, Traffic, Malware
#   Crypto     → Encoding, Hashing, Stego
#   Misc       → Utility, Reporting, OSINT-Social

DEFAULT_TOOLS = [

    # ════════════════════════════════
    #  RECON
    # ════════════════════════════════

    # ── Recon / Subdomain ──
    {
        "name": "amass",
        "description": "In-depth attack surface mapping and asset discovery",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "sudo apt install amass -y", "mac": "brew install amass", "windows": "choco install amass -y"},
        "note": ""
    },
    {
        "name": "subfinder",
        "description": "Fast passive subdomain enumeration via APIs",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest", "mac": "brew install subfinder", "windows": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"},
        "note": "Requires Go"
    },
    {
        "name": "assetfinder",
        "description": "Find domains and subdomains from public cert logs",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "go install github.com/tomnomnom/assetfinder@latest", "mac": "go install github.com/tomnomnom/assetfinder@latest", "windows": "go install github.com/tomnomnom/assetfinder@latest"},
        "note": "Requires Go"
    },
    {
        "name": "dnsx",
        "description": "Fast and multi-purpose DNS toolkit",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest", "mac": "brew install dnsx", "windows": "go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest"},
        "note": "Requires Go"
    },
    {
        "name": "puredns",
        "description": "Fast domain resolver and subdomain brute-forcer",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "go install github.com/d3mondev/puredns/v2@latest", "mac": "go install github.com/d3mondev/puredns/v2@latest", "windows": "go install github.com/d3mondev/puredns/v2@latest"},
        "note": "Requires Go and massdns"
    },
    {
        "name": "massdns",
        "description": "High-performance DNS stub resolver for bulk lookups",
        "category": "Recon", "subcategory": "Subdomain",
        "install": {"linux": "git clone https://github.com/blechschmidt/massdns && cd massdns && make", "mac": "brew install massdns", "windows": "echo Build from source on Windows"},
        "note": ""
    },

    # ── Recon / OSINT ──
    {
        "name": "theHarvester",
        "description": "Gather emails, subdomains, and names from public sources",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "sudo apt install theharvester -y", "mac": "brew install theharvester", "windows": "pip install theHarvester"},
        "note": ""
    },
    {
        "name": "shodan",
        "description": "CLI for the Shodan internet device search engine",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "pip install shodan", "mac": "pip install shodan", "windows": "pip install shodan"},
        "note": "Requires API key"
    },
    {
        "name": "recon-ng",
        "description": "Full-featured OSINT reconnaissance framework",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "sudo apt install recon-ng -y", "mac": "pip install recon-ng", "windows": "pip install recon-ng"},
        "note": ""
    },
    {
        "name": "maltego",
        "description": "Interactive link analysis and OSINT visualization tool",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "Download from maltego.com", "mac": "Download from maltego.com", "windows": "Download from maltego.com"},
        "note": "GUI tool, free community edition available"
    },
    {
        "name": "spiderfoot",
        "description": "Automated OSINT with 200+ data sources",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "pip install spiderfoot", "mac": "pip install spiderfoot", "windows": "pip install spiderfoot"},
        "note": ""
    },
    {
        "name": "sherlock",
        "description": "Hunt username across 400+ social networks",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "pip install sherlock-project", "mac": "pip install sherlock-project", "windows": "pip install sherlock-project"},
        "note": ""
    },
    {
        "name": "holehe",
        "description": "Check if an email is registered on 120+ sites",
        "category": "Recon", "subcategory": "OSINT",
        "install": {"linux": "pip install holehe", "mac": "pip install holehe", "windows": "pip install holehe"},
        "note": ""
    },

    # ── Recon / Network ──
    {
        "name": "nmap",
        "description": "Network discovery, port scanning, and OS fingerprinting",
        "category": "Recon", "subcategory": "Network",
        "install": {"linux": "sudo apt install nmap -y", "mac": "brew install nmap", "windows": "choco install nmap -y"},
        "note": ""
    },
    {
        "name": "netdiscover",
        "description": "ARP-based network scanner for LAN host discovery",
        "category": "Recon", "subcategory": "Network",
        "install": {"linux": "sudo apt install netdiscover -y", "mac": "echo Linux only", "windows": "echo Linux only"},
        "note": "Linux only"
    },
    {
        "name": "fierce",
        "description": "DNS reconnaissance tool for locating non-contiguous IP space",
        "category": "Recon", "subcategory": "Network",
        "install": {"linux": "pip install fierce", "mac": "pip install fierce", "windows": "pip install fierce"},
        "note": ""
    },
    {
        "name": "dnsrecon",
        "description": "Flexible DNS enumeration script",
        "category": "Recon", "subcategory": "Network",
        "install": {"linux": "sudo apt install dnsrecon -y", "mac": "pip install dnsrecon", "windows": "pip install dnsrecon"},
        "note": ""
    },
    {
        "name": "whatweb",
        "description": "Identify website technologies and fingerprints",
        "category": "Recon", "subcategory": "Network",
        "install": {"linux": "sudo apt install whatweb -y", "mac": "brew install whatweb", "windows": "gem install whatweb"},
        "note": "Requires Ruby"
    },

    # ════════════════════════════════
    #  SCAN
    # ════════════════════════════════

    # ── Scan / Port ──
    {
        "name": "masscan",
        "description": "Ultra-fast internet-scale TCP port scanner",
        "category": "Scan", "subcategory": "Port",
        "install": {"linux": "sudo apt install masscan -y", "mac": "brew install masscan", "windows": "choco install masscan -y"},
        "note": ""
    },
    {
        "name": "rustscan",
        "description": "Blazingly fast port scanner that feeds into nmap",
        "category": "Scan", "subcategory": "Port",
        "install": {"linux": "cargo install rustscan", "mac": "brew install rustscan", "windows": "cargo install rustscan"},
        "note": "Requires Rust/Cargo"
    },
    {
        "name": "sx",
        "description": "Fast, modern network scanner with ARP/ICMP/TCP/UDP",
        "category": "Scan", "subcategory": "Port",
        "install": {"linux": "go install github.com/v-byte-cpu/sx@latest", "mac": "go install github.com/v-byte-cpu/sx@latest", "windows": "go install github.com/v-byte-cpu/sx@latest"},
        "note": "Requires Go"
    },

    # ── Scan / Vulnerability ──
    {
        "name": "nuclei",
        "description": "Community-template-driven vulnerability scanner",
        "category": "Scan", "subcategory": "Vulnerability",
        "install": {"linux": "go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest", "mac": "brew install nuclei", "windows": "go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"},
        "note": "Requires Go"
    },
    {
        "name": "openvas",
        "description": "Full-featured open-source vulnerability management scanner",
        "category": "Scan", "subcategory": "Vulnerability",
        "install": {"linux": "sudo apt install openvas -y && gvm-setup", "mac": "echo Linux only", "windows": "echo Linux only"},
        "note": "Linux recommended; run gvm-setup after install"
    },
    {
        "name": "nessus",
        "description": "Industry-leading commercial vulnerability scanner",
        "category": "Scan", "subcategory": "Vulnerability",
        "install": {"linux": "Download from tenable.com/downloads/nessus", "mac": "Download from tenable.com/downloads/nessus", "windows": "Download from tenable.com/downloads/nessus"},
        "note": "Free Essentials tier available"
    },
    {
        "name": "vulscan",
        "description": "Nmap NSE script for offline CVE vulnerability scanning",
        "category": "Scan", "subcategory": "Vulnerability",
        "install": {"linux": "git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan", "mac": "git clone https://github.com/scipag/vulscan", "windows": "git clone https://github.com/scipag/vulscan"},
        "note": "Requires nmap"
    },

    # ── Scan / Web ──
    {
        "name": "nikto",
        "description": "Web server misconfiguration and vulnerability scanner",
        "category": "Scan", "subcategory": "Web",
        "install": {"linux": "sudo apt install nikto -y", "mac": "brew install nikto", "windows": "choco install nikto -y"},
        "note": ""
    },
    {
        "name": "skipfish",
        "description": "Fully automated active web application security scan",
        "category": "Scan", "subcategory": "Web",
        "install": {"linux": "sudo apt install skipfish -y", "mac": "brew install skipfish", "windows": "echo Linux/Mac only"},
        "note": ""
    },
    {
        "name": "wapiti",
        "description": "Black-box web app vulnerability scanner",
        "category": "Scan", "subcategory": "Web",
        "install": {"linux": "pip install wapiti3", "mac": "pip install wapiti3", "windows": "pip install wapiti3"},
        "note": ""
    },

    # ════════════════════════════════
    #  WEB
    # ════════════════════════════════

    # ── Web / Fuzzing ──
    {
        "name": "ffuf",
        "description": "Fast web fuzzer for directories, files, and parameters",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "go install github.com/ffuf/ffuf/v2@latest", "mac": "brew install ffuf", "windows": "go install github.com/ffuf/ffuf/v2@latest"},
        "note": "Requires Go"
    },
    {
        "name": "gobuster",
        "description": "Brute-force directories, files, DNS, and vhosts",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "sudo apt install gobuster -y", "mac": "brew install gobuster", "windows": "go install github.com/OJ/gobuster/v3@latest"},
        "note": ""
    },
    {
        "name": "feroxbuster",
        "description": "Fast, recursive content discovery tool written in Rust",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "cargo install feroxbuster", "mac": "brew install feroxbuster", "windows": "cargo install feroxbuster"},
        "note": "Requires Rust/Cargo"
    },
    {
        "name": "dirsearch",
        "description": "Multi-threaded web path scanner with many built-in wordlists",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "pip install dirsearch", "mac": "pip install dirsearch", "windows": "pip install dirsearch"},
        "note": ""
    },
    {
        "name": "wfuzz",
        "description": "Web application fuzzer for parameters, auth, and headers",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "pip install wfuzz", "mac": "pip install wfuzz", "windows": "pip install wfuzz"},
        "note": ""
    },
    {
        "name": "arjun",
        "description": "HTTP parameter discovery suite",
        "category": "Web", "subcategory": "Fuzzing",
        "install": {"linux": "pip install arjun", "mac": "pip install arjun", "windows": "pip install arjun"},
        "note": ""
    },

    # ── Web / Proxy & Intercept ──
    {
        "name": "burpsuite",
        "description": "Intercepting proxy and web app security testing platform",
        "category": "Web", "subcategory": "Proxy",
        "install": {"linux": "sudo apt install burpsuite -y", "mac": "brew install --cask burp-suite", "windows": "choco install burp-suite-free-edition -y"},
        "note": ""
    },
    {
        "name": "mitmproxy",
        "description": "Interactive TLS-capable HTTP/HTTPS man-in-the-middle proxy",
        "category": "Web", "subcategory": "Proxy",
        "install": {"linux": "pip install mitmproxy", "mac": "brew install mitmproxy", "windows": "pip install mitmproxy"},
        "note": ""
    },
    {
        "name": "zaproxy",
        "description": "OWASP ZAP – open-source web app security scanner and proxy",
        "category": "Web", "subcategory": "Proxy",
        "install": {"linux": "sudo apt install zaproxy -y", "mac": "brew install --cask owasp-zap", "windows": "choco install owasp-zap -y"},
        "note": ""
    },
    {
        "name": "httpx",
        "description": "Fast HTTP probing and tech fingerprinting toolkit",
        "category": "Web", "subcategory": "Proxy",
        "install": {"linux": "go install github.com/projectdiscovery/httpx/cmd/httpx@latest", "mac": "brew install httpx", "windows": "go install github.com/projectdiscovery/httpx/cmd/httpx@latest"},
        "note": "Requires Go"
    },

    # ── Web / CMS ──
    {
        "name": "wpscan",
        "description": "WordPress vulnerability and plugin security scanner",
        "category": "Web", "subcategory": "CMS",
        "install": {"linux": "gem install wpscan", "mac": "brew install wpscan", "windows": "gem install wpscan"},
        "note": "Requires Ruby"
    },
    {
        "name": "droopescan",
        "description": "Plugin-based CMS scanner for Drupal, Joomla, SilverStripe",
        "category": "Web", "subcategory": "CMS",
        "install": {"linux": "pip install droopescan", "mac": "pip install droopescan", "windows": "pip install droopescan"},
        "note": ""
    },
    {
        "name": "cmseek",
        "description": "CMS detection and exploitation tool for 180+ CMS",
        "category": "Web", "subcategory": "CMS",
        "install": {"linux": "git clone https://github.com/Tuhinshubhra/CMSeek && cd CMSeek && pip install -r requirements.txt", "mac": "git clone https://github.com/Tuhinshubhra/CMSeek", "windows": "git clone https://github.com/Tuhinshubhra/CMSeek"},
        "note": ""
    },

    # ── Web / API ──
    {
        "name": "postman",
        "description": "API development and security testing platform",
        "category": "Web", "subcategory": "API",
        "install": {"linux": "snap install postman", "mac": "brew install --cask postman", "windows": "choco install postman -y"},
        "note": "GUI application"
    },
    {
        "name": "graphw00f",
        "description": "GraphQL fingerprinting and endpoint detection",
        "category": "Web", "subcategory": "API",
        "install": {"linux": "pip install graphw00f", "mac": "pip install graphw00f", "windows": "pip install graphw00f"},
        "note": ""
    },
    {
        "name": "jwt_tool",
        "description": "Test, tamper, and attack JSON Web Tokens",
        "category": "Web", "subcategory": "API",
        "install": {"linux": "git clone https://github.com/ticarpi/jwt_tool && pip install -r requirements.txt", "mac": "git clone https://github.com/ticarpi/jwt_tool", "windows": "git clone https://github.com/ticarpi/jwt_tool"},
        "note": ""
    },

    # ════════════════════════════════
    #  EXPLOIT
    # ════════════════════════════════

    # ── Exploit / Framework ──
    {
        "name": "metasploit",
        "description": "World's most used penetration testing framework",
        "category": "Exploit", "subcategory": "Framework",
        "install": {"linux": "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall", "mac": "brew install metasploit", "windows": "choco install metasploit -y"},
        "note": ""
    },
    {
        "name": "searchsploit",
        "description": "Offline CLI search for the Exploit-DB archive",
        "category": "Exploit", "subcategory": "Framework",
        "install": {"linux": "sudo apt install exploitdb -y", "mac": "brew install exploitdb", "windows": "git clone https://gitlab.com/exploit-database/exploitdb.git"},
        "note": ""
    },
    {
        "name": "empire",
        "description": "PowerShell and Python post-exploitation agent framework",
        "category": "Exploit", "subcategory": "Framework",
        "install": {"linux": "sudo apt install powershell-empire -y", "mac": "echo Linux preferred", "windows": "echo Linux preferred"},
        "note": ""
    },
    {
        "name": "sliver",
        "description": "Open-source adversary simulation and red team C2 framework",
        "category": "Exploit", "subcategory": "Framework",
        "install": {"linux": "curl https://sliver.sh/install | sudo bash", "mac": "curl https://sliver.sh/install | sudo bash", "windows": "Download from github.com/BishopFox/sliver/releases"},
        "note": ""
    },
    {
        "name": "covenant",
        "description": ".NET-based collaborative C2 and red team framework",
        "category": "Exploit", "subcategory": "Framework",
        "install": {"linux": "git clone https://github.com/cobbr/Covenant && cd Covenant/Covenant && dotnet run", "mac": "git clone https://github.com/cobbr/Covenant", "windows": "git clone https://github.com/cobbr/Covenant"},
        "note": "Requires .NET 6"
    },

    # ── Exploit / SQLi ──
    {
        "name": "sqlmap",
        "description": "Automatic SQL injection detection and exploitation",
        "category": "Exploit", "subcategory": "SQLi",
        "install": {"linux": "sudo apt install sqlmap -y", "mac": "brew install sqlmap", "windows": "pip install sqlmap"},
        "note": ""
    },
    {
        "name": "nosqlmap",
        "description": "Automated NoSQL injection and MongoDB exploitation",
        "category": "Exploit", "subcategory": "SQLi",
        "install": {"linux": "git clone https://github.com/codingo/NoSQLMap && python setup.py install", "mac": "git clone https://github.com/codingo/NoSQLMap", "windows": "git clone https://github.com/codingo/NoSQLMap"},
        "note": ""
    },

    # ── Exploit / XSS & Injection ──
    {
        "name": "xsstrike",
        "description": "Advanced XSS detection and exploitation suite",
        "category": "Exploit", "subcategory": "XSS",
        "install": {"linux": "git clone https://github.com/s0md3v/XSStrike && pip install -r requirements.txt", "mac": "git clone https://github.com/s0md3v/XSStrike", "windows": "git clone https://github.com/s0md3v/XSStrike"},
        "note": ""
    },
    {
        "name": "dalfox",
        "description": "Fast parameter analysis and XSS scanning tool",
        "category": "Exploit", "subcategory": "XSS",
        "install": {"linux": "go install github.com/hahwul/dalfox/v2@latest", "mac": "brew install dalfox", "windows": "go install github.com/hahwul/dalfox/v2@latest"},
        "note": "Requires Go"
    },
    {
        "name": "commix",
        "description": "Automated command injection and exploitation tool",
        "category": "Exploit", "subcategory": "XSS",
        "install": {"linux": "sudo apt install commix -y", "mac": "pip install commix", "windows": "pip install commix"},
        "note": ""
    },

    # ── Exploit / Network ──
    {
        "name": "responder",
        "description": "LLMNR/NBT-NS/MDNS poisoner for credential capture",
        "category": "Exploit", "subcategory": "Network",
        "install": {"linux": "git clone https://github.com/lgandx/Responder", "mac": "echo Linux only", "windows": "echo Linux only"},
        "note": "Linux only"
    },
    {
        "name": "crackmapexec",
        "description": "Swiss army knife for pentesting Windows/AD environments",
        "category": "Exploit", "subcategory": "Network",
        "install": {"linux": "sudo apt install crackmapexec -y", "mac": "pip install crackmapexec", "windows": "pip install crackmapexec"},
        "note": ""
    },
    {
        "name": "impacket",
        "description": "Python classes for working with Windows network protocols",
        "category": "Exploit", "subcategory": "Network",
        "install": {"linux": "pip install impacket", "mac": "pip install impacket", "windows": "pip install impacket"},
        "note": ""
    },
    {
        "name": "coercer",
        "description": "Coerce Windows hosts to authenticate to an attacker machine",
        "category": "Exploit", "subcategory": "Network",
        "install": {"linux": "pip install coercer", "mac": "pip install coercer", "windows": "pip install coercer"},
        "note": ""
    },

    # ════════════════════════════════
    #  POST-EXPLOITATION
    # ════════════════════════════════

    # ── Post / PrivEsc ──
    {
        "name": "linpeas",
        "description": "Linux privilege escalation enumeration script",
        "category": "Post", "subcategory": "PrivEsc",
        "install": {"linux": "curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -o linpeas.sh", "mac": "curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -o linpeas.sh", "windows": "echo Use winpeas on Windows"},
        "note": ""
    },
    {
        "name": "winpeas",
        "description": "Windows privilege escalation enumeration script",
        "category": "Post", "subcategory": "PrivEsc",
        "install": {"linux": "echo Use linpeas on Linux", "mac": "echo Use linpeas on macOS", "windows": "curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe -o winpeas.exe"},
        "note": ""
    },
    {
        "name": "beroot",
        "description": "Privilege escalation checker for Linux, Windows, and macOS",
        "category": "Post", "subcategory": "PrivEsc",
        "install": {"linux": "git clone https://github.com/AlessandroZ/BeRoot && pip install -r requirements.txt", "mac": "git clone https://github.com/AlessandroZ/BeRoot", "windows": "git clone https://github.com/AlessandroZ/BeRoot"},
        "note": ""
    },
    {
        "name": "suid3num",
        "description": "Enumerate exploitable SUID binaries on Linux",
        "category": "Post", "subcategory": "PrivEsc",
        "install": {"linux": "git clone https://github.com/Anon-Exploiter/SUID3NUM", "mac": "echo Linux only", "windows": "echo Linux only"},
        "note": "Linux only"
    },

    # ── Post / Credential Dumping ──
    {
        "name": "mimikatz",
        "description": "Windows credential and hash extraction tool",
        "category": "Post", "subcategory": "Creds",
        "install": {"linux": "echo Windows-only tool", "mac": "echo Windows-only tool", "windows": "git clone https://github.com/gentilkiwi/mimikatz.git"},
        "note": "Windows only"
    },
    {
        "name": "pypykatz",
        "description": "Python implementation of Mimikatz for offline analysis",
        "category": "Post", "subcategory": "Creds",
        "install": {"linux": "pip install pypykatz", "mac": "pip install pypykatz", "windows": "pip install pypykatz"},
        "note": ""
    },
    {
        "name": "lazagne",
        "description": "Retrieve stored credentials from 60+ apps on disk",
        "category": "Post", "subcategory": "Creds",
        "install": {"linux": "git clone https://github.com/AlessandroZ/LaZagne && pip install -r requirements.txt", "mac": "git clone https://github.com/AlessandroZ/LaZagne", "windows": "Download from github.com/AlessandroZ/LaZagne/releases"},
        "note": ""
    },

    # ── Post / Lateral Movement ──
    {
        "name": "evil-winrm",
        "description": "Full-featured WinRM shell for Windows pentesting",
        "category": "Post", "subcategory": "Lateral",
        "install": {"linux": "gem install evil-winrm", "mac": "gem install evil-winrm", "windows": "gem install evil-winrm"},
        "note": "Requires Ruby"
    },
    {
        "name": "psexec",
        "description": "Execute processes remotely on Windows via SMB",
        "category": "Post", "subcategory": "Lateral",
        "install": {"linux": "pip install impacket", "mac": "pip install impacket", "windows": "pip install impacket"},
        "note": "Part of Impacket suite"
    },
    {
        "name": "chisel",
        "description": "Fast TCP/UDP tunnel over HTTP using SSH",
        "category": "Post", "subcategory": "Lateral",
        "install": {"linux": "go install github.com/jpillora/chisel@latest", "mac": "brew install chisel", "windows": "go install github.com/jpillora/chisel@latest"},
        "note": "Requires Go"
    },
    {
        "name": "ligolo-ng",
        "description": "Fast pivoting tool using reverse tunnels and TUN interfaces",
        "category": "Post", "subcategory": "Lateral",
        "install": {"linux": "go install github.com/nicocha30/ligolo-ng/cmd/proxy@latest", "mac": "go install github.com/nicocha30/ligolo-ng/cmd/proxy@latest", "windows": "Download from github.com/nicocha30/ligolo-ng/releases"},
        "note": "Requires Go"
    },

    # ── Post / Persistence ──
    {
        "name": "crontab-persistence",
        "description": "Document cron-based persistence techniques for Linux",
        "category": "Post", "subcategory": "Persistence",
        "install": {"linux": "echo Built-in — use crontab -e", "mac": "echo Built-in — use crontab -e", "windows": "echo Use Task Scheduler on Windows"},
        "note": "Reference technique"
    },
    {
        "name": "schtasks-ref",
        "description": "Windows scheduled task persistence reference",
        "category": "Post", "subcategory": "Persistence",
        "install": {"linux": "echo Windows only", "mac": "echo Windows only", "windows": "echo Built-in — use schtasks /create"},
        "note": "Windows only — reference technique"
    },

    # ════════════════════════════════
    #  PASSWORD
    # ════════════════════════════════

    # ── Password / Cracking ──
    {
        "name": "hashcat",
        "description": "GPU-accelerated hash cracking with 300+ hash types",
        "category": "Password", "subcategory": "Cracking",
        "install": {"linux": "sudo apt install hashcat -y", "mac": "brew install hashcat", "windows": "choco install hashcat -y"},
        "note": ""
    },
    {
        "name": "john",
        "description": "John the Ripper — versatile CPU password cracker",
        "category": "Password", "subcategory": "Cracking",
        "install": {"linux": "sudo apt install john -y", "mac": "brew install john", "windows": "choco install john -y"},
        "note": ""
    },
    {
        "name": "haiti",
        "description": "Hash type identifier for 500+ hash formats",
        "category": "Password", "subcategory": "Cracking",
        "install": {"linux": "gem install haiti-hash", "mac": "gem install haiti-hash", "windows": "gem install haiti-hash"},
        "note": "Requires Ruby"
    },
    {
        "name": "name-that-hash",
        "description": "Identify hash types with confidence rankings",
        "category": "Password", "subcategory": "Cracking",
        "install": {"linux": "pip install name-that-hash", "mac": "pip install name-that-hash", "windows": "pip install name-that-hash"},
        "note": ""
    },

    # ── Password / Brute Force ──
    {
        "name": "hydra",
        "description": "Parallelized network login brute-forcer for 50+ protocols",
        "category": "Password", "subcategory": "Brute",
        "install": {"linux": "sudo apt install hydra -y", "mac": "brew install hydra", "windows": "choco install thc-hydra -y"},
        "note": ""
    },
    {
        "name": "medusa",
        "description": "Speedy, parallel network login brute-forcer",
        "category": "Password", "subcategory": "Brute",
        "install": {"linux": "sudo apt install medusa -y", "mac": "brew install medusa", "windows": "echo Linux recommended"},
        "note": ""
    },
    {
        "name": "patator",
        "description": "Modular brute-forcer for network services and web apps",
        "category": "Password", "subcategory": "Brute",
        "install": {"linux": "sudo apt install patator -y", "mac": "pip install patator", "windows": "pip install patator"},
        "note": ""
    },
    {
        "name": "spray",
        "description": "Password sprayer for Active Directory environments",
        "category": "Password", "subcategory": "Brute",
        "install": {"linux": "go install github.com/Greenwolf/Spray@latest", "mac": "go install github.com/Greenwolf/Spray@latest", "windows": "go install github.com/Greenwolf/Spray@latest"},
        "note": "Requires Go"
    },

    # ── Password / Wordlist ──
    {
        "name": "crunch",
        "description": "Generate custom wordlists by charset and pattern",
        "category": "Password", "subcategory": "Wordlist",
        "install": {"linux": "sudo apt install crunch -y", "mac": "brew install crunch", "windows": "echo Not natively available on Windows"},
        "note": ""
    },
    {
        "name": "cewl",
        "description": "Spider a URL and generate a wordlist from page content",
        "category": "Password", "subcategory": "Wordlist",
        "install": {"linux": "sudo apt install cewl -y", "mac": "gem install cewl", "windows": "gem install cewl"},
        "note": "Requires Ruby"
    },
    {
        "name": "rockyou",
        "description": "Classic 14M-entry password wordlist for cracking",
        "category": "Password", "subcategory": "Wordlist",
        "install": {"linux": "sudo apt install wordlists -y && gunzip /usr/share/wordlists/rockyou.txt.gz", "mac": "wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", "windows": "Invoke-WebRequest -Uri https://raw.githubusercontent.com/praetorian-inc/Hob0Rules/master/wordlists/rockyou.txt.gz -OutFile rockyou.txt.gz"},
        "note": "Already available on Kali Linux"
    },
    {
        "name": "mentalist",
        "description": "Graphical wordlist generator with rule chaining",
        "category": "Password", "subcategory": "Wordlist",
        "install": {"linux": "Download from github.com/sc0tfree/mentalist", "mac": "Download from github.com/sc0tfree/mentalist", "windows": "Download from github.com/sc0tfree/mentalist"},
        "note": "GUI tool"
    },

    # ════════════════════════════════
    #  NETWORK
    # ════════════════════════════════

    # ── Network / Sniffing ──
    {
        "name": "wireshark",
        "description": "GUI network protocol analyzer and packet capture tool",
        "category": "Network", "subcategory": "Sniff",
        "install": {"linux": "sudo apt install wireshark -y", "mac": "brew install --cask wireshark", "windows": "choco install wireshark -y"},
        "note": ""
    },
    {
        "name": "tcpdump",
        "description": "Command-line packet capture and analyzer",
        "category": "Network", "subcategory": "Sniff",
        "install": {"linux": "sudo apt install tcpdump -y", "mac": "brew install tcpdump", "windows": "choco install windump -y"},
        "note": ""
    },
    {
        "name": "tshark",
        "description": "Command-line Wireshark for scripted packet analysis",
        "category": "Network", "subcategory": "Sniff",
        "install": {"linux": "sudo apt install tshark -y", "mac": "brew install wireshark", "windows": "choco install wireshark -y"},
        "note": "Installed with Wireshark"
    },
    {
        "name": "dsniff",
        "description": "Collection of tools for network auditing and sniffing",
        "category": "Network", "subcategory": "Sniff",
        "install": {"linux": "sudo apt install dsniff -y", "mac": "brew install dsniff", "windows": "echo Linux/Mac preferred"},
        "note": ""
    },

    # ── Network / MitM ──
    {
        "name": "ettercap",
        "description": "Man-in-the-middle attack suite with ARP poisoning",
        "category": "Network", "subcategory": "MitM",
        "install": {"linux": "sudo apt install ettercap-graphical -y", "mac": "brew install ettercap", "windows": "echo Linux recommended"},
        "note": ""
    },
    {
        "name": "arpspoof",
        "description": "ARP cache poisoning for LAN MitM attacks",
        "category": "Network", "subcategory": "MitM",
        "install": {"linux": "sudo apt install dsniff -y", "mac": "brew install dsniff", "windows": "echo Linux preferred"},
        "note": "Part of dsniff"
    },
    {
        "name": "bettercap",
        "description": "Swiss army knife for network attacks and monitoring",
        "category": "Network", "subcategory": "MitM",
        "install": {"linux": "sudo apt install bettercap -y", "mac": "brew install bettercap", "windows": "Download from bettercap.org"},
        "note": ""
    },

    # ── Network / Wireless ──
    {
        "name": "aircrack-ng",
        "description": "Complete suite for Wi-Fi security auditing",
        "category": "Network", "subcategory": "Wireless",
        "install": {"linux": "sudo apt install aircrack-ng -y", "mac": "brew install aircrack-ng", "windows": "choco install aircrack-ng -y"},
        "note": ""
    },
    {
        "name": "wifite",
        "description": "Automated wireless auditing tool using aircrack-ng stack",
        "category": "Network", "subcategory": "Wireless",
        "install": {"linux": "sudo apt install wifite -y", "mac": "pip install wifite", "windows": "echo Linux only"},
        "note": "Linux recommended"
    },
    {
        "name": "kismet",
        "description": "Wireless network detector, sniffer, and IDS",
        "category": "Network", "subcategory": "Wireless",
        "install": {"linux": "sudo apt install kismet -y", "mac": "brew install kismet", "windows": "echo Linux/Mac only"},
        "note": ""
    },
    {
        "name": "hcxtools",
        "description": "Convert WPA captures for use with hashcat",
        "category": "Network", "subcategory": "Wireless",
        "install": {"linux": "sudo apt install hcxtools -y", "mac": "brew install hcxtools", "windows": "echo Linux recommended"},
        "note": ""
    },

    # ── Network / Tunneling ──
    {
        "name": "proxychains",
        "description": "Redirect TCP connections through SOCKS/HTTP proxies",
        "category": "Network", "subcategory": "Tunnel",
        "install": {"linux": "sudo apt install proxychains4 -y", "mac": "brew install proxychains-ng", "windows": "echo Linux preferred"},
        "note": ""
    },
    {
        "name": "socat",
        "description": "Multipurpose relay for bidirectional data transfer",
        "category": "Network", "subcategory": "Tunnel",
        "install": {"linux": "sudo apt install socat -y", "mac": "brew install socat", "windows": "choco install socat -y"},
        "note": ""
    },
    {
        "name": "sshuttle",
        "description": "Transparent proxy server for VPN-like tunneling via SSH",
        "category": "Network", "subcategory": "Tunnel",
        "install": {"linux": "pip install sshuttle", "mac": "brew install sshuttle", "windows": "echo Linux/Mac only"},
        "note": ""
    },

    # ════════════════════════════════
    #  FORENSICS
    # ════════════════════════════════

    # ── Forensics / Disk ──
    {
        "name": "autopsy",
        "description": "GUI digital forensics platform for disk image analysis",
        "category": "Forensics", "subcategory": "Disk",
        "install": {"linux": "sudo apt install autopsy -y", "mac": "Download from sleuthkit.org/autopsy", "windows": "Download from sleuthkit.org/autopsy"},
        "note": "GUI tool"
    },
    {
        "name": "sleuthkit",
        "description": "CLI library and tools for disk forensics analysis",
        "category": "Forensics", "subcategory": "Disk",
        "install": {"linux": "sudo apt install sleuthkit -y", "mac": "brew install sleuthkit", "windows": "choco install sleuthkit -y"},
        "note": ""
    },
    {
        "name": "testdisk",
        "description": "Recover lost partitions and repair boot sectors",
        "category": "Forensics", "subcategory": "Disk",
        "install": {"linux": "sudo apt install testdisk -y", "mac": "brew install testdisk", "windows": "choco install testdisk -y"},
        "note": ""
    },

    # ── Forensics / Memory ──
    {
        "name": "volatility3",
        "description": "Advanced memory forensics and malware analysis framework",
        "category": "Forensics", "subcategory": "Memory",
        "install": {"linux": "pip install volatility3", "mac": "pip install volatility3", "windows": "pip install volatility3"},
        "note": ""
    },
    {
        "name": "rekall",
        "description": "Memory forensics framework derived from Volatility",
        "category": "Forensics", "subcategory": "Memory",
        "install": {"linux": "pip install rekall", "mac": "pip install rekall", "windows": "pip install rekall"},
        "note": ""
    },

    # ── Forensics / Traffic ──
    {
        "name": "networkminer",
        "description": "Passive network sniffer and packet capture analyzer",
        "category": "Forensics", "subcategory": "Traffic",
        "install": {"linux": "Download from netresec.com/networkminer", "mac": "Download from netresec.com/networkminer", "windows": "Download from netresec.com/networkminer"},
        "note": "Free Community edition available"
    },
    {
        "name": "zeek",
        "description": "Network traffic analysis framework for security monitoring",
        "category": "Forensics", "subcategory": "Traffic",
        "install": {"linux": "sudo apt install zeek -y", "mac": "brew install zeek", "windows": "echo Linux/Mac preferred"},
        "note": ""
    },
    {
        "name": "xplico",
        "description": "Reconstruct application data from network captures",
        "category": "Forensics", "subcategory": "Traffic",
        "install": {"linux": "sudo apt install xplico -y", "mac": "echo Linux preferred", "windows": "echo Linux preferred"},
        "note": "Linux preferred"
    },

    # ── Forensics / Malware ──
    {
        "name": "clamav",
        "description": "Open-source antivirus engine for malware scanning",
        "category": "Forensics", "subcategory": "Malware",
        "install": {"linux": "sudo apt install clamav -y", "mac": "brew install clamav", "windows": "choco install clamav -y"},
        "note": ""
    },
    {
        "name": "yara",
        "description": "Pattern-matching tool for malware classification",
        "category": "Forensics", "subcategory": "Malware",
        "install": {"linux": "sudo apt install yara -y", "mac": "brew install yara", "windows": "choco install yara -y"},
        "note": ""
    },
    {
        "name": "cuckoo",
        "description": "Automated malware sandbox for behavior analysis",
        "category": "Forensics", "subcategory": "Malware",
        "install": {"linux": "pip install cuckoo", "mac": "pip install cuckoo", "windows": "pip install cuckoo"},
        "note": "Requires VirtualBox and additional setup"
    },

    # ════════════════════════════════
    #  CRYPTO
    # ════════════════════════════════

    # ── Crypto / Encoding ──
    {
        "name": "cyberchef",
        "description": "Web-based encoding, decoding, and crypto Swiss army knife",
        "category": "Crypto", "subcategory": "Encoding",
        "install": {"linux": "npx serve github.com/gchq/CyberChef", "mac": "npx serve github.com/gchq/CyberChef", "windows": "Use online at gchq.github.io/CyberChef"},
        "note": "Also available online at gchq.github.io/CyberChef"
    },
    {
        "name": "featherduster",
        "description": "Automated classical cryptanalysis and cipher breaking",
        "category": "Crypto", "subcategory": "Encoding",
        "install": {"linux": "pip install featherduster", "mac": "pip install featherduster", "windows": "pip install featherduster"},
        "note": ""
    },
    {
        "name": "rsactftool",
        "description": "RSA attack tool for weak key exploitation in CTF/research",
        "category": "Crypto", "subcategory": "Encoding",
        "install": {"linux": "git clone https://github.com/RsaCtfTool/RsaCtfTool && pip install -r requirements.txt", "mac": "git clone https://github.com/RsaCtfTool/RsaCtfTool", "windows": "git clone https://github.com/RsaCtfTool/RsaCtfTool"},
        "note": "For educational/CTF use only"
    },

    # ── Crypto / Stego ──
    {
        "name": "steghide",
        "description": "Hide and extract data inside image/audio files",
        "category": "Crypto", "subcategory": "Stego",
        "install": {"linux": "sudo apt install steghide -y", "mac": "brew install steghide", "windows": "choco install steghide -y"},
        "note": ""
    },
    {
        "name": "exiftool",
        "description": "Read, write, and edit metadata in files",
        "category": "Crypto", "subcategory": "Stego",
        "install": {"linux": "sudo apt install libimage-exiftool-perl -y", "mac": "brew install exiftool", "windows": "choco install exiftool -y"},
        "note": ""
    },
    {
        "name": "stegseek",
        "description": "Lightning-fast steghide brute-forcer using wordlists",
        "category": "Crypto", "subcategory": "Stego",
        "install": {"linux": "Download .deb from github.com/RickdeJager/stegseek/releases", "mac": "echo Linux only", "windows": "echo Linux only"},
        "note": "Linux only"
    },
    {
        "name": "binwalk",
        "description": "Firmware analysis and embedded file extraction",
        "category": "Crypto", "subcategory": "Stego",
        "install": {"linux": "sudo apt install binwalk -y", "mac": "brew install binwalk", "windows": "pip install binwalk"},
        "note": ""
    },

    # ════════════════════════════════
    #  MISC
    # ════════════════════════════════

    # ── Misc / Utility ──
    {
        "name": "tmux",
        "description": "Terminal multiplexer for persistent hacking sessions",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "sudo apt install tmux -y", "mac": "brew install tmux", "windows": "choco install tmux -y"},
        "note": ""
    },
    {
        "name": "netcat",
        "description": "TCP/UDP networking utility for listening, sending, and pivoting",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "sudo apt install netcat-traditional -y", "mac": "brew install netcat", "windows": "choco install netcat -y"},
        "note": ""
    },
    {
        "name": "curl",
        "description": "Transfer data from or to servers with any protocol",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "sudo apt install curl -y", "mac": "brew install curl", "windows": "choco install curl -y"},
        "note": ""
    },
    {
        "name": "jq",
        "description": "Lightweight command-line JSON processor",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "sudo apt install jq -y", "mac": "brew install jq", "windows": "choco install jq -y"},
        "note": ""
    },
    {
        "name": "seclists",
        "description": "Collection of multiple types of security-related wordlists",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "sudo apt install seclists -y", "mac": "brew install seclists", "windows": "git clone https://github.com/danielmiessler/SecLists"},
        "note": "Large download (~1GB)"
    },
    {
        "name": "pwntools",
        "description": "CTF framework and exploit dev library for Python",
        "category": "Misc", "subcategory": "Utility",
        "install": {"linux": "pip install pwntools", "mac": "pip install pwntools", "windows": "pip install pwntools"},
        "note": ""
    },

    # ── Misc / Reporting ──
    {
        "name": "dradis",
        "description": "Collaborative reporting and pentest management platform",
        "category": "Misc", "subcategory": "Reporting",
        "install": {"linux": "gem install dradis", "mac": "gem install dradis", "windows": "gem install dradis"},
        "note": "Requires Ruby"
    },
    {
        "name": "faraday",
        "description": "Multi-user collaborative pentest management IDE",
        "category": "Misc", "subcategory": "Reporting",
        "install": {"linux": "pip install faradaysec", "mac": "pip install faradaysec", "windows": "pip install faradaysec"},
        "note": ""
    },
    {
        "name": "pwndoc",
        "description": "Pentest report generation with a web UI and templates",
        "category": "Misc", "subcategory": "Reporting",
        "install": {"linux": "git clone https://github.com/pwndoc/pwndoc && cd pwndoc && docker-compose up", "mac": "git clone https://github.com/pwndoc/pwndoc", "windows": "git clone https://github.com/pwndoc/pwndoc"},
        "note": "Requires Docker"
    },
]

# Top-level categories (ordered for display)
CATEGORIES = ["Recon", "Scan", "Web", "Exploit", "Post", "Password", "Network", "Forensics", "Crypto", "Misc"]

# Subcategory order per category (for display)
SUBCAT_ORDER: dict[str, list[str]] = {
    "Recon":     ["Subdomain", "OSINT", "Network"],
    "Scan":      ["Port", "Vulnerability", "Web"],
    "Web":       ["Fuzzing", "Proxy", "CMS", "API"],
    "Exploit":   ["Framework", "SQLi", "XSS", "Network"],
    "Post":      ["PrivEsc", "Creds", "Lateral", "Persistence"],
    "Password":  ["Cracking", "Brute", "Wordlist"],
    "Network":   ["Sniff", "MitM", "Wireless", "Tunnel"],
    "Forensics": ["Disk", "Memory", "Traffic", "Malware"],
    "Crypto":    ["Encoding", "Stego"],
    "Misc":      ["Utility", "Reporting"],
}


# ═══════════════════════════════════════════════════════════════════════════════
#  DATA LAYER
# ═══════════════════════════════════════════════════════════════════════════════

def load_my_tools() -> list[dict]:
    """Load user-added tools from tools.json."""
    if not TOOLS_JSON.exists():
        return []
    try:
        with open(TOOLS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, IOError):
        return []


def save_my_tools(tools: list[dict]) -> None:
    """Persist user-added tools to tools.json."""
    with open(TOOLS_JSON, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)


def get_all_tools() -> list[dict]:
    """Merge default tools + user tools."""
    return DEFAULT_TOOLS + load_my_tools()


# ═══════════════════════════════════════════════════════════════════════════════
#  OS DETECTION
# ═══════════════════════════════════════════════════════════════════════════════

def detect_os() -> str:
    """Return 'linux', 'mac', or 'windows'."""
    sys_name = platform.system().lower()
    if sys_name == "darwin":
        return "mac"
    if sys_name == "windows":
        return "windows"
    return "linux"


# ═══════════════════════════════════════════════════════════════════════════════
#  DISPLAY HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def print_banner() -> None:
    banner = f"""{GREEN}{BOLD}
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     █████╗ ██████╗ ███████╗███████╗███╗   ██╗ █████╗ ██╗      ║
    ║    ██╔══██╗██╔══██╗██╔════╝██╔════╝████╗  ██║██╔══██╗██║      ║
    ║    ███████║██████╔╝███████╗█████╗  ██╔██╗ ██║███████║██║      ║
    ║    ██╔══██║██╔══██╗╚════██║██╔══╝  ██║╚██╗██║██╔══██║██║      ║
    ║    ██║  ██║██║  ██║███████║███████╗██║ ╚████║██║  ██║███████╗ ║ 
    ║    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ║
    ║                      ██╗  ██╗                                 ║
    ║                      ╚██╗██╔╝                                 ║
    ║                       ╚███╔╝                                  ║
    ║                       ██╔██╗                                  ║
    ║                      ██╔╝ ██╗                                 ║
    ║                      ╚═╝  ╚═╝                                 ║
    ║                                                               ║
    ║        ⚔️  ARSENALX — YOUR CYBER TOOL ARSENAL  ⚔️               ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝{RESET}"""
    print(banner)


def print_header() -> None:
    print(f"\n  {CYAN}{BOLD}ARSENALX // CONTROL PANEL{RESET}")
    print(f"  {GREY}Status: {GREEN}READY{GREY}  |  Mode: {GREEN}INTERACTIVE{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")


def print_menu() -> None:
    print(f"""
  {CYAN}╔══════════════════════════════════════════════════╗{RESET}
  {CYAN}║{RESET}  {BOLD}{WHITE}Select operation:{RESET}                               {CYAN}║{RESET}
  {CYAN}╠══════════════════════════════════════════════════╣{RESET}
  {CYAN}║{RESET}                                                  {CYAN}║{RESET}
  {CYAN}║{RESET}   {GREEN}[1]{RESET} Search Tools      {GREEN}[2]{RESET} All Tools            {CYAN}║{RESET}
  {CYAN}║{RESET}   {GREEN}[3]{RESET} Default Tools     {GREEN}[4]{RESET} My Tools             {CYAN}║{RESET}
  {CYAN}║{RESET}   {GREEN}[5]{RESET} Add Tool          {GREEN}[6]{RESET} Install Tool         {CYAN}║{RESET}
  {CYAN}║{RESET}   {GREEN}[7]{RESET} Import / Export   {GREEN}[8]{RESET} Help                 {CYAN}║{RESET}
  {CYAN}║{RESET}                         {GREEN}[0]{RESET} Exit                 {CYAN}║{RESET}
  {CYAN}║{RESET}                                                  {CYAN}║{RESET}
  {CYAN}╚══════════════════════════════════════════════════╝{RESET}
""")


def print_footer() -> None:
    print(f"\n  {GREY}{'─' * 50}{RESET}")
    print(f"  {GREY}Created by {WHITE}DJ{RESET}")
    print(f"  {GREY}GitHub:   {CYAN}https://github.com/DeeeeJayy{RESET}")
    print(f"  {GREY}LinkedIn: {CYAN}https://linkedin.com/in/jagadeeswar-m{RESET}")
    print(f"  {GREY}TryHackMe:  {CYAN}https://tryhackme.com/p/Deeeejayy{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}\n")


def print_tool_line(tool: dict, index: int = 0) -> None:
    """Display a single tool as: name → short description (1 line)."""
    name = tool.get("name", "unknown")
    desc = tool.get("description", "")
    cat  = tool.get("category", "")
    # Truncate description to keep it one line
    if len(desc) > 55:
        desc = desc[:52] + "..."
    print(f"  {GREEN}{name:<16}{RESET} {GREY}→{RESET} {WHITE}{desc}{RESET}  {GREY}[{cat}]{RESET}")


def print_tools_by_category(tools: list[dict], title: str) -> None:
    """Display tools grouped by category (flat list, no subcategory breakdown)."""
    print(f"\n  {CYAN}{BOLD}{title}{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")

    if not tools:
        print(f"  {GREY}(no tools found){RESET}")
        return

    grouped: dict[str, list[dict]] = {}
    for t in tools:
        cat = t.get("category", "Other")
        grouped.setdefault(cat, []).append(t)

    for cat in CATEGORIES + sorted(set(grouped.keys()) - set(CATEGORIES)):
        if cat not in grouped:
            continue
        print(f"\n  {YELLOW}{BOLD}  ── {cat} ({len(grouped[cat])}) ──{RESET}")
        for tool in grouped[cat]:
            print_tool_line(tool)

    print(f"\n  {GREY}Total: {len(tools)} tools{RESET}")


PAGE_SIZE = 10  # tools per page for paginated subcategory views


def _paginate_tools(tools: list[dict], subcat_label: str) -> None:
    """Display tools in pages of PAGE_SIZE, asking to continue."""
    total = len(tools)
    if total == 0:
        return
    for i in range(0, total, PAGE_SIZE):
        page = tools[i: i + PAGE_SIZE]
        for tool in page:
            print_tool_line(tool)
        remaining = total - (i + PAGE_SIZE)
        if remaining > 0:
            more = input(
                f"  {GREY}── {remaining} more in {subcat_label} – press Enter to continue (or 'q' to skip) {RESET}"
            ).strip().lower()
            if more == "q":
                break


def cmd_browse_default_tools() -> None:
    """
    Hierarchical browser: Category → Subcategory → paginated tool list.
    Replaces the old flat cmd_default_tools for the menu option.
    """
    while True:
        # ── Level 1: category selection ──
        print(f"\n  {CYAN}{BOLD}DEFAULT TOOLS — Categories{RESET}")
        print(f"  {GREY}{'─' * 50}{RESET}")

        # Build category summary
        cat_counts: dict[str, int] = {}
        for t in DEFAULT_TOOLS:
            c = t.get("category", "Other")
            cat_counts[c] = cat_counts.get(c, 0) + 1

        ordered_cats = [c for c in CATEGORIES if c in cat_counts]
        extra_cats   = sorted(c for c in cat_counts if c not in CATEGORIES)
        all_cats     = ordered_cats + extra_cats

        for idx, cat in enumerate(all_cats, start=1):
            print(f"  {GREEN}[{idx}]{RESET} {BOLD}{cat:<12}{RESET}  {GREY}{cat_counts[cat]} tools{RESET}")
        print(f"  {GREEN}[a]{RESET} All tools (flat list)")
        print(f"  {GREEN}[0]{RESET} Back")

        choice = input(f"\n  {SYM_ASK} Select category: {YELLOW}").strip().lower()
        print(RESET, end="")

        if choice == "0":
            return
        if choice == "a":
            print_tools_by_category(DEFAULT_TOOLS, "DEFAULT TOOLS — All")
            input(f"  {GREY}Press Enter to continue...{RESET}")
            continue

        try:
            cat_idx = int(choice) - 1
            if cat_idx < 0 or cat_idx >= len(all_cats):
                raise ValueError
            selected_cat = all_cats[cat_idx]
        except ValueError:
            print(f"  {SYM_ERR} {RED}Invalid selection.{RESET}")
            continue

        # ── Level 2: subcategory selection ──
        cat_tools = [t for t in DEFAULT_TOOLS if t.get("category") == selected_cat]

        # Group by subcategory
        subcat_map: dict[str, list[dict]] = {}
        for t in cat_tools:
            sub = t.get("subcategory", "General")
            subcat_map.setdefault(sub, []).append(t)

        ordered_subs = SUBCAT_ORDER.get(selected_cat, [])
        extra_subs   = sorted(s for s in subcat_map if s not in ordered_subs)
        all_subs     = [s for s in ordered_subs if s in subcat_map] + extra_subs

        while True:
            print(f"\n  {CYAN}{BOLD}{selected_cat} — Subcategories{RESET}")
            print(f"  {GREY}{'─' * 50}{RESET}")
            for idx, sub in enumerate(all_subs, start=1):
                print(f"  {GREEN}[{idx}]{RESET} {sub:<16}  {GREY}{len(subcat_map[sub])} tools{RESET}")
            print(f"  {GREEN}[a]{RESET} All in {selected_cat}")
            print(f"  {GREEN}[0]{RESET} Back")

            sub_choice = input(f"\n  {SYM_ASK} Select subcategory: {YELLOW}").strip().lower()
            print(RESET, end="")

            if sub_choice == "0":
                break
            if sub_choice == "a":
                print(f"\n  {CYAN}{BOLD}{selected_cat} — All Tools{RESET}")
                print(f"  {GREY}{'─' * 50}{RESET}")
                for sub in all_subs:
                    print(f"\n  {YELLOW}  ── {sub} ──{RESET}")
                    _paginate_tools(subcat_map[sub], sub)
                input(f"  {GREY}Press Enter to continue...{RESET}")
                continue

            try:
                sub_idx = int(sub_choice) - 1
                if sub_idx < 0 or sub_idx >= len(all_subs):
                    raise ValueError
                selected_sub = all_subs[sub_idx]
            except ValueError:
                print(f"  {SYM_ERR} {RED}Invalid selection.{RESET}")
                continue

            # ── Level 3: paginated tool list ──
            print(f"\n  {CYAN}{BOLD}{selected_cat} / {selected_sub}{RESET}")
            print(f"  {GREY}{'─' * 50}{RESET}")
            _paginate_tools(subcat_map[selected_sub], selected_sub)
            input(f"  {GREY}Press Enter to continue...{RESET}")


# ═══════════════════════════════════════════════════════════════════════════════
#  SEARCH ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def fuzzy_score(query: str, text: str) -> float:
    """Return similarity ratio between query and text."""
    return SequenceMatcher(None, query.lower(), text.lower()).ratio()


def search_tools(keyword: str) -> list[dict]:
    """Search all tools by keyword with fuzzy matching on name, description, category."""
    keyword_lower = keyword.lower()
    results: list[tuple[float, dict]] = []

    for tool in get_all_tools():
        name  = tool.get("name", "").lower()
        desc  = tool.get("description", "").lower()
        cat   = tool.get("category", "").lower()

        # Exact substring match gets highest priority
        if keyword_lower in name:
            results.append((1.0, tool))
            continue
        if keyword_lower in desc or keyword_lower in cat:
            results.append((0.8, tool))
            continue

        # Fuzzy match
        score = max(
            fuzzy_score(keyword_lower, name),
            fuzzy_score(keyword_lower, desc) * 0.7,
            fuzzy_score(keyword_lower, cat) * 0.6,
        )
        if score >= 0.4:
            results.append((score, tool))

    # Sort by score descending
    results.sort(key=lambda x: x[0], reverse=True)
    return [tool for _, tool in results]


# ═══════════════════════════════════════════════════════════════════════════════
#  COMMAND HANDLERS
# ═══════════════════════════════════════════════════════════════════════════════

def cmd_search() -> None:
    """Search tools by keyword."""
    keyword = input(f"  {SYM_ASK} Enter search keyword: {YELLOW}").strip()
    print(RESET, end="")

    if not keyword:
        print(f"  {SYM_ERR} {RED}Keyword cannot be empty.{RESET}")
        return

    results = search_tools(keyword)
    if not results:
        print(f"  {SYM_ERR} {RED}No tools matched '{keyword}'.{RESET}")
        return

    print(f"\n  {SYM_OK} {GREEN}Found {len(results)} result(s) for '{keyword}':{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")
    for tool in results:
        print_tool_line(tool)


def cmd_all_tools() -> None:
    """List all tools (default + custom)."""
    print_tools_by_category(get_all_tools(), "ALL TOOLS (Default + My)")


def cmd_default_tools() -> None:
    """Browse built-in default tools via the hierarchical browser."""
    cmd_browse_default_tools()


def cmd_my_tools() -> None:
    """List user-added tools grouped by category (and custom tags if present)."""
    my = load_my_tools()
    if not my:
        print(f"\n  {GREY}(My Tools is empty — use option 5 or 'add' to add tools){RESET}")
        return
    # Show tags alongside category if present
    print(f"\n  {CYAN}{BOLD}MY TOOLS{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")
    grouped: dict[str, list[dict]] = {}
    for t in my:
        cat = t.get("category", "Other")
        grouped.setdefault(cat, []).append(t)
    for cat in CATEGORIES + sorted(set(grouped.keys()) - set(CATEGORIES)):
        if cat not in grouped:
            continue
        print(f"\n  {YELLOW}{BOLD}  ── {cat} ({len(grouped[cat])}) ──{RESET}")
        for tool in grouped[cat]:
            name = tool.get("name", "unknown")
            desc = tool.get("description", "")
            tags = tool.get("tags", [])
            if len(desc) > 50:
                desc = desc[:47] + "..."
            tag_str = ""
            if tags:
                tag_str = f"  {GREY}#{' #'.join(tags)}{RESET}"
            print(f"  {GREEN}{name:<16}{RESET} {GREY}→{RESET} {WHITE}{desc}{RESET}{tag_str}")
    print(f"\n  {GREY}Total: {len(my)} tools{RESET}")


def cmd_add_tool() -> None:
    """Interactively add a new tool to My Tools (with optional custom tags)."""
    print(f"\n  {SYM_ACT} {CYAN}Add a new tool to your arsenal{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")

    name = input(f"  {SYM_ASK} Tool name: {YELLOW}").strip()
    print(RESET, end="")
    if not name:
        print(f"  {SYM_ERR} {RED}Name cannot be empty.{RESET}")
        return

    description = input(f"  {SYM_ASK} Description: {YELLOW}").strip()
    print(RESET, end="")
    if not description:
        print(f"  {SYM_ERR} {RED}Description cannot be empty.{RESET}")
        return

    # Category selection
    print(f"  {GREY}Categories: {', '.join(CATEGORIES)}{RESET}")
    category = input(f"  {SYM_ASK} Category (or press Enter for 'Misc'): {YELLOW}").strip()
    print(RESET, end="")
    if not category:
        category = "Misc"
    elif category not in CATEGORIES:
        # Accept as-is (user can create their own category)
        print(f"  {GREY}  Custom category '{category}' will be created.{RESET}")

    # Custom tags (optional, comma-separated)
    print(f"  {GREY}  Tags help you find tools faster in My Tools.{RESET}")
    tags_raw = input(f"  {SYM_ASK} Tags (comma-separated, optional): {YELLOW}").strip()
    print(RESET, end="")
    tags: list[str] = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    # Install commands (optional)
    print(f"  {GREY}Install commands (press Enter to skip):{RESET}")
    linux_cmd   = input(f"  {SYM_ASK} Linux install cmd:   {YELLOW}").strip()
    print(RESET, end="")
    mac_cmd     = input(f"  {SYM_ASK} macOS install cmd:   {YELLOW}").strip()
    print(RESET, end="")
    windows_cmd = input(f"  {SYM_ASK} Windows install cmd: {YELLOW}").strip()
    print(RESET, end="")

    note = input(f"  {SYM_ASK} Note (optional): {YELLOW}").strip()
    print(RESET, end="")

    new_tool = {
        "name": name,
        "description": description,
        "category": category,
        "tags": tags,
        "install": {
            "linux": linux_cmd,
            "mac": mac_cmd,
            "windows": windows_cmd,
        },
        "note": note,
    }

    my_tools = load_my_tools()

    # Check for duplicate
    if any(t["name"].lower() == name.lower() for t in my_tools):
        print(f"  {SYM_ERR} {RED}Tool '{name}' already exists in My Tools.{RESET}")
        return

    my_tools.append(new_tool)
    save_my_tools(my_tools)
    tag_display = f"  Tags: {', '.join('#' + t for t in tags)}" if tags else ""
    print(f"  {SYM_OK} {GREEN}Tool '{name}' added to your arsenal!{RESET}{GREY}{tag_display}{RESET}")


def cmd_install() -> None:
    """Install a tool by name (detects OS, confirms, runs via subprocess)."""
    tool_name = input(f"  {SYM_ASK} Enter tool name to install: {YELLOW}").strip()
    print(RESET, end="")

    if not tool_name:
        print(f"  {SYM_ERR} {RED}Tool name cannot be empty.{RESET}")
        return

    # Find the tool
    all_tools = get_all_tools()
    match = None
    for t in all_tools:
        if t["name"].lower() == tool_name.lower():
            match = t
            break

    if not match:
        print(f"  {SYM_ERR} {RED}Tool '{tool_name}' not found.{RESET}")
        return

    current_os = detect_os()
    install_cmds = match.get("install", {})
    cmd = install_cmds.get(current_os, "")

    if not cmd:
        print(f"  {SYM_ERR} {RED}No install command for {current_os}.{RESET}")
        return

    print(f"\n  {SYM_ACT} {CYAN}Tool:{RESET}    {WHITE}{match['name']}{RESET}")
    print(f"  {SYM_ACT} {CYAN}OS:{RESET}      {WHITE}{current_os}{RESET}")
    print(f"  {SYM_ACT} {CYAN}Command:{RESET} {WHITE}{cmd}{RESET}")

    if match.get("note"):
        print(f"  {SYM_ACT} {GREY}Note: {match['note']}{RESET}")

    confirm = input(f"\n  {SYM_ASK} Execute install? (y/n): {YELLOW}").strip().lower()
    print(RESET, end="")

    if confirm != "y":
        print(f"  {SYM_ERR} {RED}Install cancelled.{RESET}")
        return

    print(f"\n  {SYM_ACT} {CYAN}Running...{RESET}\n")
    try:
        subprocess.run(cmd, shell=True, check=False)
        print(f"\n  {SYM_OK} {GREEN}Install command executed.{RESET}")
    except Exception as e:
        print(f"\n  {SYM_ERR} {RED}Install failed: {e}{RESET}")


def cmd_import_export() -> None:
    """Import or export My Tools."""
    print(f"\n  {CYAN}{BOLD}Import / Export{RESET}")
    print(f"  {GREY}{'─' * 50}{RESET}")
    print(f"  {GREEN}[1]{RESET} Export My Tools to JSON")
    print(f"  {GREEN}[2]{RESET} Import tools from JSON")

    choice = input(f"\n  {SYM_ASK} Select (1/2): {YELLOW}").strip()
    print(RESET, end="")

    if choice == "1":
        _export_tools()
    elif choice == "2":
        _import_tools()
    else:
        print(f"  {SYM_ERR} {RED}Invalid choice.{RESET}")


def _export_tools() -> None:
    """Export My Tools to a specified JSON file."""
    my_tools = load_my_tools()
    if not my_tools:
        print(f"  {SYM_ERR} {RED}No custom tools to export.{RESET}")
        return

    filepath = input(f"  {SYM_ASK} Export file path (e.g. export.json): {YELLOW}").strip()
    print(RESET, end="")

    if not filepath:
        print(f"  {SYM_ERR} {RED}File path cannot be empty.{RESET}")
        return

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(my_tools, f, indent=2, ensure_ascii=False)
        print(f"  {SYM_OK} {GREEN}Exported {len(my_tools)} tool(s) to '{filepath}'.{RESET}")
    except IOError as e:
        print(f"  {SYM_ERR} {RED}Export failed: {e}{RESET}")


def _import_tools() -> None:
    """Import tools from a JSON file, validate, skip duplicates."""
    filepath = input(f"  {SYM_ASK} Import file path: {YELLOW}").strip()
    print(RESET, end="")

    if not filepath:
        print(f"  {SYM_ERR} {RED}File path cannot be empty.{RESET}")
        return

    if not os.path.isfile(filepath):
        print(f"  {SYM_ERR} {RED}File not found: '{filepath}'.{RESET}")
        return

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"  {SYM_ERR} {RED}Failed to read JSON: {e}{RESET}")
        return

    if not isinstance(data, list):
        print(f"  {SYM_ERR} {RED}JSON must be a list of tool objects.{RESET}")
        return

    my_tools = load_my_tools()
    existing_names = {t["name"].lower() for t in my_tools}
    required_keys = {"name", "description", "category"}

    added = 0
    skipped = 0

    for item in data:
        if not isinstance(item, dict):
            skipped += 1
            continue
        if not required_keys.issubset(item.keys()):
            skipped += 1
            continue
        if item["name"].lower() in existing_names:
            print(f"  {GREY}  Skipped duplicate: {item['name']}{RESET}")
            skipped += 1
            continue

        # Ensure install dict exists
        if "install" not in item or not isinstance(item["install"], dict):
            item["install"] = {"linux": "", "mac": "", "windows": ""}
        if "note" not in item:
            item["note"] = ""

        my_tools.append(item)
        existing_names.add(item["name"].lower())
        added += 1

    save_my_tools(my_tools)
    print(f"  {SYM_OK} {GREEN}Imported {added} tool(s), skipped {skipped}.{RESET}")


def cmd_help() -> None:
    """Display the ArsenalX help screen."""
    print(f"""
  {CYAN}{BOLD}╔══════════════════════════════════════════════════════════╗{RESET}
  {CYAN}{BOLD}║  ArsenalX — Help & Reference                            ║{RESET}
  {CYAN}{BOLD}╚══════════════════════════════════════════════════════════╝{RESET}

  {YELLOW}{BOLD}PURPOSE{RESET}
    ArsenalX is a hacker-themed CLI arsenal manager.
    Store, search, browse, and install 100+ ethical hacking
    tools — organized by category and subcategory.

  {YELLOW}{BOLD}MENU SHORTCUTS{RESET}
    {GREEN}[1]{RESET} Search Tools      — fuzzy keyword search across all tools
    {GREEN}[2]{RESET} All Tools         — full list grouped by category
    {GREEN}[3]{RESET} Default Tools     — browse the 100+ built-in tools
                           (Category → Subcategory → Tools)
    {GREEN}[4]{RESET} My Tools          — view custom tools you have added
    {GREEN}[5]{RESET} Add Tool          — add a tool with optional custom tags
    {GREEN}[6]{RESET} Install Tool      — run the OS-specific install command
    {GREEN}[7]{RESET} Import / Export   — share tool collections as JSON files
    {GREEN}[0]{RESET} Exit

  {YELLOW}{BOLD}INLINE COMMANDS{RESET}
    {GREEN}search <keyword>{RESET}   — e.g.  search nmap
    {GREEN}install <tool>{RESET}    — e.g.  install sqlmap
    {GREEN}add{RESET}               — interactive add wizard
    {GREEN}list{RESET}              — list all tools (flat)
    {GREEN}import <file>{RESET}     — e.g.  import backup.json
    {GREEN}export <file>{RESET}     — e.g.  export mytools.json
    {GREEN}help{RESET}              — show this screen
    {GREEN}exit{RESET}              — quit ArsenalX

  {YELLOW}{BOLD}BEGINNER WORKFLOW{RESET}
    1. Type {GREEN}3{RESET} to browse Default Tools by category.
    2. Navigate to a subcategory (e.g. Recon → Subdomain).
    3. Note a tool name, then type {GREEN}install <tool>{RESET} to install it.
    4. Use {GREEN}add{RESET} to save your own tools with custom tags.
    5. Use {GREEN}search{RESET} any time to find tools fast.

  {YELLOW}{BOLD}COMMAND EXAMPLES{RESET}
    arsenalx> search sql            (find SQL-related tools)
    arsenalx> search wireless       (find Wi-Fi attack tools)
    arsenalx> install nmap          (install nmap for your OS)
    arsenalx> install nuclei        (install nuclei scanner)
    arsenalx> add                   (add a custom tool)
    arsenalx> export backup.json    (backup My Tools)
    arsenalx> import backup.json    (restore from backup)

  {YELLOW}{BOLD}TOOL FORMAT (tools.json){RESET}
    {{"name": "mytool", "description": "...", "category": "Misc",
      "tags": ["ctf", "web"],
      "install": {{"linux": "...", "mac": "...", "windows": "..."}},
      "note": ""}}

  {GREY}Documentation: See README.md for full details.{RESET}
""")


def cmd_exit() -> None:
    """Exit the CLI."""
    print(f"\n  {SYM_ACT} {CYAN}Exiting ArsenalX... Stay sharp. ⚔️{RESET}\n")
    sys.exit(0)


# ═══════════════════════════════════════════════════════════════════════════════
#  INLINE COMMAND PARSER
# ═══════════════════════════════════════════════════════════════════════════════

def handle_inline_command(raw: str) -> bool:
    """
    Handle typed commands like 'search nmap', 'install sqlmap', etc.
    Returns True if a command was matched, False otherwise.
    """
    parts = raw.strip().split(maxsplit=1)
    if not parts:
        return False

    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "search" and arg:
        results = search_tools(arg)
        if not results:
            print(f"  {SYM_ERR} {RED}No tools matched '{arg}'.{RESET}")
        else:
            print(f"\n  {SYM_OK} {GREEN}Found {len(results)} result(s) for '{arg}':{RESET}")
            print(f"  {GREY}{'─' * 50}{RESET}")
            for tool in results:
                print_tool_line(tool)
        return True

    if cmd == "add":
        cmd_add_tool()
        return True

    if cmd == "list":
        cmd_all_tools()
        return True

    if cmd == "install" and arg:
        # Direct install by name
        all_tools = get_all_tools()
        match = None
        for t in all_tools:
            if t["name"].lower() == arg.lower():
                match = t
                break
        if not match:
            print(f"  {SYM_ERR} {RED}Tool '{arg}' not found.{RESET}")
        else:
            current_os = detect_os()
            install_cmd = match.get("install", {}).get(current_os, "")
            if not install_cmd:
                print(f"  {SYM_ERR} {RED}No install command for {current_os}.{RESET}")
            else:
                print(f"\n  {SYM_ACT} {CYAN}Tool:{RESET}    {WHITE}{match['name']}{RESET}")
                print(f"  {SYM_ACT} {CYAN}OS:{RESET}      {WHITE}{current_os}{RESET}")
                print(f"  {SYM_ACT} {CYAN}Command:{RESET} {WHITE}{install_cmd}{RESET}")
                if match.get("note"):
                    print(f"  {SYM_ACT} {GREY}Note: {match['note']}{RESET}")
                confirm = input(f"\n  {SYM_ASK} Execute install? (y/n): {YELLOW}").strip().lower()
                print(RESET, end="")
                if confirm == "y":
                    print(f"\n  {SYM_ACT} {CYAN}Running...{RESET}\n")
                    try:
                        subprocess.run(install_cmd, shell=True, check=False)
                        print(f"\n  {SYM_OK} {GREEN}Install command executed.{RESET}")
                    except Exception as e:
                        print(f"\n  {SYM_ERR} {RED}Install failed: {e}{RESET}")
                else:
                    print(f"  {SYM_ERR} {RED}Install cancelled.{RESET}")
        return True

    if cmd == "import" and arg:
        # Treat arg as filepath
        if not os.path.isfile(arg):
            print(f"  {SYM_ERR} {RED}File not found: '{arg}'.{RESET}")
            return True
        try:
            with open(arg, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"  {SYM_ERR} {RED}Failed to read JSON: {e}{RESET}")
            return True
        if not isinstance(data, list):
            print(f"  {SYM_ERR} {RED}JSON must be a list of tool objects.{RESET}")
            return True
        my_tools = load_my_tools()
        existing_names = {t["name"].lower() for t in my_tools}
        required_keys = {"name", "description", "category"}
        added = 0
        for item in data:
            if not isinstance(item, dict) or not required_keys.issubset(item.keys()):
                continue
            if item["name"].lower() in existing_names:
                continue
            if "install" not in item or not isinstance(item["install"], dict):
                item["install"] = {"linux": "", "mac": "", "windows": ""}
            if "note" not in item:
                item["note"] = ""
            my_tools.append(item)
            existing_names.add(item["name"].lower())
            added += 1
        save_my_tools(my_tools)
        print(f"  {SYM_OK} {GREEN}Imported {added} tool(s) from '{arg}'.{RESET}")
        return True

    if cmd == "export" and arg:
        my_tools = load_my_tools()
        if not my_tools:
            print(f"  {SYM_ERR} {RED}No custom tools to export.{RESET}")
            return True
        try:
            with open(arg, "w", encoding="utf-8") as f:
                json.dump(my_tools, f, indent=2, ensure_ascii=False)
            print(f"  {SYM_OK} {GREEN}Exported {len(my_tools)} tool(s) to '{arg}'.{RESET}")
        except IOError as e:
            print(f"  {SYM_ERR} {RED}Export failed: {e}{RESET}")
        return True

    if cmd in ("help", "?"):
        cmd_help()
        return True

    if cmd == "exit":
        cmd_exit()
        return True

    return False


# ═══════════════════════════════════════════════════════════════════════════════
#  MENU DISPATCHER
# ═══════════════════════════════════════════════════════════════════════════════

MENU_DISPATCH = {
    "1": cmd_search,
    "2": cmd_all_tools,
    "3": cmd_default_tools,
    "4": cmd_my_tools,
    "5": cmd_add_tool,
    "6": cmd_install,
    "7": cmd_import_export,
    "8": cmd_help,
    "0": cmd_exit,
}


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN LOOP
# ═══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    clear_screen()
    print_banner()
    print_header()
    print_footer()

    while True:
        try:
            print_menu()
            raw = input(f"  {GREEN}{BOLD}arsenalx>{RESET} {YELLOW}").strip()
            print(RESET, end="")

            if not raw:
                continue

            # Try inline commands first
            if handle_inline_command(raw):
                continue

            # Then try menu numbers
            handler = MENU_DISPATCH.get(raw)
            if handler:
                handler()
            else:
                print(f"  {SYM_ERR} {RED}Unknown command. Use menu numbers or type a command.{RESET}")
                print(f"  {GREY}  Commands: search <kw>, install <tool>, add, list, import <file>, export <file>, help, exit{RESET}")

        except KeyboardInterrupt:
            print(f"\n\n  {SYM_ACT} {CYAN}Caught interrupt. Exiting ArsenalX... Stay sharp. ⚔️{RESET}\n")
            sys.exit(0)
        except EOFError:
            cmd_exit()
        except Exception as e:
            print(f"  {SYM_ERR} {RED}Unexpected error: {e}{RESET}")


if __name__ == "__main__":
    main()
