class Inventory:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.total_quantity = 0
        self.inventory = {}

    def add_item(self, name: str, price: float, quantity: int):
        if (self.total_quantity + quantity <= self.max_capacity) and (name not in self.inventory):
            self.inventory[name] = [price, quantity]
            self.total_quantity += quantity
            return True  # add to the inventory dictionary
        return False


    def delete_item(self, name: str):
        if name in self.inventory:
            if self.inventory.pop(name, False) != False:
                return True
        return False

    def get_items_in_price_range(self, min_price: float, max_price: float):
        # Write your code here.
        pass

    def get_most_stocked_item(self):
        largest_qty = None
        largest_keys = [] 

        if len(self.inventory) == 0:
           return None
       
        for key in self.inventory:
            if len(largest_keys) == 0:
                largest_qty = self.inventory.get(key)[1]
                largest_keys.append(key)
         
            current_key_qty = self.inventory.get(key)[1]
            
            if current_key_qty == largest_qty:
                largest_keys.append(key)
            elif current_key_qty > largest_qty:
                largest_keys = [key]

        return str(largest_keys)       
        #if len(largest_keys) == 1:
            #return largest_keys[0]

        #else:
            #eturn tuple(largest_keys)
          
           
inventory = Inventory(4)
print(inventory.add_item('Chocolate', 4.99, 4))
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Chocolate'))
print(inventory.add_item('Chocolate', 4.99, 4))
print(inventory.delete_item('Chocolate'))

#inventory = Inventory(9)

#print(inventory.add_item('Chocolate', 4.99, 1))
#print(inventory.add_item('Vanilla', 6.99, 2))
#inv = inventory.inventory
#print(inv)

#print(inventory.get_most_stocked_item())
#inventory.delete_item('Chocolate')
#print(inventory.get_most_stocked_item())
#inventory.delete_item('Vanilla')
#print(inventory.get_most_stocked_item())
