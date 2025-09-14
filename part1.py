# part1.py


from datetime import datetime #importing datetime module

# Dictionary to store inventory
inventory = {}

# Read manufacturer list

with open("ManufacturerList.txt", "r") as file:
    for line in file:
        # Split line by comma to get item atributes
        parts = line.strip().split(",")

        # Extract item ID, manufacturer, item type and damaged status
        item_id = parts[0].strip()
        manufacturer = parts[1].strip()
        item_type = parts[2].strip()
        damaged = parts[3].strip() if len(parts) > 3 else "False"

        # Add item to inventory
        inventory[item_id] = {
            "manufacturer": manufacturer,
            "item_type": item_type,
            "damaged": damaged == "True",
            "price": 0, #intialize price and service date to 0
            "service_date": ""
        }

# step 3: Read and process the PriceList.txt file
with open("PriceList.txt", "r") as file:
        for line in file:
            # Split line by comma to get item atributes
            parts = line.strip().split(",") 
            item_id = parts[0].strip()
            price = int(parts[1].strip())

            # If item exists in inventory, add price
            if item_id in inventory:
                inventory[item_id]["price"] = price

# step 4: Read and process the ServiceDatesList.txt file
with open("ServiceDatesList.txt", "r") as file:
    for line in file:
        # Split by comma to get item attributes
        parts = line.strip().split(",")
        item_id = parts[0].strip()
        service_date = parts[1].strip()

        # If item exists in inventory, add service date
        if item_id in inventory:
            inventory[item_id]["service_date"] = service_date

# step 5: Sort function for FullInventory

def sort_by_manufacturer(item):
    return item[1]

# step 6: Create FullInventory.txt - all items sorted alphabetically by manufacturer
full_inventory = []

for item_id, item in inventory.items():
    full_inventory.append((item_id, item["manufacturer"], item["item_type"], item["price"], item["service_date"], item["damaged"]))

# sort by manufacturer
for i in range(len(full_inventory)):
    for j in range(i + 1, len(full_inventory)):
        if full_inventory[i][1] > full_inventory[j][1]:
            full_inventory[i], full_inventory[j] = full_inventory[j], full_inventory[i]

# Write to FullInventory.txt
with open("FullInventory.txt", "w") as file:
    for item in full_inventory:
        line = f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}"
        if item[5]:
            line += ",damaged\n"
        file.write(line + "\n")

# step 7: Sort function for ItemType Inventory Files (sort by item ID)
def sort_by_item_id(item):
    return item[0]

# step 8: Create ItemTypeInventory.txt files
item_types = {}

for item_id, item in inventory.items():
    item_type = item["item_type"]
    if item_type not in item_types:
        item_types[item_type] = []

    item_types[item_type].append((item_id, item["manufacturer"], item["price"], item["service_date"], item["damaged"]))

# Sort by item ID
for item_type, items in item_types.items():
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][0] > items[j][0]:
                items[i], items[j] = items[j], items[i]

    # Write to ItemTypeInventory.txt
    with open(f"{item_type}Inventory.txt", "w") as file:
        for item in items:
            line = f"{item[0]},{item[1]},{item[2]},{item[3]}"
            if item[4]:
                line += ",damaged\n"
            file.write(line + "\n")

# Create PastServiceDateInventory.txt
today = datetime.today()
past_service_items = []

for item_id, item in inventory.items():
    if item["service_date"]:
        service_date = datetime.strptime(item["service_date"], "%m/%d/%Y")
        if service_date < today:
            past_service_items.append((item_id, item["manufacturer"], item["item_type"], item["price"], item["service_date"], item["damaged"]))

# Sort by service date
for i in range(len(past_service_items)):
    for j in range(i + 1, len(past_service_items)):
        if datetime.strptime(past_service_items[i][4], "%m/%d/%Y") > datetime.strptime(past_service_items[j][4], "%m/%d/%Y"):
            # Swap
            past_service_items[i], past_service_items[j] = past_service_items[j], past_service_items[i]

# Write to PastServiceDateInventory.txt
with open ("PastServiceDateInventory.txt", "w") as file:
    for item in past_service_items:
        line = f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}"
        if item[5]:
            line += ",damaged\n"
        file.write(line + "\n")
# Create DamagedInventory.txt
damaged_items = []

for item_id, item in inventory.items():
    if item["damaged"]:
        damaged_items.append((item_id, item["manufacturer"], item["item_type"], item["price"], item["service_date"]))

# Sort damaged items by price
for i in range(len(damaged_items)):
    for j in range(i + 1, len(damaged_items)):
        if damaged_items[i][3] < damaged_items[j][3]: # Compare prices
            damaged_items[i], damaged_items[j] = damaged_items[j], damaged_items[i]

# Write to DamagedInventory.txt
with open("DamagedInventory.txt", "w") as file:
    for item in damaged_items:
        line = f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}"
        file.write(line + "\n")

print("Inventory processing complete. ")
print("Full Inventory:", full_inventory)
print("Item Type Inventory:", item_types)
# Debugging to ensure inventory is populated correctly
print("Inventory dictionary:", inventory)
print("Inventory processing complete. ")   
  
# git add part1.py

#Project Part 1:
#Nicely done.
#processing of damaged has logic error and doesn't pick up all damaged items (-5)
#95/100

        



        