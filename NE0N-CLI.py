#
'''
greatest group chat messages quotes of all time:

orderize: SIXX SEEEVEENN LIILEOFIOLO
opa433: bro tf you on about vro???
orderize: SIXX SEEVVENRN lolo9loOLol :))))))))))))))))))))
funky2341121: ight thats all i need to hear -_-

'''


import sys
import os
import time
import random
import datetime
import hashlib
import subprocess
from typing import List

# Initialize colorama properly
try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=False)
    COLORAMA_AVAILABLE = True
except ImportError:
    class _NoColor:
        def __getattr__(self, name):
            return ''
    Fore = Style = _NoColor()
    COLORAMA_AVAILABLE = False

# Config
APP_NAME = "NEON-CLI"
VERSION = "0.9"

# nmapscan configuration
FAKEIP_DURATION = 17.0
FAKEIP_MIN_DELAY = 0.0
FAKEIP_MAX_DELAY = 0.4
FAKEIP_INITIAL_WAIT_MIN = 6.0
FAKEIP_INITIAL_WAIT_MAX = 7.0 # SIX SEEVVEENNN LOloLlo)llOLlOlLo0

# orderize bro wtf

# datacracker configuration
DATACRACK_TICK = 0.05
DATACRACK_GLYPH_SET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{};:,.<>/?"
)

# Password database (editable)
PASSWORD_DATABASE = [
    "Tr0ub4dor&3",
    "P@ssw0rd123!",
    "Sup3rS3cr3t#",
    "H4ck3rM@n99",
    "N30nCyb3r!",
    "Qu4ntumL0ck$",
    "D@t4Br34ch7",
    "Encrypti0n#1",
    "F1r3w@ll2024",
    "Blu3T34m!42"
]

# Utility helpers
def compute_file_hash(path: str) -> str:
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""

SCRIPT_PATH = None
try:
    SCRIPT_PATH = os.path.abspath(__file__)
except NameError:
    SCRIPT_PATH = None

INITIAL_HASH = None
INITIAL_MTIME = None
if SCRIPT_PATH and os.path.isfile(SCRIPT_PATH):
    INITIAL_HASH = compute_file_hash(SCRIPT_PATH)
    try:
        INITIAL_MTIME = os.path.getmtime(SCRIPT_PATH)
    except Exception:
        INITIAL_MTIME = None

def now_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_ip() -> str:
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Animation & Display Helpers
def slow_print(s, delay=0.01, newline=True):
    """Print characters slowly for effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def spinner(duration=1.2, prefix=''):
    """Show a spinning animation."""
    chars = ['|', '/', '-', '\\']
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f'\r{prefix} {Fore.WHITE}{chars[i % len(chars)]}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(prefix) + 4) + '\r')
    sys.stdout.flush()

def progress_bar(total=20, prefix='Progress'):
    """Display a progress bar animation."""
    for i in range(total + 1):
        pct = int(i / total * 100)
        bar = ('#' * i).ljust(total)
        sys.stdout.write(f'\r{Fore.CYAN} [{bar}] {pct}%{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(random.uniform(0.0, 3.0))
    sys.stdout.write('\n')
    sys.stdout.flush()

# Simulated Attack Data
ATTACK_TYPES = {
    'scan': "Service & port scan",
    'sql_injection': "SQL Injection",
    'xss': "Cross-Site Scripting",
    'csrf': "CSRF attempt",
    'rce': "Remote Code Execution",
    'brute_force': "Authentication brute-force",
    'ddos': "Distributed denial-of-service",
    'recon': "Reconnaissance & fingerprinting"
}

SIMULATED_VULNS = [
    "Potential SQL injection in query parameter 'id'",
    "Reflected XSS in search parameter 'q'",
    "Missing CSRF token on form /login",
    "Outdated server version: header suggests EOL release",
    "Directory listing enabled on /uploads/",
    "Insecure cookie flags not set (HttpOnly missing)",
    "Verbose error page revealing stack traces",
    "Weak password policy detected"
]

SIMULATED_RESPONSES = [
    "200 OK [len=1024]",
    "500 Internal Server Error [len=2048]",
    "404 Not Found",
    "302 Found -> /login",
    "401 Unauthorized",
    "403 Forbidden"
]

# Simulated Attack Functions
def simulate_network_activity(url, lines=6):
    """Simulate HTTP requests with responses."""
    for i in range(lines):
        path = random.choice(['/', '/login', '/search', '/api/v1/items', '/upload', '/admin', '/wp-login.php'])
        method = random.choice(['GET', 'POST', 'HEAD', 'OPTIONS'])
        resp = random.choice(SIMULATED_RESPONSES)
        slow_print(f'{Fore.YELLOW}> {method} {url}{path} HTTP/1.1  -- {resp}{Style.RESET_ALL}', delay=0.002)
        time.sleep(random.uniform(0.05, 0.20))

def simulate_attack(url, attack_type):
    """Perform a purely cosmetic simulated attack run with colored output."""
    header = f"{Fore.GREEN}{Style.BRIGHT}=== Simulating {ATTACK_TYPES.get(attack_type, attack_type)} against {url} ==={Style.RESET_ALL}"
    print(header)
    
    spinner(0.8, prefix=f'{Fore.CYAN}Initializing{Style.RESET_ALL}')
    slow_print(f'{Fore.CYAN}Resolving target...{Style.RESET_ALL}', delay=0.004)
    spinner(0.6, prefix=f'{Fore.CYAN}Querying DNS{Style.RESET_ALL}')
    slow_print(f'{Fore.CYAN}Collecting headers...{Style.RESET_ALL}', delay=0.004)
    simulate_network_activity(url, lines=random.randint(3, 6))

    found = random.choices(SIMULATED_VULNS, k=random.randint(0, 3))
    if not found:
        slow_print(f'\n{Fore.WHITE}No obvious issues discovered during this run.{Style.RESET_ALL}\n')
    else:
        slow_print(f'\n{Fore.MAGENTA}Findings:{Style.RESET_ALL}')
        for v in found:
            severity = random.choice(['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
            sev_color = {'LOW': Fore.GREEN, 'MEDIUM': Fore.YELLOW, 'HIGH': Fore.MAGENTA, 'CRITICAL': Fore.RED}.get(severity, Fore.WHITE)
            slow_print(f'{sev_color} - {v} [severity: {severity}]{Style.RESET_ALL}')
            time.sleep(0.14)

    slow_print(f'\n{Fore.CYAN}Attempting exploitation sequence...{Style.RESET_ALL}', delay=0.006)
    progress_bar(prefix=f'{Fore.MAGENTA}Exploit progress{Style.RESET_ALL}')
    
    outcome = random.choices(['SUCCESS', 'PARTIAL', 'FAILED'], weights=[0.2, 0.3, 0.5])[0]
    if outcome == 'SUCCESS':
        slow_print(f'\n{Fore.GREEN}Exploit was successful! (simulated){Style.RESET_ALL}')
    elif outcome == 'PARTIAL':
        slow_print(f'\n{Fore.YELLOW}Exploit partially successful. Gained limited info.{Style.RESET_ALL}')
    else:
        slow_print(f'\n{Fore.RED}Exploit failed. Target appears resilient.{Style.RESET_ALL}')

# Command Functions
def cmd_sim(args):
    """Run a simulated attack. Usage: sim <type> <url>"""
    if not args or len(args) < 2:
        print(f'{Fore.YELLOW}Usage: sim <type> <url>{Style.RESET_ALL}')
        return
    atype = args[0]
    url = args[1]
    if atype not in ATTACK_TYPES:
        print(f'{Fore.YELLOW}Unknown attack type \'{atype}\'. Available: {", ".join(ATTACK_TYPES.keys())}{Style.RESET_ALL}')
        return
    simulate_attack(url, atype)

def cmd_demo(args):
    """Quick demo: prompts for URL and runs a 'scan' simulation."""
    if args:
        url = args[0]
    else:
        try:
            url = input(f'{Fore.CYAN}Enter URL to scan (e.g. http://example.com): {Style.RESET_ALL}').strip()
        except (KeyboardInterrupt, EOFError):
            print(f'\n{Fore.YELLOW}Scan cancelled.{Style.RESET_ALL}')
            return
    if not url:
        print(f'{Fore.YELLOW}No URL provided.{Style.RESET_ALL}')
        return
    simulate_attack(url, 'scan')

def print_banner():
    """Display the startup banner."""
    meta = f"{Style.DIM}{Fore.YELLOW}{APP_NAME} {VERSION} - {now_str()}{Style.RESET_ALL}"
    print()
    print(meta)
    print(f"{Fore.GREEN}NE0N-CLI, a powerful command with data cracking and IP scanning capabilities{Style.RESET_ALL}\n")



def show_help():
    """Display available commands."""
    print(f"{Fore.YELLOW}Credits:{Style.RESET_ALL}")
    cmds = [
        ("@orderize", "main dev and backend coding"),
        ("@Tescent", "professional code and syntax reviewer and API development"),
        ("@opa334", "some more backend coding"),
        ("@alessiioooo", "gui and interface coding"),
        ("@sosensantionall", "beta tester"),
        ("@funky2341121", "beta tester"),
    ]
    for cmd, desc in cmds:
        print(f"  {Fore.CYAN}{cmd:<28} {desc}{Style.RESET_ALL}")
    print()

def cmd_time():
    """Display current time."""
    print(f"{Fore.GREEN}{now_str()}{Style.RESET_ALL}")

def cmd_injecttoip(args=None):
    spinner(11.0, prefix=f'{Style.DIM}[msfinject] loading msfinject module.{Style.RESET_ALL}')
    spinner(3.0, prefix=f'{Style.DIM}[msfinject] loading pynumerator. (dialect of python enumerator){Style.RESET_ALL}')
    spinner(2.0, prefix=f'{Style.DIM}[msfinject] loading pyhash.{Style.RESET_ALL}')
    spinner(2.0, prefix=f'{Style.DIM}[msfinject] verifing tokenid.{Style.RESET_ALL}')
    spinner(1.0, prefix=f'{Style.DIM}[msfinject] finalizing.{Style.RESET_ALL}')
    iptoinject = input(f'{Fore.MAGENTA}[msfinject] Enter the victim machine ip address: {Style.RESET_ALL}')
    hfixer6 = f"{Fore.CYAN}Targeting:{Style.RESET_ALL} {Fore.YELLOW}{iptoinject}{Style.RESET_ALL}"
    print(hfixer6)
    spinner(15.0, prefix=f'{Fore.CYAN}[msfinject] Initializing NE0N injection via msfinject.{Style.RESET_ALL}')
    hfixer4 = f"{Fore.CYAN}[msfinject] Initializing NE0N injection via msfinject.{Style.RESET_ALL}"
    print(hfixer4)
    spinner(6.0, prefix=f'{Fore.CYAN}[msfinject] Connecting to machine with brute force method.{Style.RESET_ALL}')
    hfixer7 = f"{Fore.CYAN}[msfinject] Connecting to machine with brute force method.{Style.RESET_ALL}"
    print(hfixer7) 
    hfixer8 = f"{Fore.CYAN}[msfinject] successfully connected to machine on open port{Style.RESET_ALL} {Fore.YELLOW}{iptoinject}{Style.RESET_ALL}"
    print(hfixer8)
    progress_bar(prefix=f'{Fore.CYAN}[msfinject] requesting data:{Style.RESET_ALL}')  
    spinner(15.0, prefix=f'{Fore.CYAN}[msfinject] trying to bypass anti-payload.{Style.RESET_ALL}')
    hfixer9 = f"{Fore.CYAN}[msfinject] trying to bypass anti-payload.{Style.RESET_ALL}"
    print(hfixer9)
    hfixer5 = f"{Fore.CYAN}[msfinject] ip address has been successfully infected by NE0N and commands will now work!{Style.RESET_ALL}"
    print(hfixer5)

def cmd_echo(args: List[str]):
    """Echo the provided arguments."""
    print(" ".join(args))

def cmd_reverse(args: List[str]):
    """Reverse the provided text."""
    print("".join(args)[::-1])

def _animated_finding(remaining_wait: float):
    """Show animated 'Scanning IPs' message."""
    label = f"{Fore.YELLOW}Scanning for IPs on target port{Style.RESET_ALL}"
    dot_color = f"{Style.DIM}{Fore.WHITE}"
    
    start = time.time()
    dot_index = 0
    try:
        while True:
            elapsed = time.time() - start
            if elapsed >= remaining_wait:
                break
            dots = "." * (dot_index % 4)
            print(f"\r{label}{dot_color}{dots}{Style.RESET_ALL} ", end="", flush=True)
            dot_index += 1
            time.sleep(0.8)
    except KeyboardInterrupt:
        print()
        raise
    print()

def cmd_fakeip():
    """Generate fake IP addresses at random intervals."""
    try:
        data = input(f"{Fore.MAGENTA}Enter the target machine's (target) port: {Style.RESET_ALL}")
    except (KeyboardInterrupt, EOFError):
        print()
        return

    spinner(7.0, prefix=f'{Fore.CYAN}[nmap] executing nmap against port:{Style.RESET_ALL} {Fore.YELLOW}{data}{Style.RESET_ALL}')
    hfixer = f"{Fore.CYAN}[nmap] executing nmap against port:{Style.RESET_ALL} {Fore.YELLOW}{data}{Style.RESET_ALL}"
    print(hfixer)
    time.sleep(0.2)
    spinner(5.0, prefix=f'{Fore.CYAN}[nmap]{Style.RESET_ALL} {Fore.RED}could not find port {data} in zshdylib. Resorting to pyhash.{Style.RESET_ALL}')
    hfixer2 = f"{Fore.CYAN}[nmap]{Style.RESET_ALL} {Fore.RED}could not find port {data} in zshdylib. Resorting to pyhash.{Style.RESET_ALL}"
    print(hfixer2)
    hfixer3 = f"{Fore.CYAN}[nmap] established nmap server:{Style.RESET_ALL} {Fore.YELLOW}120::4076525-98409-24985{Style.RESET_ALL}\n"
    print(hfixer3)

    start_time = time.time()
    end_time = start_time + FAKEIP_DURATION

    initial_wait = random.uniform(FAKEIP_INITIAL_WAIT_MIN, FAKEIP_INITIAL_WAIT_MAX)
    remaining_total = end_time - time.time()
    initial_wait = min(initial_wait, max(0.0, remaining_total))

    if initial_wait > 0:
        try:
            _animated_finding(initial_wait)
            print()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Generation interrupted by user.{Style.RESET_ALL}")
            return

    count = 0

    try:
        while True:
            now = time.time()
            if now >= end_time:
                break

            ip = generate_random_ip()
            ip_str = f"{Fore.CYAN}[nmap]{Style.RESET_ALL} {Fore.GREEN}{ip}{Style.RESET_ALL} {Style.DIM}found{Style.RESET_ALL}"
            print(ip_str)
            count += 1

            remaining = end_time - time.time()
            if remaining <= 0:
                break
            sleep_time = random.uniform(FAKEIP_MIN_DELAY, FAKEIP_MAX_DELAY)
            if sleep_time > remaining:
                time.sleep(remaining)
                break
            else:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Scanning interrupted by user.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.YELLOW}Done. {count} IP(s) found.{Style.RESET_ALL}")

def cmd_datacracker():
    """Animated password 'cracking' simulation with 2-row table format."""
    try:
        username = input(f"{Fore.MAGENTA}Enter target username: {Style.RESET_ALL}").strip()
        if not username:
            print(f"{Fore.YELLOW}No username provided.{Style.RESET_ALL}")
            return
            
        website_url = input(f"{Fore.MAGENTA}Enter website URL: {Style.RESET_ALL}").strip()
        if not website_url:
            print(f"{Fore.YELLOW}No URL provided.{Style.RESET_ALL}")
            return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    # Select a random password from the database
    target_password = random.choice(PASSWORD_DATABASE)
    password_length = len(target_password)
    
    # Initialize display
    print(f"\n{Fore.YELLOW}Connecting to {website_url}...{Style.RESET_ALL}")
    time.sleep(0.8)
    print(f"{Fore.GREEN}Connection established.{Style.RESET_ALL}")
    time.sleep(0.5)
    print(f"{Fore.CYAN}Accessing password database...{Style.RESET_ALL}")
    spinner(1.0, prefix=f'{Fore.CYAN}Downloading hashes{Style.RESET_ALL}')
    print(f"{Fore.GREEN}Database acquired. Found user: {username}{Style.RESET_ALL}")
    time.sleep(0.6)
    print(f"\n{Fore.YELLOW}Initializing brute force attack...{Style.RESET_ALL}")
    time.sleep(0.8)
    print(f"{Fore.CYAN}Password length detected: {password_length} characters{Style.RESET_ALL}\n")
    time.sleep(0.5)

    # Initialize current attempt
    current_attempt = [random.choice(DATACRACK_GLYPH_SET) for _ in range(password_length)]
    cursor_pos = 0
    
    def draw_table(cursor_position):
        """Draw the 2-row table with cursor indicator."""
        cell_width = 3
        print(f"{Fore.YELLOW}╔{'═' * (cell_width * password_length + password_length - 1)}╗{Style.RESET_ALL}")
        
        # Row 1: Current attempt
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}", end="")
        for i, char in enumerate(current_attempt):
            if current_attempt[i] == target_password[i]:
                color = f"{Fore.GREEN}{Style.BRIGHT}"
            else:
                color = f"{Fore.WHITE}"
            print(f"{color}{char:^{cell_width}}{Style.RESET_ALL}", end="")
            if i < password_length - 1:
                print(f"{Fore.YELLOW}│{Style.RESET_ALL}", end="")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}")
        
        # Middle border
        print(f"{Fore.YELLOW}╠{'═' * (cell_width * password_length + password_length - 1)}╣{Style.RESET_ALL}")
        
        # Row 2: Cursor indicator
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}", end="")
        for i in range(password_length):
            if i == cursor_position:
                indicator = f"{Fore.CYAN}{Style.BRIGHT}▲{Style.RESET_ALL}"
            else:
                indicator = " "
            print(f"{indicator:^{cell_width}}", end="")
            if i < password_length - 1:
                print(f"{Fore.YELLOW}│{Style.RESET_ALL}", end="")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}")
        
        # Bottom border
        print(f"{Fore.YELLOW}╚{'═' * (cell_width * password_length + password_length - 1)}╝{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}Starting character-by-character analysis...{Style.RESET_ALL}\n")
    time.sleep(0.5)
    
    try:
        while cursor_pos < password_length:
            # Random interval for this position
            cycles = random.randint(5, 15)
            cycle_delay = random.uniform(0.03, 0.08)
            
            # Cycle through random characters
            for _ in range(cycles):
                current_attempt[cursor_pos] = random.choice(DATACRACK_GLYPH_SET)
                
                # Clear previous output and redraw
                draw_table(cursor_pos)
                
                time.sleep(cycle_delay)
            
            # Check if character matches
            if current_attempt[cursor_pos] != target_password[cursor_pos]:
                current_attempt[cursor_pos] = target_password[cursor_pos]
                draw_table(cursor_pos)
                print(f"{Fore.YELLOW}Position {cursor_pos + 1}: Mismatch detected, correcting...{Style.RESET_ALL}")
                time.sleep(0.5)
            else:
                draw_table(cursor_pos)
                print(f"{Fore.GREEN}Position {cursor_pos + 1}: Match confirmed! ✓{Style.RESET_ALL}")
                time.sleep(0.4)
            
            cursor_pos += 1
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}Cracking interrupted by user.{Style.RESET_ALL}")
        return

    # Final display - no cursor
    print(f"\n{Fore.YELLOW}╔{'═' * (3 * password_length + password_length - 1)}╗{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}║{Style.RESET_ALL}", end="")
    for i, char in enumerate(current_attempt):
        print(f"{Fore.GREEN}{Style.BRIGHT}{char:^3}{Style.RESET_ALL}", end="")
        if i < password_length - 1:
            print(f"{Fore.YELLOW}│{Style.RESET_ALL}", end="")
    print(f"{Fore.YELLOW}║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}╚{'═' * (3 * password_length + password_length - 1)}╝{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}{Style.BRIGHT}Password cracked successfully!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Username: {Fore.WHITE}{username}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Password: {Fore.WHITE}{target_password}{Style.RESET_ALL}\n")

def cmd_refresh(args):
    """Check if script has changed and restart if needed."""
    force = 'force' in args
    
    if not SCRIPT_PATH or not os.path.isfile(SCRIPT_PATH):
        print(f"{Fore.RED}Cannot determine script path for refresh.{Style.RESET_ALL}")
        return

    if force:
        print(f"{Fore.YELLOW}Force restart requested...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Restarting...{Style.RESET_ALL}\n")
        os.execv(sys.executable, [sys.executable, SCRIPT_PATH] + sys.argv[1:])
        return

    current_hash = compute_file_hash(SCRIPT_PATH)
    current_mtime = os.path.getmtime(SCRIPT_PATH) if os.path.isfile(SCRIPT_PATH) else None

    changed = False
    if INITIAL_HASH and current_hash != INITIAL_HASH:
        changed = True
    elif INITIAL_MTIME and current_mtime and current_mtime != INITIAL_MTIME:
        changed = True

    if changed:
        print(f"{Fore.YELLOW}Script file has changed. Restarting...{Style.RESET_ALL}\n")
        os.execv(sys.executable, [sys.executable, SCRIPT_PATH] + sys.argv[1:])
    else:
        print(f"{Fore.GREEN}No changes detected. Script is up to date.{Style.RESET_ALL}")

# Main REPL
def main():
    print_banner()
    show_help()

    while True:
        try:
            user_input = input(f"{Fore.BLUE}[msf#] neon>{Style.RESET_ALL} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            break

        if not user_input:
            continue

        
        parts = user_input.split()
        cmd = parts[0].lower()
        args = parts[1:]
        # Create a normalized command key with no spaces to allow "nmap scan" == "nmapscan"
        cmd_key = "".join(user_input.lower().split())

        if cmd_key in ('exit', 'quit'):
            print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
            break
        elif cmd_key == 'help' or cmd == 'help':
            show_help()
        elif cmd_key == 'time' or cmd == 'time':
            cmd_time()
        elif cmd_key == 'echo' or cmd == 'echo':
            cmd_echo(args)
        elif cmd_key == 'reverse' or cmd == 'reverse':
            cmd_reverse(args)
        elif cmd_key == 'nmap' or cmd == 'nmap':
            cmd_fakeip()
        elif cmd_key == 'datacracker' or cmd == 'datacracker':
            cmd_datacracker()
        elif cmd_key == 'injectip' or cmd == 'injectip':
            cmd_injecttoip(args)
        elif cmd_key == 'websiteattack' or cmd == 'websiteattack':
            cmd_sim(args)
        elif cmd_key == 'scan' or cmd == 'scan':
            cmd_demo(args)
        elif cmd_key == 'refresh' or cmd == 'refresh':
            cmd_refresh(args)
        else:
            print(f"{Fore.RED}Unknown command: {cmd}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Type 'help' for available commands.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
