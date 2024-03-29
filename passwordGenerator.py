import random

passwordLabel = input("Welcome to The Password Generator! Input the label for your password (Which website will it be used on etc.): ")
passwordLength = input("How long do you want the password to be? ")

try:
    int(passwordLength)

    password = ""
    for i in range(int(passwordLength)):
        password = password + chr(random.randint(32,126))

    passwordTxt = open("Data/passwords.txt", "a")
    passwordTxt.write(f'{passwordLabel}: {password}\n')
    print("Password Generated!")
except ValueError:
    print("Not a valid length.")
    exit()
    
    
