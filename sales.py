# sales.py

class Product:
    def __init__(self, s, p, quantity):
        self.name = s
        self.price = p
        self.stock = quantity

    def hasEnough(self, i):
        if i <= self.stock:
            return True
        else:
            return False

    def totalCost(self, i):
        return i*self.price

    def remove(self, i):
        self.stock = self.stock - i

'''
productNames = [ "Ultrasonic range finder"
                , "Servo motor"
                , "Servo controller"
                , "Microcontroller Board"
                , "Laser range finder"
                , "Lithium polymer battery"
                ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]
'''

products = [Product("Ultrasonic range finder", 2.5, 4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8)]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in products:
        if i.stock >= 1:
            print(str(products.index(i)) + " | " + i.name + ", price: " + str(i.price) + ", stock: " + str(i.stock))
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        try:
            print("(Enter 'q' to quit)")
            prodId = int(input("Enter product ID: "))
            count = int(input("Enter quantity you wish to buy: "))
        except ValueError:
            break

        p = products[prodId]
        cost = p.totalCost(count)

        if p.hasEnough(count):
            if cost < cash:
                p.remove(count)
                cash -= cost
                print("You purchased", count, p.name +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", p.name)

main()
