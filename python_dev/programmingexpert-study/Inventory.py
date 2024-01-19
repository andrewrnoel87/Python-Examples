class Inventory:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.item_count = 0
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int):
        if (self.item_count + quantity <= self.max_capacity) and (name not in self.items):
            self.items[name] = {'name': name, 'price': price, 'quantity': quantity}
            self.item_count += quantity
            return True 
        
        return False


    def delete_item(self, name: str):
        if name not in self.items:
            return False
      
        self.item_count -= self.items[name]['quantity']
        del self.items[name]
        return True
        


    def get_items_in_price_range(self, min_price: float, max_price: float):
        items_in_price_range = []

        for name in self.items:
            if min_price <= self.items[name]['price'] <= max_price:
                items_in_price_range.append(name)

        return items_in_price_range

    def get_most_stocked_item(self):
        
        most_stocked_item = None 
        most_stocked_item_qty = 0
       
        for name in self.items:

            if self.items[name]['quantity'] > most_stocked_item_qty:
                most_stocked_item = name
                most_stocked_item_qty = self.items[name]['quantity']

        return most_stocked_item
          
           
#inventory = Inventory(4)
#print(inventory.add_item('Chocolate', 4.99, 4))
#print(inventory.delete_item('Chocolate'))
#print(inventory.delete_item('Chocolate'))
#print(inventory.delete_item('Chocolate'))
#print(inventory.add_item('Chocolate', 4.99, 4))
#print(inventory.delete_item('Chocolate'))

inventory = Inventory(99)

print(inventory.add_item('Chocolate', 4.99, 6))
print(inventory.add_item('Vanilla', 6.99, 2))
print(inventory.items)
print(inventory.get_most_stocked_item())
print(inventory.items)
print(inventory.delete_item('Chocolate'))
print(inventory.items)
print(inventory.get_most_stocked_item())
print(inventory.delete_item('Vanilla'))
print(inventory.items)
print(inventory.get_most_stocked_item())
print(inventory.add_item('Chocolate', 14.99, 9))
print(inventory.items)
print(inventory.get_most_stocked_item())
print(inventory.get_items_in_price_range(.99, 19.99))
print(inventory.add_item('Vanilla', 16.99, 2))
print(inventory.add_item('Cookie', 3.99, 2))
print(inventory.add_item('Chicken', 10, 2))
print(inventory.add_item('Bread', 19.99, 2))
print(inventory.get_items_in_price_range(.99, 19.99))
print('\n')
print(inventory.items.items())
print('\n')
print(inventory.items.values())
