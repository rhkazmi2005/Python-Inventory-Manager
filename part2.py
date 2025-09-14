
# part2.py #
# CIS 1348 - Spring 2025 #
# Project Part 2 - Inventory Management System. #
# Classes are used. Pandas is prohibited. Code is extensively commented. #

import datetime

# Class to represent an item in the inventory #
class Inventory:
    def __init__(self):
        # Initialize empty list to store items #
        self.items = []


    def add_item(self, item_id, manufacturer, item_type, price, service_date, damaged):
        # Add item to the list
        self.items.append({
            'item_id': item_id,
            'manufacturer': manufacturer.strip().lower(),
            'item_type': item_type.strip().lower(),
            'price': int(price),
            'service_date': datetime.datetime.strptime(service_date.strip(), '%m/%d/%Y'),
            'damaged': damaged.strip().lower() == 'damaged'

        })

    def is_valid(self, item):
        # Check if the item is valid, not damaged and not passed service date                 #
        return not item['damaged'] and item['service_date'] > datetime.datetime.now()

    def query_item(self, manufacturer, item_type):
        # Find the most expensive valid item matching the manufacturer and type.              #
        # Also find an alternative item with the closest price from a different manufacturer. #
        manufacturer = manufacturer.lower()
        item_type = item_type.lower()

        # Find matching items
        matched_items = [item for item in self.items if 
                         manufacturer == item['manufacturer'] and
                         item_type == item['item_type'] and
                         self.is_valid(item)]

        if not matched_items:
            return None, None

        # Find the most expensive item and sort by price descending
        matched_items.sort(key=lambda x: x['price'], reverse=True) 
        selected_items = matched_items[0]

        # Find an alternative item with the closest price from a different manufacturer
        alternatives = [item for item in self.items if
                        item['item_type'] == item_type and
                        item['manufacturer'] != manufacturer and
                        self.is_valid(item)]

        if alternatives:
            # Sort by price difference (smallest first), then by price (highest first)
            alternatives.sort(key=lambda x: (abs(x['price'] - selected_items['price']), -x['price']))
            alternative = alternatives[0]

        else:
            alternative = None

        return selected_items, alternative

    def search(self, user_input):
        # Process user input, extract manufacturer and type, print the results #
        words = user_input.lower().split()
        manufacturers = set()
        item_types = set()
        
        # Identify words matching manufacturer and item type
        for item in self.items:
            for word in words:
                if word == item['manufacturer']:
                    manufacturers.add(word)
                if word == item['item_type']:
                    item_types.add(word)

        # Handle invalid queries
        if len(manufacturers) != 1 or len(item_types) != 1:
            print("No such item in inventory.")
            return

        manufacturer = manufacturers.pop()
        item_type = item_types.pop()

        selected_item, alternative_item = self.query_item(manufacturer, item_type)

        if selected_item:
            print(f"Your item is: {selected_item['item_id']}, {selected_item['manufacturer'].title()}, {selected_item['item_type'].title()}, ${selected_item['price']}")
            if alternative_item:
                print(f"You may, also, consider: {alternative_item['item_id']}, {alternative_item['manufacturer'].title()}, {alternative_item['item_type'].title()}, ${alternative_item['price']}")
        else:
            print("No such item in inventory.")

def main():
    "Main function to run inventory system"
    inventory = Inventory()

    # Example data; replace this with loading from your Part 1 inventory if needed
    inventory.add_item('1', 'Apple', 'Laptop', '1200', '12/12/2025', 'not damaged')
    inventory.add_item('2', 'Dell', 'Laptop', '1000', '01/01/2026', 'not damaged')
    inventory.add_item('3', 'Apple', 'Phone', '800', '11/11/2025', 'damaged')
    inventory.add_item('4', 'Samsung', 'Phone', '900', '10/10/2026', 'not damaged')

    while True:
        user_input = input("\nPlease enter your query (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Thank you for using the inventory system. Goodbye!")
            break
        inventory.search(user_input)

# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
            




