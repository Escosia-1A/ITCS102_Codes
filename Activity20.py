from getpass import getpass

isLogin = False
while isLogin == False:
    username = input("Input Username: ")
    password = getpass("Input password: ")

    if username == "User5" and password == "HBD":
        print("Access Granted")
        isLogin = True
    else:
        print("Access Denied")
        isLogin = False