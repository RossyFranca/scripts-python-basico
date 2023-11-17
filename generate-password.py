import bcrypt

password = "admin123"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hashed_password.decode('utf-8'))
if(bcrypt.checkpw(password.encode('utf-8'), hashed_password)):
    print("Password is correct!")
else:
    print("Password is incorrect.")
