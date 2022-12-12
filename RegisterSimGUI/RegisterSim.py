##GUI Module, MAIN
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
itemtotal= 0
items = []
itemtuple = {}
itemlist = []

def additem(id, measurement):
    global itemlist, itemtotal
    itemlist = copy.deepcopy(itemlist)
    found = False #flag for found items, used for gui text
    #opens file containing store items and applies them to a list(itemPrice)
    with open('items.csv', 'r') as items:
        dictionary = csv.DictReader(items)
        itemPrice = list(dictionary)
        

       #checks index for id that matches an item, if found, calculates the price given its quantity and adds it to the subtotal
        for x in itemPrice:
           if x['ID']  == id:
              if 0 < int(id) < 1000: #checks for item in weightable category
                  qty = 1
                  itemTotal = float(x.get("Price")) * measurement
                  itemtuple['Item'] = x.get("Item")
                  itemtuple['ID'] = x.get("ID")
                  itemtuple['Total'] = itemTotal
                  itemtuple['Qty'] = qty
                  found = True
                  
              else:
                  measurement = math.floor(measurement)
                  itemTotal = float(x.get("Price")) * measurement
                  itemtuple['Item'] = x.get("Item")
                  itemtuple['ID'] = x.get("ID")
                  itemtuple['Total'] = itemTotal
                  itemtuple['Qty'] = measurement
                  found = True
                  
                  #disdplays item added and adds to subtotal and list before asking another item
              addlist(itemtuple)
                  
              #changes int/ float to str to use make string for return
              itemtotal = str("%0.2f" % itemTotal)
              measurement = str(measurement)
              txt = (measurement + " " + x['Item'] + " added $" + itemtotal + '\n')
              print (txt)
    if found == True:
        return txt
    else:
        return 'Item Not found\n'
            
           

def addlist(itemtuple):
    itemlist.append(itemtuple)

def removelist(removeID):
    #removes an item from the shopping cart

    print("Remove Items".center(30,'-'))
    print("Item: ID\n"+ '-' * 30)
    for x in itemlist:
        print(x.get('Item') + ":", x.get('ID') )
 
    print('-' * 30)
    for x in itemlist:
  
       if x['ID'] == removeID:
           x.pop('Qty')
           x.pop('Item')
           x.pop('Total')
           x.pop('ID')
           while {} in itemlist:
               itemlist.remove({})
           return

      
    print("ID not found, Try again")
          

def subtotal():
    #gets subtotal
    global subTotal
    subTotal = 0 #reset subTotal for re-checkout
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
    #cli txt
    print('-' * 30)
    print("Subtotal: $" + "%0.2f" % subTotal)
    print("Sales tax: $"+ "%0.2f" % tax)
    print("Your total is $" + "%0.2f" % total)

    #GUI append
    totaltxt = (('-' * 30) + '\n' + ("Subtotal: $" + "%0.2f" % subTotal) + '\n' + ("Sales tax: $"+ "%0.2f" % tax) + '\n' + ("Your total is $" + "%0.2f" % total) + '\n' ) #for GUI

    return totaltxt
        