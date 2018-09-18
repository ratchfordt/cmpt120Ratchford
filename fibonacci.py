# Fibonacci.py
# This program computes the nth number in the Fibonacci sequence


def main():
    print("(Positive numbers only please)")
    n = eval(input("Input a number to pull from the Fibonacci sequence: "))
    ans = fibonacci(n)
    print(ans)


def fibonacci(i):
    i = abs(i)
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        n = fibonacci(i-1) + fibonacci(i-2)
    return n


main()
