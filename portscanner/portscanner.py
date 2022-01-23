import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:                                        # for ipaddress
        IP(ip)
        return(ip)
    except ValueError:                          # for domainname
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)                         # byte size

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)                    # the higher the timeout, the higher the accuracy
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))

    except:
        # print('[-] Port ' + str(port) + ' Is Closed')
        pass

if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
    # port_num = input('[+] Enter Number of Ports you want to scan: ')
    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)
