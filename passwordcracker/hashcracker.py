import hashlib, termcolor

type_of_hash = str(input('Which type of hash you want to bruteforce? '))
file_path = str(input('Enter path to the file to bruteforce with: '))
hash_to_decrypt = str(input('Enter hash Value to bruteforce: '))
print()

try:
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if type_of_hash == 'md5':
                hash_object = hashlib.md5(line.strip().encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print(termcolor.colored(('[+] Found MD5 Password: ' + line.strip()), 'green'))
                    exit(0)
            elif type_of_hash == 'sha1':
                hash_object = hashlib.sha1(line.strip().encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print(termcolor.colored(('[+] Found SHA1 Password: ' + line.strip()), 'green'))
                    exit(0)
            else:
                print(termcolor.colored(('[-] Hash not supported.'), 'red'))
                exit(0)
except FileNotFoundError:
    print(termcolor.colored(('[!!] File does not exist.'), 'red'))
except:
    print(termcolor.colored(('[!!] Unhandeld error.'), 'red'))