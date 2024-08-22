"""
This script is authored by Behnam and is created on August, 2024.

# cc5_append
# 15-30

This script demonstrates the usage of the append() method to add \
elements to a list.
"""

# import time  # Imports the time module, although it's not used \
# in this script

def main():
    """
    Main function to demonstrate the append() method to add elements \
    to a list.
    """

    i_index = 0  # Initialize an index variable to 0 (not used in this function)
    print("i_index = ", i_index)

    x_list = []  # Initialize an empty list
    print(x_list) # Print initial x_list

    x_list.append(0)  # Append 0 to the empty list

    print(x_list)  # Print the list after appending 0, which will output: [0]

    x_list.append(1)  # Append 1 to the list

    print(x_list)  # Print the list after appending 1, which will output: [0, 1]

    x_list.append(2)  # Append 2 to the list

    print(x_list)  # Print the list after appending 2, which will output: [0, 1, 2]

    # The following lines are commented out, so they do not execute:

    # x_list.insert(1,33)  # Uncomment to insert 33 at index 1 of the list

    # print(x_list)  # Uncomment to print the list after inserting 33

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
