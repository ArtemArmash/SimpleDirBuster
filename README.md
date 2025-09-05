# SimpleDirBuster - A Lightweight Directory & File Bruteforcer

SimpleDirBuster is a simple, fast, and customizable tool written in Python for discovering hidden directories and files on a web server. It's designed for educational purposes and penetration testing exercises on systems where you have explicit authorization.

This tool was created to understand the core mechanics of web content discovery tools like DirBuster and Dirb.

## Features

-   **Fast & Simple:** Scans for directories and files using a provided wordlist.
-   **User-Friendly:** Takes target URL and wordlist path as command-line arguments.
-   **Intelligent Analysis:** Correctly interprets common HTTP status codes (200, 403, 301/302).
-   **Colored Output:** Uses `colorama` for clear and readable results.
-   **Robust:** Handles connection errors and bad file paths gracefully.
-   **Clean Wordlists:** Ignores empty lines and comments (`#`) in wordlists.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-github-username/SimpleDirBuster.git
    cd SimpleDirBuster
    ```
    *(Не забудь изменить `your-github-username/SimpleDirBuster` на твой реальный путь на GitHub)*

2.  **It's highly recommended to use a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, providing the target URL (including `http://` or `https://`) and the path to your wordlist.

**Syntax:**
```bash
python3 bruteforcer.py <TARGET_URL> <WORDLIST_PATH>
```

**Example:**
Scanning a local Metasploitable 2 machine using a common wordlist found in Kali Linux.
```bash
python3 bruteforcer.py http://192.168.1.14 /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
```

### Example Output

```
--- START SCANNING TARGET: http://192.168.1.14 ---

[+] Found directory: http://192.168.1.14/test
[!] Access denied: http://192.168.1.14/server-status
[+] Found directory: http://192.168.1.14/phpinfo.php

--- SCANNING COMPLETED ---
```

## Disclaimer

⚠️ **This tool is for educational and authorized testing purposes ONLY.** Unauthorized scanning of websites is illegal and unethical. Ensure you have explicit, written permission from the system owner before using this tool on any target. The author is not responsible for any misuse or damage caused by this script.
```
