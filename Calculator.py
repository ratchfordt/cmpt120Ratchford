# Calculator.py
# Calculates arithmatic functions without using eval()


def main():
    print("Calculator.py")
    user = input("Enter your expression: ")
    hard = user.replace(" ", "")
    list = user.split(" ")
    #pemdas(user)


def pemdas(s):
    n = len(s)
    for i in range(n):
        if s[i] == "(":
            for j in range(i+1, n):
                #print(j)
                if s[j] == "+":
                    t1 = s[i+1:(j-1)]
                    t2 = s[(j+1):n]
                    for l in range(len(t1), 0):
                        print(l)
                        if not isinstance(t1[l], int):
                            t1 = t1[l:len(t1)]
                    #s = t1 + t2
    print(t1)

main()
