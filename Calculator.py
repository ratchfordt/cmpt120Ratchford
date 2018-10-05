# Calculator.py
# Calculates arithmatic functions without using eval()


def main():
    print("--Calculator.py--\n--Please mind order of operations in your input.--\n")
    user = input("Enter your expression: ")\
        .replace("*", " * ").replace("+", " + ").replace("/", " / ").replace("(", " ( ").replace(")", " ) ").replace("-", " - ")

    slist = user.split(" ")
    user = checknegatives(slist)
    print(pemdas(user))

def pemdas(s):
# i wanted to introduce order of operations here as well, but i would have needed to build a sort function that sorts by * = / > + = - ...
# my plan would be to create a second list in the main that converts * -> a, / -> a, + -> b, - -> b, then sorted terms by ord() or the operator substitution but that seems way too hard
    i = 0

    while i < len(s):
        if s[i] == "*":
            if s[i + 1] == "-" and not i == len(s - 1):
                s[i+2] = -s[i+2]
                del s[i]
            else:
                t1 = float(s[i - 1]) * float(s[i + 1])
                s[i] = t1
                del s[i - 1]
                del s[i]

        elif s[i] == "/":
            if s[i + 1] == "-" and not i == len(s - 1):
                s[i+2] = -s[i+2]
                del s[i]
            else:
                t1 = float(s[i - 1]) / float(s[i + 1])
                s[i] = t1
                del s[i - 1]
                del s[i]

        if s[i] == "+":
            if s[i + 1] == "-" and not i == len(s - 1):
                s[i+2] = -s[i+2]
                del s[i]
            else:
                t1 = float(s[i - 1]) + float(s[i + 1])
                s[i] = t1
                del s[i - 1]
                del s[i]

        elif s[i] == "-":
            if s[i+1] == "-" and not i == len(s-1):
                s[i+2] = -s[i+2]
                del s[i]
            else:
                t1 = float(s[i - 1]) - float(s[i + 1])
                s[i] = t1
                del s[i - 1]
                del s[i]


        else:
            i = i + 1

    return s

def checknegatives(s):
    i = 0
    while i < len(s):
        if s[i] == "":
            del s[i]
        i = i + 1
    if s[0] == "-":  # check for negatives
        s[1] = -float(s[1])
        del s[0]

    return s


main()
