# program made by tst_off,  you can edit this program as you wish, but please give credit to me if you use this program in your own projects, thanks!
# vA.1.0.0 (considered alpha) - main UI (10-17-2026 4:20:45 PM cst) - added everything, first version of the program... will add an item description soon!
# i sound so much like napstablook :p

def unpack(class_name): #idk this part of the code is a bit confusing but it works so i guess its fine
    values_list = [
        value for key, value in vars(class_name).items() 
        if not key.startswith("__")
    ]
    return values_list #returns the unpacked values of the class as a list

class items: #all items are defined here, if you want to add more items, add them here
    item_vars = ["item ID", "is inventory", "removable", "Addable"] #if you add more item behaviors, add them here and in the item classes below
    class usable_item: #item :p
        name = "usable_item"
        inventory = False
        removable = True
        Addable = True

    class usable_item2: #item again :p
        name = "usable_item2"
        inventory = False
        removable = True
        Addable = True

    class unremovable_item: #test of an unremovable item, this item cannot be removed from the inventory once added
        name = "unremovable_item"
        inventory = False
        removable = False
        Addable = True

    class inaddable_item: #test of an inaddable item, this item cannot be added to the inventory (but if in inventory by default, it stays)
            name = "inaddable_item"
            inventory = False
            removable = True
            Addable = False
    #will add more items later, but for now this is all the items that are defined

    

items.item_names = [ #idk this part again...
    name #what?
    for name, cls in vars(items).items()
    if isinstance(cls, type)
]

class inventory: #inventory class, this is where the inventory is defined and controlled
    class inventory_vars:
        slots = 10 #maximum number of items addable in the inventory, if you want to change the maximum number of slots, change this value
        items = [unpack(item) for item in [items.usable_item, items.usable_item2, items.unremovable_item, items.inaddable_item]] #the default items in the inventory, if you want to add more default items, add them here


class controls: # controls class, this is where the inventory is controlled
    def inventory_controls(ic_items, max_slots): #oh no
        new_items = ic_items #new items is a copy of the current items in the inventory by default, this is used to modify the inventory without modifying the original list
        item_names = "\n".join([f"  {i+1}: {ic_items[i][0]}" for i in range(len(ic_items))]) #these are the item names in the inventory turned into a readable format, this is used to display the items in the inventory for the UI
        inp_action = input(f"What do you want to do with the inventory?\n\nslots:\n {item_names}\n\n1: Add\n2: Remove\n3: show defined items (reccomended before adding)\n4: show info of item (reccomended before adding and deleting)\n") #the input for what action the user wants to take with the inventory, this is used to control the inventory 

        if inp_action == "1": #add a new item to the inventory
                if len(new_items) < max_slots: #if the inventory is not full, the user can add a new item
                    item_name = str(input("item ID?\n")) #the user inputs the item ID of the item they want to add
                    if hasattr(items, item_name): #if the item ID exists in the items class, the user can add the item
                        item_unpacked = unpack(getattr(items, item_name)) #unpack the item class into a list of values
                        if item_unpacked[3] == True: #if the item is addable, the user can add the item
                            new_items.append(item_unpacked) #add the unpacked item to the new items list
                            inventory.inventory_vars.items = new_items #update the inventory with the new items list
                            print(f"{item_unpacked[0]} added to inventory") #print a message saying that the item was added to the inventory
                            controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
                        else:
                            print(f"{item_unpacked[0]} is inaddable and cannot be added to inventory :(") #print a message saying that the item is inaddable and cannot be added to the inventory
                            controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
                    else:
                        print(f"{item_name} is not a defined item") #print a message saying that the item ID does not exist in the items class
                        controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
                else:
                    print("inventory is full, cannot add more items") #print a message saying that the inventory is full and the user cannot add more items
                    controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
        elif inp_action == "2": #remove an item from the inventory
            item_num = int(input("slot number?\n")) #asks for slot number of the item to be removed
            if 1 <= item_num <= len(ic_items): #if the slot number is valid, the user can remove the item
                item_unpacked = ic_items[item_num-1] #unpack the item class into a list of values
                if item_unpacked[2] == True: #if the item is removable, the user can remove the item
                    removed_item = new_items.pop(item_num-1) #remove the unpacked item from the new items list (and store it in a variable to print later)
                    inventory.inventory_vars.items = new_items #update the inventory with the new items list
                    print(f"{removed_item[0]} removed from inventory") #prints a message saying that the item was removed from the inventory
                    controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
                else: #if the item is unremovable, the user cannot remove the item
                    print(f"{item_unpacked[0]} is unremovable and cannot be removed from inventory :(") # D:
                    controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
        elif inp_action == "3": #show defined items
            item_names_sentenced = "\n".join([f"  {i+1}: {items.item_names[i]}" for i in range(len(items.item_names))]) #this is the item names in the items class turned into a readable format
            print(f"defined items:\n{item_names_sentenced}\n\n\n") #print the items
            controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory
        elif inp_action == "4": #show info of item
            item_name = str(input("item ID?\n")) #the user inputs the item ID of the item they want to see the info of
            item_info = unpack(getattr(items, item_name)) #unpack the item class into a list of values
            item_info_sentenced = "\n".join([f"  {items.item_vars[i]}: {item_info[i]}" for i in range(len(item_info))]) #this is the item info turned into a readable format
            print(f"{item_name} info:\n{item_info_sentenced}\n\n\n") #print the item info
            controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #call the inventory controls function again to allow the user to continue controlling the inventory

# wow that was long... overuse of comments but i think it was necessary to explain the code, if you have any questions about the code, feel free to ask me on discord! (acronym_of_262144) or yt (@tst_off)

controls.inventory_controls(inventory.inventory_vars.items, inventory.inventory_vars.slots) #run the inventory controls function to start the program

#yeah thats all ._.
