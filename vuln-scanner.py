import socket
import os
import sys

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename):
    service =  open(filename, 'r')
    for line in service.readlines():
        if line.strip("\n") == banner:
            print("[+] Server is vulnerable: "+ str(banner.strip("\n")))

def main():
    if len(sys.argv) != 2:
        print(f"[-] Usage: {sys.argv[0]} <vuln filename>")
        exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"[-] {filename} does not exist")
        exit(1)
    if not os.access(filename, os.R_OK):
        print(f"[-] {filename} access denied.")
        exit(1)

    portList = [21, 22, 25, 80, 110, 443]
    for port in portList:
        for x in range(120, 125):
            ip = f'***.**.***.{x}'
            banner = retBanner(ip, port)
            if banner:
                print(f"[+] {ip}:{port} - {banner}")
                checkVulns(banner,filename)

if __name__ == '__main__':
    main()
