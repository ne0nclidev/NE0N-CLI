#!/usr/bin/env python3
"""
mini_hack_cli.py
A tiny "pseudo hacking" terminal CLI with colored output and:
 - fakeip (animated random IP generation)
 - datacracker (animated reveal of a generated 16-20 char string)
 - refresh (checks file for updates and restarts if changed)
Requires: pip install colorama
Usage: python mini_hack_cli.py
"""

import sys
import os
import time
import random
import datetime
import hashlib
from typing import List

try:
    from colorama import init as colorama_init, Fore, Style
except ImportError:
    print("This script requires the 'colorama' package. Install with:")
    print("    pip install colorama")
    sys.exit(1)

# ----------------- Config -----------------
colorama_init(autoreset=True)  # ensures colors reset after each print

APP_NAME = "NEON-CLI"
VERSION = "0.9"

# FakeIP configuration
FAKEIP_DURATION = 20.0        # seconds total
FAKEIP_MIN_DELAY = 0.0        # min seconds between IPs
FAKEIP_MAX_DELAY = 0.7       # max seconds between IPs
FAKEIP_INITIAL_WAIT_MIN = 4.0 # min initial "Finding IPs" wait (seconds)
FAKEIP_INITIAL_WAIT_MAX = 5.0 # max initial "Finding IPs" wait (seconds)

# DataCracker configuration
DATACRACK_MIN_LEN = 34
DATACRACK_MAX_LEN = 35
DATACRACK_TICK = 0.02            # fast update tick (seconds)
DATACRACK_FREEZE_INTERVAL = 0.8 # time between freezing successive characters (seconds)
DATACRACK_GLYPH_SET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{};:,.<>/?"
)

# ------------------------------------------

# ---------- Startup file-hash capture for refresh ----------
# Determine script path if available
SCRIPT_PATH = None
try:
    SCRIPT_PATH = os.path.abspath(__file__)
except NameError:
    SCRIPT_PATH = None

def compute_file_hash(path: str) -> str:
    """Return SHA-256 hex digest of file at path."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""

# capture initial hash and mtime if script file is available
INITIAL_HASH = None
INITIAL_MTIME = None
if SCRIPT_PATH and os.path.isfile(SCRIPT_PATH):
    INITIAL_HASH = compute_file_hash(SCRIPT_PATH)
    try:
        INITIAL_MTIME = os.path.getmtime(SCRIPT_PATH)
    except Exception:
        INITIAL_MTIME = None

# ---------- Utility functions ----------
def now_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_ip() -> str:
    # Generate four octets 0-255 (simple random IPv4)
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def print_banner():
    # Colors
    cyan = Fore.CYAN + Style.BRIGHT
    mag = Fore.MAGENTA + Style.BRIGHT
    dim = Style.DIM
    reset = Style.RESET_ALL
    meta = f"{dim}{Fore.YELLOW}{APP_NAME} {VERSION} - {now_str()}{reset}"
    print(reset)
    print(meta)
    print(f"{Fore.GREEN}NE0N-CLI, a powerful command with data cracking and IP scanning capabillities{reset}\n")

def show_help():
    print(Fore.YELLOW + "Available commands:" + Style.RESET_ALL)
    cmds = [
        ("help", "Show this help"),
        ("exit", "Exit the CLI"),
        ("time", "Show current time"),
        ("echo <text>", "Echo input"),
        ("reverse <text>", "Reverse the text"),
        ("fakeip", "Prompt then generate fake IPv4 addresses at random intervals"),
        ("datacracker", "Enter text then watch a 16-20 char 'crack' reveal animation"),
        ("refresh [force]", "Check the script file for updates and restart if changed. 'force' restarts unconditionally."),
    ]
    for cmd, desc in cmds:
        print(f"  {Fore.CYAN}{cmd:<18}{Style.RESET_ALL} {desc}")
    print()

# ---------- Command implementations ----------
def cmd_time():
    print(Fore.GREEN + now_str() + Style.RESET_ALL)

def cmd_echo(args: List[str]):
    print(" ".join(args))

def cmd_reverse(args: List[str]):
    print("".join(args)[::-1])

def _animated_finding(remaining_wait: float):
    """
    Show "Finding IPs" with animated dots while sleeping for remaining_wait seconds.
    This uses short sub-sleeps so that it's responsive to KeyboardInterrupt.
    """
    label = Fore.YELLOW + "Scanning IPs" + Style.RESET_ALL
    dot_color = Style.DIM + Fore.WHITE
    reset = Style.RESET_ALL

    start = time.time()
    dot_index = 0
    try:
        while True:
            elapsed = time.time() - start
            if elapsed >= remaining_wait:
                break
            # build dots (0..3)
            dots = "." * (dot_index % 4)
            print(f"\r{label}{dot_color}{dots}{reset} ", end="", flush=True)
            dot_index += 1
            # short sleep to animate smoothly and allow Ctrl+C
            time.sleep(0.8)
    except KeyboardInterrupt:
        # ensure we move to new line and propagate interruption
        print()
        raise
    # finalize line and move to next line (clear the animated line)
    print("\r" + " " * (len("Scanning IPs....") + 5) + "\r", end="", flush=True)

def cmd_fakeip():
    """
    Prompts the user for a piece of data (flavor), shows a short 'Finding IPs' animation,
    then prints random IPv4 addresses for FAKEIP_DURATION seconds. IPs appear at random
    intervals between FAKEIP_MIN_DELAY and FAKEIP_MAX_DELAY seconds.
    """
    try:
        data = input(Fore.MAGENTA + "Enter a DNS/ID: " + Style.RESET_ALL)
    except (KeyboardInterrupt, EOFError):
        print()  # newline after ^C or EOF
        return

    header = f"\n{Fore.YELLOW}IPScan script executed.{Style.RESET_ALL}  (input: {Fore.CYAN}{data}{Style.RESET_ALL})\n"
    print(header)

    # Start time and compute end time
    start_time = time.time()
    end_time = start_time + FAKEIP_DURATION

    # initial little wait before first IP with "Finding IPs" animated message
    initial_wait = random.uniform(FAKEIP_INITIAL_WAIT_MIN, FAKEIP_INITIAL_WAIT_MAX)
    # But clamp to remaining total time
    remaining_total = end_time - time.time()
    initial_wait = min(initial_wait, max(0.0, remaining_total))

    if initial_wait > 0:
        try:
            _animated_finding(initial_wait)
        except KeyboardInterrupt:
            print("\n" + Fore.RED + "Generation interrupted by user." + Style.RESET_ALL)
            return

    count = 0

    try:
        while True:
            now = time.time()
            if now >= end_time:
                break

            ip = generate_random_ip()
            # IP green, "Generating IP..." dim gray
            ip_str = f"{Fore.GREEN}--| {ip}{Style.RESET_ALL} {Style.DIM}found{Style.RESET_ALL}"
            print(ip_str)
            count += 1

            # choose a random delay while respecting remaining time
            remaining = end_time - time.time()
            if remaining <= 0:
                break
            # pick random delay but don't exceed remaining
            sleep_time = random.uniform(FAKEIP_MIN_DELAY, FAKEIP_MAX_DELAY)
            if sleep_time > remaining:
                # sleep the remaining to create a natural pacing before finishing
                time.sleep(remaining)
                break
            else:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\n" + Fore.RED + "Generation interrupted by user." + Style.RESET_ALL)
        return

    print(f"\n{Fore.YELLOW}Done. {count} IP(s) found.{Style.RESET_ALL}\n")

# ---------- DataCracker implementation ----------
def _make_target_from_input(user_input: str, length: int) -> str:
    """
    Deterministically generate a target string of given length from user_input.
    Uses SHA-256 bytes to map into DATACRACK_GLYPH_SET.
    """
    digest = hashlib.sha256(user_input.encode("utf-8")).digest()
    glyphs = DATACRACK_GLYPH_SET
    out = []
    for i in range(length):
        b = digest[i % len(digest)]
        idx = b % len(glyphs)
        out.append(glyphs[idx])
    return "".join(out)

def cmd_datacracker():
    """
    Prompt for input, generate a 16-20 char target string from it, then show
    a fast-changing line where each character cycles through random glyphs.
    One-by-one (left->right) characters freeze to reveal the target, creating
    a 'data cracking' animation.
    """
    try:
        user_input = input(Fore.MAGENTA + "Enter an encrypted password to crack: " + Style.RESET_ALL)
    except (KeyboardInterrupt, EOFError):
        print()
        return

    length = random.randint(DATACRACK_MIN_LEN, DATACRACK_MAX_LEN)
    target = _make_target_from_input(user_input, length)

    # animation state
    frozen = [False] * length
    display = [" "] * length

    # reveal left to right
    next_to_freeze = 0

    # track times
    last_freeze_time = time.time()
    start_time = time.time()

    # print header
    print(f"\n{Fore.YELLOW}[BRUTE FORCE METHOD]{Style.RESET_ALL})\n")

    try:
        while True:
            now = time.time()
            # update characters that are not frozen with random glyphs
            for i in range(length):
                if not frozen[i]:
                    display[i] = random.choice(DATACRACK_GLYPH_SET)

            # Build colored line:
            # - frozen chars: bright green
            # - unfrozen changing chars: cyan (bright)
            # - to make it look "glitchy", we dim non-primary chars slightly
            frozen_part = ""
            for i, ch in enumerate(display):
                if frozen[i]:
                    frozen_part += f"{Fore.GREEN}{Style.BRIGHT}{target[i]}{Style.RESET_ALL}"
                else:
                    frozen_part += f"{Fore.CYAN}{ch}{Style.RESET_ALL}"

            # Carriage-return print without newline, flush immediately
            print("\r" + frozen_part, end="", flush=True)

            # Check if it's time to freeze the next character
            if next_to_freeze < length and (now - last_freeze_time) >= DATACRACK_FREEZE_INTERVAL:
                # freeze next
                frozen[next_to_freeze] = True
                # ensure its display becomes the target (so next print shows it)
                display[next_to_freeze] = target[next_to_freeze]
                next_to_freeze += 1
                last_freeze_time = now

            # Exit when all frozen
            if all(frozen):
                break

            # Short tick so characters update rapidly
            time.sleep(DATACRACK_TICK)
    except KeyboardInterrupt:
        # Move to next line and show partial revealed string
        print()
        print(Fore.RED + "Datacracker interrupted by user." + Style.RESET_ALL)
        return

    # finalize output with newline and show result
    print()  # newline after the final line
    print(f"{Fore.YELLOW}Crack complete: {Fore.GREEN}{Style.BRIGHT}{target}{Style.RESET_ALL}\n")

def cmd_refresh(args: List[str]):
    """
    Check the script file for updates. If changed (hash or mtime different),
    restart the process to reload the updated script. If 'force' is provided,
    restart unconditionally.
    """
    force = False
    if args and args[0].lower() == "force":
        force = True

    if not SCRIPT_PATH:
        print(Fore.RED + "Cannot determine script file path for refresh (no __file__). Refresh not available." + Style.RESET_ALL)
        return

    if not os.path.isfile(SCRIPT_PATH):
        print(Fore.RED + f"Script file not found at expected path: {SCRIPT_PATH}" + Style.RESET_ALL)
        return

    try:
        current_hash = compute_file_hash(SCRIPT_PATH)
        current_mtime = os.path.getmtime(SCRIPT_PATH)
    except Exception as e:
        print(Fore.RED + f"Error reading script file for refresh: {e}" + Style.RESET_ALL)
        return

    changed = False
    reason = []
    if INITIAL_HASH is None:
        # If we didn't capture initial hash earlier, consider mtime change
        if INITIAL_MTIME is None:
            # no baseline; only 'force' works
            if force:
                changed = True
                reason.append("forced by user (no baseline available)")
            else:
                print(Fore.YELLOW + "No baseline available to compare. Use 'refresh force' to restart unconditionally." + Style.RESET_ALL)
                return
        else:
            if current_mtime != INITIAL_MTIME:
                changed = True
                reason.append("file modification time changed")
    else:
        if current_hash != INITIAL_HASH:
            changed = True
            reason.append("file content hash changed")
        elif current_mtime != INITIAL_MTIME:
            # hash same but mtime different — possibly touched; treat as change
            changed = True
            reason.append("file modification time changed (content same)")

    if force:
        changed = True
        reason.append("forced restart")

    if not changed:
        print(Fore.GREEN + "No updates detected. (script file unchanged)" + Style.RESET_ALL)
        return

    # Show details and restart
    print(Fore.YELLOW + "Update detected: " + ", ".join(reason) + Style.RESET_ALL)
    print(Fore.CYAN + "Restarting to apply updates..." + Style.RESET_ALL)

    # Replace the current process with a new Python process running the same argv
    try:
        python = sys.executable or "python"
        # flush stdout/stderr
        sys.stdout.flush()
        sys.stderr.flush()
        os.execv(python, [python] + sys.argv)
    except Exception as e:
        print(Fore.RED + f"Failed to restart: {e}" + Style.RESET_ALL)
        print(Fore.YELLOW + "You can manually restart the script to apply updates." + Style.RESET_ALL)

# ----------  Run CMDS ----------
def cmd_run(args: List[str]):
    """
    Run another Python script.

    Usage:
      run path/to/script.py [arg1 arg2 ...]
      run ./script.py
      run ../otherdir/script.py --option value

    This launches the given script with the same Python interpreter (sys.executable)
    and streams its stdout/stderr directly to this terminal. Ctrl+C will try to
    terminate the child process.
    """
    if not args:
        print(Fore.YELLOW + "Usage: run <script.py> [args...]" + Style.RESET_ALL)
        return

    script_path = args[0]
    script_args = args[1:]

    # Try the path as given, then relative to the CLI script's directory
    candidates = [script_path]
    if SCRIPT_PATH:
        base_dir = os.path.dirname(SCRIPT_PATH)
        candidates.append(os.path.join(base_dir, script_path))

    found = None
    for p in candidates:
        if os.path.isfile(p):
            found = p
            break

    if not found:
        print(Fore.RED + f"Script not found: {script_path}" + Style.RESET_ALL)
        return

    # Warn if not a .py file (still allow)
    if not found.lower().endswith(".py"):
        print(Fore.YELLOW + "Warning: file does not end with .py — attempting to run anyway." + Style.RESET_ALL)

    cmd = [sys.executable, found] + script_args
    print(Fore.CYAN + f"Running: {cmd}" + Style.RESET_ALL)

    try:
        # Launch child with stdio inherited so output appears live in terminal
        proc = subprocess.Popen(cmd)
        # Wait for it to finish; allow KeyboardInterrupt to interrupt child
        try:
            returncode = proc.wait()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nInterrupt received — terminating child process..." + Style.RESET_ALL)
            proc.terminate()
            try:
                returncode = proc.wait(timeout=5)
            except Exception:
                proc.kill()
                returncode = proc.wait()
            print(Fore.RED + f"Child process terminated with code {returncode}" + Style.RESET_ALL)
            return
        print(Fore.GREEN + f"Child exited with code {returncode}" + Style.RESET_ALL)
    except FileNotFoundError as e:
        print(Fore.RED + f"Failed to run script: {e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error running script: {e}" + Style.RESET_ALL)

# ---------- Main loop ----------
def main():
    print_banner()

    while True:
        try:
            raw = input(Fore.BLUE + "[#] neon> " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n" + Fore.RED + "Exiting. Goodbye!" + Style.RESET_ALL)
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "help":
            show_help()
        elif cmd == "exit":
            print(Fore.RED + "Goodbye!" + Style.RESET_ALL)
            break
        elif cmd == "time":
            cmd_time()
        elif cmd == "echo":
            cmd_echo(args)
        elif cmd == "reverse":
            cmd_reverse(args)
        elif cmd == "ipscan":
            cmd_fakeip()
        elif cmd == "datacracker":
            cmd_datacracker()
        elif cmd == "refresh":
            cmd_refresh(args)
        elif cmd == "run":
            cmd_run(args)
        else:
            print(Fore.RED + f"Unknown command: {cmd}. Type 'help' for commands." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
