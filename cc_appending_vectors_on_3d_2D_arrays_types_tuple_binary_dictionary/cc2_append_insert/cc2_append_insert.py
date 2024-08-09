"""
This script is authored by Behnam and is created on August, 2024.

# cc2_append_insert

This script demonstrates the usage of the append() method to add \
elements to a list.
"""

import time  # Imports the time module to use time-related functions

def main():
    """
    Main function to demonstrate the usage of the append() method.
    """
    i_index = 0  # Initialize an index variable to 0 (not used in\
    # this function)
    print("i_index =", i_index)
    x_list = []  # Initialize an empty list
    print("x_list_old[]=", x_list)  # Print the original empty list
    time.sleep(1.5)  # Pause execution for 0.5 seconds

    x_list.append(5)  # Append 5 to the list
    print("x_list_new[]=", x_list)  # Print the updated list
    # with 5 appended
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    # x_list.insert(1, 33)  # Uncomment to demonstrate the usage of the \
    # insert() method
    # print(x_list)  # Uncomment to print the list after insertion of 33 \
    # at index 1

if __name__ == "__main__":
    # Call the main function when the script is executed directly
    main()
