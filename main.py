#!/usr/bin/env python3
# ==========================================
#  CIBETIVIST :: CYBER TOOL (PY3)
#  Legal-use PenTest Utility
# ==========================================

import socket
import os
import time
import threading
import random

# ========= GLITCH INTRO ==========
def glitch(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

# clear screen
os.system("clear" if os.name == "posix" else "cls")

# ========= BANNER ==========
banner = r'''
 ██████╗ ██╗██████╗ ███████╗████████╗██╗██╗   ██╗██╗████████╗██╗███████╗████████╗
██╔═══██╗██║██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██║╚══██╔══╝██║██╔════╝╚══██╔══╝
██║   ██║██║██████╔╝█████╗     ██║   ██║██║   ██║██║   ██║   ██║█████╗     ██║   
██║▄▄ ██║██║██╔══██╗██╔══╝     ██║   ██║╚██╗ ██╔╝██║   ██║   ██║██╔══╝     ██║   
╚██████╔╝██║██║  ██║███████╗   ██║   ██║ ╚████╔╝ ██║   ██║   ██║███████╗   ██║   
 ╚══▀▀═╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝   ╚═╝   ╚═╝╚══════╝   ╚═╝   

                           >>> CIBETIVIST CYBER SECURITY <<<
'''
print(banner)

# ========== MAIN MENU ==========
def menu():
    print("""
[1] Check IP & DNS
[2] Port Scanner
[3] Simple Firewall Monitor (Simulator)
[4] LOCAL Stress-Test (Legal DDoS Test)
[5] Exit
""")

# ========== FEATURE 1: IP & DNS Checker ==========
def ip_dns_check():
    host = input("Masukkan domain / host: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"[✔] IP Address: {ip}")
    except Exception as e:
        print(f"[!] Error: {e}")

# ========== FEATURE 2: Port Scanner ==========
def port_scan():
    target = input("Target IP / domain: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]

    print(f"[•] Scanning {target} ...")
    for p in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target, p))
            print(f"[OPEN] Port {p}")
            s.close()
        except:
            pass

# ========== FEATURE 3: Fake Firewall Monitor ==========
def firewall_monitor():
    print("[•] Firewall monitor aktif (simulasi)... CTRL + C untuk stop\n")
    try:
        while True:
            time.sleep(1)
            print(f"[LOG] Traffic normal | Random token: {random.randint(1000,9999)}")
    except KeyboardInterrupt:
        print("\n[✔] Monitor dihentikan.")

# ========== FEATURE 4: Legal LOCAL DDoS Test ==========
def legal_ddos_test():
    print("""
WARNING:
Fitur ini hanya untuk mengirim traffic ke LOCALHOST (127.0.0.1).
Tidak boleh dipakai ke target tanpa izin.
""")

    target = input("Target (default 127.0.0.1): ") or "127.0.0.1"
    port = int(input("Port (default 80): ") or 80)
    threads = int(input("Jumlah thread (max 200): ") or 50)

    if target != "127.0.0.1":
        print("[BLOCKED] Tool hanya mengizinkan target 127.0.0.1 demi legalitas.")
        return

    print(f"[•] Mengirim traffic ke {target}:{port} dengan {threads} threads...\n")

    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((target, port))
                s.send(b"GET / CIBETIVIST-TEST HTTP/1.1\r\n\r\n")
                s.close()
            except:
                pass

    for i in range(threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()

    print("[✔] Stress-test berjalan... CTRL + C untuk stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[✔] Stress-test dihentikan.")

# ========== RUN ==========
while True:
    menu()
    choice = input("Pilih opsi: ")
    if choice == "1":
        ip_dns_check()
    elif choice == "2":
        port_scan()
    elif choice == "3":
        firewall_monitor()
    elif choice == "4":
        legal_ddos_test()
    elif choice == "5":
        print("Keluar...")
        break
    else:
        print("Input salah.")