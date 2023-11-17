import pyzipper

# Nome do arquivo ZIP
zip_file_name = 'evil.zip'

# Nome do arquivo a ser adicionado ao ZIP
file_to_zip = 'teste.txt'

# Senha para o arquivo ZIP
password = 'secret'

# Cria o arquivo ZIP e adiciona o conteúdo com senha
with pyzipper.AESZipFile(zip_file_name, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zip_file:
    zip_file.setpassword(password.encode())
    zip_file.write(file_to_zip)

print(f"Arquivo ZIP '{zip_file_name}' criado com sucesso.")
