import socket
def scan_port(ip, port):
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()

    if result == 0:
        return True
    else:
        return False
    
def run_scanner(ip, start_port, end_port):
    print(f"Scanning {ip}...")

    for port in range(start_port, end_port + 1):
        if scan_port(ip, port) == True:
            print(f"Port {port} -- OPEN")

target = input(" Enter the IP you want to scan: ")
run_scanner(target, 1, 100)