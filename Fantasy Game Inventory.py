stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))


dragonLoot =['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
        
    
print('You just slayed the final boss \"Twin-headed Dragon\" \n')
print('You picked up the following items: ' + str(dragonLoot) + '\n')

addToInventory(stuff, dragonLoot)
displayInventory(stuff)





