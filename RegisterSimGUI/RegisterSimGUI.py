from breezyGUI import EasyFrame
from tkinter import *
import RegisterSim


class program(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title= "Grocery Store checkout UI", background="gray")
        #labels
        self.addLabel(text = "Item ID:", row = 0, column = 0)
        self.addLabel(text = "QTY/ Weight(lbs):", row = 1, column = 0)
        #fields
        self.IDField = self.addTextField(text = "", row = 0, column = 1)
        self.measurementField = self.addIntegerField(value = 0, row = 1, column = 1)

        self.IO = self.addTextArea(text = "", column = 6, row = 0, )  

        #command buttons
        self.addButton(text = "Add Item to cart", row = 0, column = 2, command = self.addtocart)
        self.addButton(text = "Remove Item from cart", row = 0, column = 3, command = self.removeitem)
        self.addButton(text = "Checkout", row = 3, column = 4, command = self.checkout)

    def addtocart(self):
        itemID = self.IDField.getText()
        measurement = self.measurementField.getValue()
        RegisterSim.additem(itemID, float(measurement)) #DEBUG: CAN BE REMOVED AFTERWARDS, replaced by following statement
        #self.IO.appendText(RegisterSim.additem(itemID, float(measurement)))
        #self.IO.appendText(RegisterSim.additem(itemID, float(measurement))) #works
        self.cartupdate()
        

    def removeitem(self):
        itemID = self.IDField.getText()
        RegisterSim.removelist(itemID)
        self.cartupdate()

    def checkout(self):
        #RegisterSim.checkout() #computes total in cli
        self.IO.appendText(RegisterSim.checkout())

    def cartupdate(self):
        self.IO.setText('')
        for x in RegisterSim.itemlist:
            self.IO.appendText(str(x.get('Qty')) + " " + x.get('Item') + " " + "$%.02f" % x.get('Total') + '\n' )


def main():
    program().mainloop()

if __name__ == "__main__":
    main()