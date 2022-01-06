import socket
# import subprocess
import sys
import os

from datetime import datetime

os.system('cls')  # on windows

print(r"""  ____ _          _     _               __        ___ _ _ _     
 / ___| |__  _ __(_)___| |_ ___  _ __   \ \      / (_) | (_)___ 
| |   | '_ \| '__| / __| __/ _ \| '_ \   \ \ /\ / /| | | | / __|
| |___| | | | |  | \__ \ || (_) | | | |   \ V  V / | | | | \__ \
 \____|_| |_|_|  |_|___/\__\___/|_| |_|    \_/\_/  |_|_|_|_|___/
                                                                """)
print(":" * 60)
print("\nWelcome to my basic (non-multi-threaded) port scanner!\n")
print(":" * 60)

# Ask for input
server = input("\nEnter a remote host to scan: ")
ip = socket.gethostbyname(server)


print("*" * 60)
print("Please wait, scanning host", ip)
print("*" * 60)

# Check the date and time the scan was started
start = datetime.now()


open_ports = []

for port in range(1, 81):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            sock.connect((ip, port))
            open_ports.append(port)

    except:
        print(f"Port {port} is closed on {server}.")

for port in open_ports:
    print(f"Port {port} is open on {server}.")

# Checking time again
finish = datetime.now()

# Calculate the time difference
total = finish - start

# Printing the information on the screen
print(f'Scanning Completed in {total}')
