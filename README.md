# Hackathon-Projects
This is a compilation of whatever projects we might work on in the future.

Web Phisher:
Web Phisher or Web Phish is an online application we are developing that is used to verify and authenticate URLs that are shared and received in emails, messages, websites, etc. 
It is a program primarily developed to curb the spread of phishing by providing its users a simple way of detecting suspicious and fraudulent links.

It does this by running it through a series of pre-determined checks and tests and scoring it based on how well it passes these tests. it then generates a trustworthiness scale which give the user a measure of how trustworthy this url is and helps them stay safe. 

Here is a detailed and formal summary of my work.

## Web Phisher

### Overview

**Web Phisher** is a Python-based command-line tool for detecting potentially phishing URLs. It leverages a combination of heuristic rules, domain reputation data, suspicious pattern matching, and WHOIS domain age analysis to determine the authenticity of a given website link. This tool is designed for prototyping, experimentation, and educational purposes, helping users better understand basic phishing detection mechanisms.

**Key Features:**
- Compares input URLs against a curated list of authentic websites and a dynamically maintained blacklist.
- Analyzes URL structure (prefix, TLD, use of IP addresses, path length, suspicious/random characters).
- Matches suspicious terms in URLs commonly used in phishing attacks.
- Checks domain age using WHOIS information.
- Assigns a trust ranking and a numerical score out of 4.0 to each URL.

---

### Challenges Encountered

- **Data Collection & Curation:** Assembling comprehensive lists of authentic websites, suspicious patterns, and categorizing TLDs required significant manual effort and is inherently incomplete.
- **WHOIS Data Variability:** WHOIS lookups can be slow, fail, or return inconsistent structures depending on the domain registrar.
- **Heuristic Tuning:** Balancing the weights and thresholds for various checks to minimize false positives and negatives is challenging and often requires iterative real-world testing.
- **Handling Obfuscated URLs:** Detecting advanced obfuscation and redirection techniques (such as URL shorteners or encoded characters) is non-trivial and not fully addressed in the current version.
- **User Input Validation:** Ensuring the tool robustly handles malformed or unusual URLs while providing clear feedback.

---

### Limitations

- **Static Lists:** The list of authentic websites and suspicious patterns is hardcoded and may quickly become outdated or incomplete.
- **No Machine Learning:** The current version relies on simple heuristics and does not use any learning or adaptive mechanisms.
- **Limited Language and Internationalization Support:** The tool primarily targets English-language and major global domains, missing localized phishing tactics.
- **Performance:** Multiple checks (e.g., WHOIS) can slow down analysis, especially when running in batches or on unreliable connections.
- **No Browser/Network Integration:** This is a standalone CLI tool; it does not integrate with browsers, proxies, or email gateways for real-time protection.
- **Primitive Blacklist:** Blacklisting is per-session and not persisted or shared across runs/users.
- **Possible False Positives/Negatives:** Due to its heuristic nature, some legitimate URLs may be flagged as sketchy, and some phishing attempts may evade detection.

---

### Scalability Options

#### Short-term

- **Modularize Code:** Break out core logic into reusable modules and add unit tests for easier maintenance and extension.
- **Configurable Lists:** Move authentic websites, suspicious patterns, and TLD lists to external files or allow user customization.
- **Batch Processing:** Allow the tool to scan lists of URLs at once rather than single URL input.
- **Logging & Reporting:** Add structured output (e.g., JSON/CSV) and detailed logging for further analysis.

#### Long-term

- **Machine Learning Integration:** Train models on labeled phishing/benign datasets to improve accuracy and adaptability.
- **Live Threat Intelligence:** Integrate with public threat feeds or APIs to update blacklists and patterns dynamically.
- **Cross-Platform Integration:** Develop browser extensions, email plugins, or REST APIs for real-time phishing detection.
- **Distributed Blacklisting:** Implement persistent and shared blacklists using a database or cloud storage.
- **Internationalization:** Support detection of phishing in other languages and localized domain patterns.
- **Community Contribution:** Allow users to submit suspicious URLs and patterns to improve collective intelligence.

---

**Note:**  
This tool is for educational and prototyping purposes only. It should not be relied upon as a sole defense against phishing in production environments.

---
