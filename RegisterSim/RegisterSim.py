"""
Program: RegisterSim.py
Simulate a register experience, user experience of manually inputting items to see how much they owe at checkout
"""

import csv #to use excel spreadsheets for inventory management

#variables to calculate total
subTotal = 0
total = 0

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


              print(qty, x['Item'], "added $"+ str(round(itemTotal,2)))
              total(itemTotal)
              cart()
              return

    #if item not found, warns user that item is not found
    print("Item not found, check the id and try again.")    
    cart()
        
def total(itemTotal):
    #gets subtotal
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
    print("Enter item id provided from book (enter 0 for id to checkout)")
    cart()
    

if __name__ == "__main__":
    main()