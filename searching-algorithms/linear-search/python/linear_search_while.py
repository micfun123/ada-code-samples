# Raspberry Pi Foundation
# Developed as part of Ada Computer Science
# 
# Usage licensed under CC BY-NC-SA 4.0


def linear_search_version_2(items, search_item):
    """A linear search algorithm that stops iterating if the item is found"""
       
    # Initialise the variables
    found_index = -1
    current = 0
    found = False

    # Repeat while the end of the list has not been reached
    # and the search item has not been found
    while current < len(items) and found == False:
        print(f"Checking index {current} with value {items[current]}")
        
        # Compare the item at the current index to the search item
        if items[current] == search_item:
            # If the item has been found, store the current index
            found_index = current 
            found = True # Raise the flag to stop the loop
            print("Item found! Stopping the search")

        current = current + 1 # Go to the next index in the list

    # Return the index of the search_item or -1 if not found
    return found_index


def main():
    """Perform a linear search on the test data"""
    test_items = [11,25,10,29,15,13,18]
    
    print("### Linear search version 2 (while loop) ###")
    print(test_items)

    # Search for a value and return the found index
    item_to_find = 15
    print(f"\nThe search item is {item_to_find}\n")
    index = linear_search_version_2(test_items, item_to_find)

    if index == -1:
        print(f"\n{item_to_find} was not found in the list")
    else:
        print(f"\n{item_to_find} was found at index {index}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
