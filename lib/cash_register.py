#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total = 0):
         self.discount = discount 
         self.total = total
         self.items = []
      
    def add_item(self, title, price, quantity = 1):
        self.i=0
        self.price = price
        self.title = title
        self.quantity = quantity
        self.last_price=price
        self.last_title=title
        self.last_quantity=quantity

        self.total += price * quantity
        for self.i in range(quantity):
            self.items.append(title)  
        if (self.items != []):
             return (self.items)        
        
    def apply_discount(self):
        if (self.discount == 0):
            print("There is no discount to apply.")
        else:    
            self.total = self.total - (self.price * self.discount)/100
            print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        print(self.last_price, self.last_title, self.last_quantity, self.total )
        self.total = self.total - (self.price * self.quantity)
        print(self.total)
        
checkout = CashRegister()
checkout.add_item("apple", 0.99)    
checkout.add_item("tomato", 1.76) 
checkout.void_last_transaction()