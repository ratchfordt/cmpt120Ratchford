# OO_Calculator

from graphics import *

# CalculatorGraphics.py

"""
def main():
    equation = input("Please enter an equation (use spaces):")
    listEquation = equation.split()
    result = solveEquation(listEquation)
    print(result)
"""


def modifyEquation(idx, eq, value):
    # remove the two operands and the operqator
    del eq[idx - 1:idx + 2]
    # insert the result
    eq.insert(idx - 1, value)
    # move the index back one place
    idx = idx - 1
    return idx, eq


def solveEquation(eq):
    eq = eq.split()
    opIdx = 1
    while '*' in eq or '/' in eq:
        if eq[opIdx] == '*':
            # calculate the operation
            result = float(eq[opIdx - 1]) * float(eq[opIdx + 1])
            # update the equation list
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '/':
            result = float(eq[opIdx - 1]) / float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1
        if opIdx >= len(eq):
            break
    opIdx = 1
    while '+' in eq or '-' in eq:
        if eq[opIdx] == '+':
            result = float(eq[opIdx - 1]) + float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '-':
            result = float(eq[opIdx - 1]) - float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1
        if opIdx >= len(eq):
            break
    return eq[0]


def createButton(values):
    p1 = Point(values[0], values[1])
    p2 = Point(values[0] + .9, values[1] + .9)
    button = Rectangle(p1, p2)
    button.setFill("lightblue")
    label = Text(Point(values[0] + .5, values[1] + .5), values[2])
    label.setStyle("bold")
    return button, label


def createKeypad(lst):
    keys = []
    for key in lst:
        button, label = createButton(key)
        keys.append([button, label])
    return keys


def renderKeys(keys, win):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)


def getInputs(w):
    m = w.getMouse()
    return m


def checkInput(inp):
    while True:
        if 1 > inp.getX() >= 0 and 1 > inp.getY() >= 0:
            return "+/-"
        elif 2 > inp.getX() >= 1 and 1 > inp.getY() >= 0:
            return "0"
        elif 3 > inp.getX() >= 2 and 1 > inp.getY() >= 0:
            return "."
        elif 4 > inp.getX() >= 3 and 1 > inp.getY() >= 0:
            return "="
        elif inp.getX() >= 4 and 1 > inp.getY() >=0:
            return "M+"
        elif 1 > inp.getX() >= 0 and 2 > inp.getY() >= 1:
            return "1"
        elif 2 > inp.getX() >= 1 and 2 > inp.getY() >= 1:
            return "2"
        elif 3 > inp.getX() >= 2 and 2 > inp.getY() >= 1:
            return "3"
        elif 4 > inp.getX() >= 3 and 2 > inp.getY() >= 1:
            return "+"
        elif inp.getX() >= 4 and 2 > inp.getY() >= 1:
            return "M-"
        elif 1 > inp.getX() >= 0 and 3 > inp.getY() >= 2:
            return "4"
        elif 2 > inp.getX() >= 1 and 3 > inp.getY() >= 2:
            return "5"
        elif 3 > inp.getX() >= 2 and 3 > inp.getY() >= 2:
            return "6"
        elif 4 > inp.getX() >= 3 and 3 > inp.getY() >= 2:
            return "-"
        elif inp.getX() >= 4 and 3 > inp.getY() >= 2:
            return "MR"
        elif 1 > inp.getX() >= 0 and 4 > inp.getY() >= 3:
            return "7"
        elif 2 > inp.getX() >= 1 and 4 > inp.getY() >= 3:
            return "8"
        elif 3 > inp.getX() >= 2 and 4 > inp.getY() >= 3:
            return "9"
        elif 4 > inp.getX() >= 3 and 3 <= inp.getY() < 4:
            return "*"
        elif 4 > inp.getX() >= 3 and inp.getY() >= 4:
            return "/"
        elif inp.getX() >= 4 and 3 <= inp.getY() < 4:
            return "MC"


def disp(eq, w):
    tcoorx = Point(0, 4)
    tcoory = Point(2.9, 5)
    tbox = Rectangle(tcoorx, tcoory)
    tbox.setFill("yellow")
    tbox.draw(w)

    coords = Point(1.4, 4.5)
    e = Text(coords, eq)
    e.draw(w)


def main():
    keyList = [[0, 0, '+/-'], [1, 0, '0'], [2, 0, '.'], [3, 0, '='], [4, 0, 'M+'],
               [0, 1, '1'], [1, 1, '2'], [2, 1, '3'], [3, 1, '+'], [4, 1, 'M-'],
               [0, 2, '4'], [1, 2, '5'], [2, 2, '6'], [3, 2, '-'], [4, 2, 'MR'],
               [0, 3, '7'], [1, 3, '8'], [2, 3, '9'], [3, 3, 'x'], [4, 3, 'MC'],
               [0, 4, ''], [1, 4, ''], [2, 4, ''], [3, 4, '/']]

    keys = createKeypad(keyList)

    equation = ""
    negative = False

    win = GraphWin("Key Pad")
    win.setCoords(0.0, 0.0, 5.0, 5.0)
    win.setBackground("navy")

    renderKeys(keys, win)

    tcoordx = Point(0,4)
    tcoordy = Point(2.9,5)
    textbox = Rectangle(tcoordx, tcoordy)
    textbox.setFill("yellow")
    textbox.draw(win)

    mem = ''

    while True:
        user = checkInput(getInputs(win))
        try:
            int(user)
            equation = equation + user
            disp(equation, win)
        except:
            if user == "+/-" and negative:
                negative = False
            elif user == "+/-" and not negative:
                negative = True
            elif user == "M+":
                if mem == "":
                    mem = equation
                else:
                    mem = mem + "+ " + equation + " "
                equation = ''
            elif user == "M-":
                if mem == "":
                    mem = equation
                else:
                    mem = mem + "- " + equation + " "
                equation = ''
            elif user == "MR":
                equation = mem
                disp(equation, win)
            elif user == "MC":
                mem = ''
            elif user == '.':
                equation = equation + "."
            elif user == "=":
                try:
                    equation = solveEquation(equation)
                    disp(equation, win)
                    equation = ''
                except:
                    equation = ''
                    disp(equation, win)
            else:
                if equation == "":
                    user = None
                else:
                    equation = equation + " " + user + " "
                    disp(equation, win)
        if negative:
            equation = "-" + equation
            disp(equation, win)
        print("Equation: ")
        print(equation)
        print("Memory: ")
        print(mem)


main()
