import tkinter as tk
class CustomerOrder(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Topping Select")
        self.addLabel(text="Select Your Toppings", row=0, column=0)
        self.cheeseCB = tk.Checkbutton(self, text="Cheese")
        self.cheeseCB.grid(row=1, column=0)
        self.pepperoniCB = tk.Checkbutton(self, text="Pepperoni")
        self.pepperoniCB.grid(row=2, column=0)
        self.mushroomsCB = tk.Checkbutton(self, text="Mushrooms")
        self.mushroomsCB.grid(row=3, column=0)
        self.onionsCB = tk.Checkbutton(self, text="Onions")
        self.onionsCB.grid(row=1, column=1)
        self.sausageCB = tk.Checkbutton(self, text="Sausage")
        self.sausageCB.grid(row=2, column=1)
        self.blackolivesCB = tk.Checkbutton(self, text="Black Olives")
        self.blackolivesCB.grid(row=3, column=1)
        self.greenpappersCB = tk.Checkbutton(self, text="Green Peppers")
        self.greenpappersCB.grid(row=1, column=2)
        self.pineappleCB = tk.Checkbutton(self, text="Pineapple")
        self.pineappleCB.grid(row=2, column=2)
        self.hamCB = tk.Checkbutton(self, text="Ham")
        self.hamCB.grid(row=3, column=2)
        self.addButton("Place Order", 4, 0, 3, self.placeOrder)
    def addLabel(self, text, row, column):
        label = tk.Label(self, text=text)
        label.grid(row=row, column=column)
    def addButton(self, text, row, column, columnspan, command):
        button = tk.Button(self, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan)
    def placeOrder(self):
        # Add your place order logic here
        pass
# Create an instance of the CustomerOrder class
app = CustomerOrder()
# Start the GUI application
app.mainloop()