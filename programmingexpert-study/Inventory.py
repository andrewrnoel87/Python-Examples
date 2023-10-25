class Inventory:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.item_count = 0
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int):
        if (self.item_count + quantity <= self.max_capacity) and (name not in self.inventory):
            self.inventory[name] = {'name': name, 'price': price, 'quantity': quantity}
            self.total_quantity += quantity
            return True 
        return False


    def delete_item(self, name: str):
        if name not in self.inventory:
            return False
        for key in self.inventory:
            if name == key:
                self.total_quantity -= self.inventory.get(key)[1]
                del self.inventory[name]
                return True
        


    def get_items_in_price_range(self, min_price: float, max_price: float):
        # Write your code here.
        pass

    def get_most_stocked_item(self):
        largest_qty = 0
        largest_key = None 

        if len(self.inventory) == 0:
           return None
        else:
            first_key = self.inventory.popitem()

            largest_qty = first_key[1][1]
            largest_key = first_key[0]
         
            self.inventory[first_key[0]] = [first_key[1][0], first_key[1][1]]
       
        for key in self.inventory:
            if key not in largest_key:

                current_key_qty = self.inventory.get(key)[1]
                    
                if current_key_qty > largest_qty:
                    
                    largest_qty = current_key_qty
                    largest_keys = key
                    
        return largest_key

          
           
#inventory = Inventory(4)
#print(inventory.add_item('Chocolate', 4.99, 4))
#print(inventory.delete_item('Chocolate'))
#print(inventory.delete_item('Chocolate'))
#print(inventory.delete_item('Chocolate'))
#print(inventory.add_item('Chocolate', 4.99, 4))
#print(inventory.delete_item('Chocolate'))

inventory = Inventory(9)

print(inventory.add_item('Chocolate', 4.99, 6))
print(inventory.add_item('Vanilla', 6.99, 2))
inv = inventory.inventory
print(inv)

#print(inventory.delete_item('Chocolate'))
print(inventory.get_most_stocked_item())
print(inventory.inventory)
print(inventory.delete_item('Chocolate'))
print(inventory.get_most_stocked_item())
print(inventory.delete_item('Vanilla'))
print(inventory.get_most_stocked_item())
