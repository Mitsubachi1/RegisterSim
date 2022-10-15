"""
Program: RegisterSim.py
Simulate a register experience, user experience of manually inputting items to see how much they owe at checkout
"""

import csv #to use excel spreadsheets for inventory management


subTotal = 0
total = 0

def cart():
    #input item id and qty
    id = str(input("Enter item id: "))
    qty = int(input("Enter quantity: "))
    
    #check for exit, if not continue to add item to cart
    if id and qty != 0:
        additem(id,qty)
    else:
        checkout()



def additem(id,qty):
    
    #opens file containing store items and applies them to a list(itemPrice)
    with open('items.csv', 'r') as items:
        dictionary = csv.DictReader(items)
        itemPrice = list(dictionary)
        print(itemPrice)

       #checks index for id that matches an item, if found, calculates the price given its quantity and adds it to the subtotal
        for x in itemPrice:
           if x['ID']  == id:
              itemTotal = float(x.get("Price")) * qty
              print(qty, x['Item'], "added $"+ str(round(itemTotal,2)))
              total(itemTotal)
              cart()
              return

    #if item not found, warns user that item is not found
    print("Item not found, check the id and try again.")    
    cart()
        
def total(itemTotal):
    global subTotal
    subTotal += itemTotal
    return subTotal
        
           
def checkout():
    #takes total and adds the tax rate, proceeds to display total
    global total
    TAXRATE = .08
    total = (total(0) * TAXRATE) + total(0)
    print("Your total is $" +  str("%0.2f" % total))
        
            

def main():
    #entrance point, welcomes user and proceeds to cart
    print("Welcome to Generic Grocery Store")
    print("Enter item id provided from book (enter 0 for id and qty to checkout)")
    cart()
    

if __name__ == "__main__":
    main()