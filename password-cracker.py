import bcrypt

def testPass(cryptPass):
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n').encode('utf-8')  
        salt = cryptPass.encode('utf-8')
        # hashed_word = bcrypt.hashpw(word, salt)
        if bcrypt.checkpw(word, salt):
            print(f"[+] Senha encontrada: {word.decode('utf-8')}")
            return
    print("[-] Password Not Found.\n") 

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip('\n')
            print(f"[*] Cracking Password For {user}")
            testPass(cryptPass)

if __name__ == '__main__':
    main()
