# guessing game
# Trevor Ratchford

def main():
    animal = "dog"
    wrong = True
    print("I'm thinking of an animal. Which one is it? ")
    while wrong:
        guess = input()
        if guess.lower() == animal:
            print("Yes! Good job")
            wrong = False
        else:
            print("Nope. Try again. ")


main()
