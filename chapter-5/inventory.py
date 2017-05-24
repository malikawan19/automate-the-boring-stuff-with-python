'''
Project Description:

List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
Dictionaries and Structuring Data 121
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item. Your code could look something like this:

def addToInventory(inventory, addedItems):
# your code goes here
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
The previous program (with your displayInventory() function from the
previous project) would output the following:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
'''


inv = {'gold coin': 42, 'rope': 1} # Our initial inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems: #loop through each item in the dragonLoot list
        if i in inventory.keys(): #if the name of item in dragonLoot is available as key in the inv dictionary
            inventory[i] += 1 # increment the value in the dictionary for that key
        else:
            inventory.setdefault(i, 0) # Create a new key if doesn't exist and set it to 0 as the default value
            inventory[i] += 1 # Now that the key exists, increment it
    return inventory # return the latest inventory dictionary


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
