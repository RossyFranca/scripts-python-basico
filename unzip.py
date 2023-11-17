import pyzipper
import optparse
from threading import Thread

def extractFile(zfile, password):
    try:
        with pyzipper.AESZipFile(zfile) as zFile:
            zFile.setpassword(password.encode())
            zFile.extractall()
            print(f"[+] Password found: {password}")
            exit(0)  # Encerra o programa após encontrar a senha
    except Exception as e:
        return

def main():
    parser = optparse.OptionParser(usage="usage: %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    
    if (options.zname == None) or (options.dname == None):
        print(parser.usage)
        exit(1)
    else:
        zname = options.zname
        dname = options.dname

    zip_file_name = zname
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        # Cria uma thread para cada elemento do array e executa simultaneamente
        t = Thread(target=extractFile, args=(zip_file_name, password))
        t.start()

if __name__ == '__main__':
    main()
