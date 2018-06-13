stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope']

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(k + ": " + str(v))
        item_total += v
    print("\nTotal number of items: " + str(item_total))
def addToInventory(inventory, addeditems):
    for items in addeditems:
        if items not in inventory:
            inventory[items] = 1
        else:
            itemValue = 0
            itemValue = inventory.get(items)
            itemValue += 1
            inventory.update({items: itemValue})
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
