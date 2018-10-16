# CMPT 120 - Lab #6
# Trevor Ratchford
# 10.16.2018


def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nNerd.")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower().replace(" ", "")

        if cmd == "add":
            try:
                [num1, num2] = getNums()
                result = num1 + num2
            except:
                print("Error: invalid input.")
                result = None

        elif cmd == "sub":
            try:
                [num1, num2] = getNums()
                result = num1 - num2
            except:
                print("Error: invalid input.")
                result = None

        elif cmd == "mult":
            try:
                [num1, num2] = getNums()
                result = num1 * num2
            except:
                print("Error: invalid input.")
                result = None

        elif cmd == "div":
            try:
                [num1, num2] = getNums()
                try:
                    result = num1 / num2
                except ArithmeticError:
                    print("Error: divide by 0")
                    result = None
            except:
                print("Error: invalid input.")
                result = None


        elif cmd == "quit":
            break

        else:
            print("invalid command")

        if not result == None:
            print("The result is " + str(result) + "\n")
        else:
            print("\n")

def getNums():
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    return [first, second]

def main():
    showIntro()
    doLoop()
    showOutro()

main()