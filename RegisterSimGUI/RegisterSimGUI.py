from breezyGUI import EasyFrame
from tkinter import *
import RegisterSim
from playsound import playsound


class program(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title= "Grocery Store checkout UI", background="blue", height = 250, width = 1300)
        #labels
        self.addLabel(text = "Item ID:", font = ('Arial', 30) , row = 0, column = 0, sticky = 'nsew')
        self.addLabel(text = "QTY/ Weight(lbs):",font = ('Arial', 30), row = 1, column = 0, sticky = 'nsew')
        #fields
        self.IDField = self.addTextField(text = "", row = 0, column = 1, sticky = 'nsew' )
        self.measurementField = self.addIntegerField(value = 0, row = 1, column = 1, sticky = 'nsew' )

        self.IO = self.addTextArea(text = "", column = 6, row = 0, rowspan = 2, height = 10 )  

        #command buttons
        self.addButton(text = "Add Item to cart", row = 0, column = 2, columnspan=1, rowspan = 1, command = self.addtocart)
        self.addButton(text = "Remove Item from cart", row = 0, column = 2, rowspan = 2, command = self.removeitem)
        self.addButton(text = "Checkout", row = 1, column = 2, rowspan = 2, command = self.checkout)

    def addtocart(self):
        itemID = self.IDField.getText()
        measurement = self.measurementField.getValue()
        if RegisterSim.additem(itemID, float(measurement)) == 'Item Not found\n':
            playsound('sounds/404.mp3')
        else:
            self.cartupdate()
            playsound('sounds/addsound.mp3')
            return
        

    def removeitem(self):
        itemID = self.IDField.getText()
        RegisterSim.removelist(itemID)
        self.cartupdate()

    def checkout(self):
        #RegisterSim.checkout() #computes total in cli
        self.IO.appendText(RegisterSim.checkout())
        playsound('sounds/checkout.mp3')

    def cartupdate(self):
        self.IO.setText('')
        for x in RegisterSim.itemlist:
            self.IO.appendText(str(x.get('Qty')) + " " + x.get('Item') + " " + "$%.02f" % x.get('Total') + '\n' )


def main():
    program().mainloop()

if __name__ == "__main__":
    main()