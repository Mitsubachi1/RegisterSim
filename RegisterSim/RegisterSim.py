"""
Program: RegisterSim.py
Simulate a register experience, user experience of manually inputting items to see how much they owe at checkout
"""

import csv #to use excel spreadsheets for inventory management

#variables to store items and calculate total
subTotal = 0
total = 0
items = []

def cart():
    #input item id and qty
    id = str(input("Enter item id: "))
    #qty = int(input("Enter quantity(): "))
    
    #check for exit, if not continue to add item to cart
    if id != '0':
        additem(id)
    else:
        checkout()



def additem(id):
    
    #opens file containing store items and applies them to a list(itemPrice)
    with open('items.csv', 'r') as items:
        dictionary = csv.DictReader(items)
        itemPrice = list(dictionary)
        

       #checks index for id that matches an item, if found, calculates the price given its quantity and adds it to the subtotal
        for x in itemPrice:
           if x['ID']  == id:
              if 0 < int(id) < 100: #checks for item in weightable category
                  qty = 1
                  weight = float(input("Please enter weight of item (lbs): "))
                  itemTotal = float(x.get("Price")) * weight
              else:
                  qty = int(input("Enter quantity: "))
                  itemTotal = float(x.get("Price")) * qty

                  #disdplays item added and adds to subtotal and list before asking another item
              print(qty, x['Item'], "added $"+ str("%0.2f" % itemTotal))
              itemInCart(str(qty), x['Item'], str( "%0.2f" % itemTotal))
              total(itemTotal)
              cart()
              return

    #if item not found, warns user that item is not found
    print("Item not found, check the id and try again.")    
    cart()


def itemInCart(qty, Item, Price):
    #stores a list of items added to cart to be printed at checkout using checkout()
    itemDescript = qty + " " + Item + " $" + Price
    items.append(itemDescript)
    

def total(itemTotal):
    #gets subtotal
    global subTotal
    subTotal += itemTotal
    return subTotal
        
           
def checkout():
    #takes total and adds the tax rate, proceeds to display total
    TAXRATE = .08
    total = (subTotal * TAXRATE) + subTotal
    tax = subTotal * TAXRATE
    print("Your cart".center(30,'-'))
    for x in range(len(items)):
        print (items[x])
    print('-' * 30)
    print("Subtotal: $" + "%0.2f" % subTotal)
    print("Sales tax: $"+ "%0.2f" % tax)
    print("Your total is $" + "%0.2f" % total)
        
            

def main():
    #entrance point, welcomes user and proceeds to cart
    print("Welcome to Generic Grocery Store")
    print("Enter item id provided from book (enter 0 for id to checkout)")
    cart()
    

if __name__ == "__main__":
    main()