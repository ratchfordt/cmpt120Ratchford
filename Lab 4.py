# CMPT 120
# Lab 4
# Trevor Ratchford
# 2018.9.25


def main():

    n = eval(input("How many users do you need to register?"))
    users = 0
    for i in range(n):
        first, last = getUsername()
        uname = buildUsername(first, last, users)
        pwd = checkPass()

        print("Account configured. Your new email address is",
              uname + "@marist.edu")
        users += 1


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


def buildUsername(f, l, u):
    if u != 0:
        username = f + "." + l + str(u)
    else:
        username = f + "." + l

    return username


def passStrength(password):

    # i apologie for this one.

    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper():
                for j in range(len(password)):
                    if password[j].islower():
                        return True
    else:
        return False


main()
