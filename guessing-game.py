# guessing game
# Trevor Ratchford

def main():
    animal = "dog"
    wrong = True
    print("I'm thinking of an animal. Which one is it?\n(To quit, type q)\n")
    while wrong:
        guess = input().lower()
        if guess == animal:
            print("Yes! Good job")
            wrong = False
        elif guess == "q":
            break
        else:
            print("Nope. Try again. ")


main()
