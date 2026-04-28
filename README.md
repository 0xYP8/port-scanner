# Port Scanner

A simple Python port scanner I built while learning Python and experimenting with hands-on security tools to get real-world experience of how recon works.

## What it does
Scans all ports on a given IP and lists the ones that are open. Useful for getting a quick overview of a target's exposed services and identifying what could be improved from a security standpoint.

## How it works
Uses Python's `socket` library to attempt a connection to each port. If the connection succeeds, the port is open. To make it fast, I used `threading` so multiple ports get scanned at the same time instead of one by one.

## How to run
python3 port_scanner.py
Then enter the IP you want to scan when prompted.

## Sample Output
Enter the IP you want to scan: scanme.nmap.org
Scanning scanme.nmap.org...
Port 53 -- OPEN
Scan complete!

## Challenges I faced
The first version scanned ports one by one and was painfully slow : 1024 ports could take several minutes. I fixed this by adding threading so all ports are scanned in parallel. Massive speed improvement.

## What I learned
- How sockets work for network connections in Python
- Why timeouts matter (otherwise the scanner hangs on closed ports)
- How threading can speed up I/O bound tasks

## Tested on
scanme.nmap.org : a server provided by Nmap for legal scan practice.

## Future improvements
- Save scan results to a file
- Add banner grabbing to detect what service and version is running on each open port
