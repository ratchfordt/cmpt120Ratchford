# CMPT 120
# Lab 4
# Trevor Ratchford
# 2018.9.25

def main():
    names = getUsername()
    first = names[0]
    last = names[1]
    uname = buildUsername(first, last)
    pwd = checkPass()
    # TODO modify this to ensure the password has at least 8 characters

    print("Account configured. Your new email address is",
          uname + "@marist.edu")

def checkPass():
    passwd = input("Create a new password: ")
    while not passStrength(passwd):
        passwd = input("Weak. Must be 8 characters w/"
                       " upper and lower cases. Try again: ")
        print("Close enough.")
    return passwd

def getUsername():
    f = input("Enter your first name: ").lower()
    l = input("Enter your last name: ").lower()
    return f, l

def buildUsername(f, l):
    username = f + "." + l
    return username

def passStrength(password):
    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper():
                for j in range(len(password)):
                    if password[j].islower():
                        return True
    else:
        return False
main()