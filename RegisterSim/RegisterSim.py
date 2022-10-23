"""
Program: RegisterSim.py
Simulate a register experience, user experience of manually inputting items to see how much they owe at checkout
"""

import csv #to use excel spreadsheets for inventory management
import math
import copy

#variables to store items and calculate total
subTotal = 0
total = 0
items = []
itemtuple = {}
itemlist = []

def cart():
    #input item id and qty


    id = int(input("Enter item id: "))
    #qty = int(input("Enter quantity(): "))
    
    #check for exit, if not continue to add item to cart
    if id == 0:
        checkout()
    elif id == -1:
        print(itemlist)
        removelist()
    else:
        additem(str(id))



def additem(id):
    global itemlist
    itemlist = copy.deepcopy(itemlist)
    #opens file containing store items and applies them to a list(itemPrice)
    with open('items.csv', 'r') as items:
        dictionary = csv.DictReader(items)
        itemPrice = list(dictionary)
        

       #checks index for id that matches an item, if found, calculates the price given its quantity and adds it to the subtotal
        for x in itemPrice:
           if x['ID']  == id:
              if 0 < int(id) < 1000: #checks for item in weightable category
                  qty = 1
                  weight = float(input("Please enter weight of item (lbs): "))
                  itemTotal = float(x.get("Price")) * weight
                  itemtuple['Item'] = x.get("Item")
                  itemtuple['ID'] = x.get("ID")
                  itemtuple['Total'] = itemTotal
                  itemtuple['Qty'] = qty
                  
                  
              else:
                  qty = float(input("Enter quantity: "))
                  qty = math.floor(qty)
                  itemTotal = float(x.get("Price")) * qty
                  itemtuple['Item'] = x.get("Item")
                  itemtuple['ID'] = x.get("ID")
                  itemtuple['Total'] = itemTotal
                  itemtuple['Qty'] = qty
                  
                  

                  #disdplays item added and adds to subtotal and list before asking another item
              addlist(itemtuple)
              print(qty, x['Item'], "added $"+ str("%0.2f" % itemTotal))
              cart()
              return
           
           
    
    #if item not found, warns user that item is not found
    print("Item not found, check the id and try again.")    
    cart()

def addlist(itemtuple):
    itemlist.append(itemtuple)

def removelist():
    #removes an item from the shopping cart
    removeID = str(input("Enter item id to remove: "))
    for x in itemlist:
  
       if x['ID'] == removeID:
           x.pop('Qty')
           x.pop('Item')
           x.pop('Total')
           x.pop('ID')
           while {} in itemlist:
               itemlist.remove({})
           cart()
           return

      
    print("ID not found, Try again")
    cart()
          

def subtotal():
    #gets subtotal
    global subTotal
    for x in itemlist:
        subTotal += x.get('Total')
    return subTotal
        
           
def printItems():
    for x in itemlist:
        print(x.get('Qty'), x.get('Item') , "$%.02f" % x.get('Total'))

def checkout():
    #takes subtotal and adds the tax rate, proceeds to display total
    subtotal()
    TAXRATE = .08
    total = (subTotal * TAXRATE) + subTotal
    tax = subTotal * TAXRATE
    print("Your cart".center(30,'-'))
    printItems()
 
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