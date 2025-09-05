import requests
import sys
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def check_status_code(status_code__, full_url):
    if status_code__ == 200:
        return f"{Fore.GREEN}[+] Found directory: {Style.RESET_ALL} {full_url}"
    elif status_code__ == 404:
        return None
    elif status_code__ == 301 or status_code__ == 302:
        return f"{Fore.YELLOW}[+] Redirection: {Style.RESET_ALL} {full_url}"
    elif status_code__ == 403:
        return f"{Fore.YELLOW}[+] Access denied: {Style.RESET_ALL} {full_url}"
    
def main():
    parser = argparse.ArgumentParser(description="Simple brutforce directories and files")
    parser.add_argument("target_url", help="Target URL (Example, http://192.168.1.14)")
    parser.add_argument("wordlist", help="Path to file with word list")
    
    args = parser.parse_args()
    
    target_url = args.target_url
    wordlist_path = args.wordlist
    print(f"\n--- START SCANNING TARGET: {target_url} ---\n")
    try:
        with open(wordlist_path, "r") as f:
            for target_dir in f:
                target_dir = target_dir.strip()
                if not target_dir or target_dir.startswith('#'):
                    continue
                full_url = f'{target_url}/{target_dir}'
                try:
                    response = requests.get(full_url)
                    result_message = check_status_code(response.status_code, full_url)
                    if result_message:
                        print(result_message)
                except requests.exceptions.RequestException as e:
                    pass
                
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: Dictionary file not found at path: {wordlist_path}")
        sys.exit(1)
    print(f"\n--- SCANNING COMPLETED ---\n")
    
if __name__ == "__main__":
    main()