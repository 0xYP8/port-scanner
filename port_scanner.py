import socket
import threading
import csv
from datetime import datetime
results = []

def scan_port(ip, port):
    sock = socket.socket()
    sock.settimeout(0.3)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        status = "OPEN"
        print(f"Port {port} -- OPEN")
    else:
        status = "CLOSED"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append([timestamp,ip, port, status])

def run_scanner(ip, start_port, end_port):
    print(f"Scanning {ip}...")
    threads = []
    
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Scan complete!")

def save_to_csv(ip):
    filename = f"scan_{ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["TimeStamp", "Target IP", "Port", "Status"])
        writer.writerows(results)
    print(f"Results saved to {filename}")

target = input("Enter the IP you want to scan: ")
run_scanner(target, 1, 1024)
save_to_csv(target)