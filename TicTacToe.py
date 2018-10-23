# CMPT 120 Intro to Programming
# Lab #7
# Author: Trevor Ratchford
# Created: 2018-10-22


symbol = [ " ", "x", "o" ]

def printBoard(board):
    i = 0
    r = 0
    while i<7:
        if i % 2 == 0:
            print("+-----------+")
        else:
            print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
            r = r + 1
        i = i + 1


def markBoard(board, row, col, player):
    if board[row][col] == " ":
        if player == 1:
            board[row][col] = "O"
        elif player == 2:
            board[row][col] = "X"
        return board
    else:
        print("Invalid position.")
        return None


def getPlayerMove():
    row = int(input("Input intended row: "))
    col = int(input("Input intended column: "))
    return row,col


def hasBlanks(board):
    for x in board:
        for y in x:
            if y == " ":
                return True
    return False


def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        b = markBoard(board,row,col,player)
        if not b is None:
            player = player % 2 + 1 # switch player for next turn
            board = b
        else:
            "Same player"
    printBoard(board)


main()
