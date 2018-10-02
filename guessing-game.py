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
            like = input("Do you like ", animal, "s?").lower()
            if like[0] == "y":
                print("Me too!")
            if like[0] == "n":
                print("Shame on you.")
        elif guess[0] == "q":
            break
        else:
            print("Nope. Try again. ")


main()
