# David Lim, 1625277

class ItemToPurchase:
  
  def __init__(self,name="none",price=0,qty=0):
    
    self.item_name = name
    self.item_price = price
    self.item_quantity = qty


  def print_item_cost(self):
    print(self.item_name + " "+ str(self.item_quantity)+" @ $"+str(self.item_price)+" = $" + str(self.item_price*self.item_quantity))


total = 0

items = []

for i in range(2):
  print("Item "+str(i+1))
  name=str(input("Enter the item name:"'\n'))
  price=int(input("Enter the item price:"'\n'))
  qty=int(input("Enter the item quantity:"'\n'))
  
  items.append(ItemToPurchase(name,price,qty))
  print()

print("TOTAL COST")

for i in items:
  i.print_item_cost()
  total = total + i.item_price*i.item_quantity

print('\n'"Total: $"+str(total))
