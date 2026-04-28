import socket
import threading

def scan_port(ip, port):
    sock = socket.socket()
    sock.settimeout(0.3)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        print(f"Port {port} -- OPEN")

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

target = input("Enter the IP you want to scan: ")
run_scanner(target, 1, 1024)