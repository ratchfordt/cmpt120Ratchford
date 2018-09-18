# pi.py
# This approximates pi to n degrees
import math


def main():
    isEven = 1
    appx = 0
    print("Approximate Pi")
    n = eval(input("How many degrees would you like to approximate pi to? "))
    for i in range(n):
        isEven += 1
        d = (1 + i * 2)
        if (isEven % 2) != 0:
            appx -= 4/d
        else:
            appx += 4/d
    print("The approximated value is ", appx, ", which is ",
          appx - math.pi, " off from pi.")


main()
