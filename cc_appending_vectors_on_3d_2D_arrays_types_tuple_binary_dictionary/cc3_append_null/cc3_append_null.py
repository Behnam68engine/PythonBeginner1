"""
This script is authored by Behnam and is created on July, 2024.

# cc3_append_null

This script demonstrates the usage of the append() and insert() \
methods to add elements to a list. Also it show how we can create \
a row vector by an empty null array in version 2.
"""

import time  # Imports the time module to use time-related functions

def main():
    """
    Main function to demonstrate appending and inserting elements \
    into a list.
    """
    # Version 1
    print("version1:\n")  # Print a header for version 1 of the \
    # demonstration

    i_index = 0  # Initialize an index variable to 0 \
    # (not used in this function)

    print("i_index = ", i_index)

    x_list = [0, 1, 2, 3, 4]  # Initialize a list with elements 0 to 4

    print('x_list =\n ', x_list, '\n')  # Print the initial list

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(5)  # Append 5 to the list

    print("x_list.append(5) to x_list:\n", x_list, '\n')
    # Print the list after appending 5

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(6)  # Append 6 to the list

    print("x_list.append(6) to x_list:\n", x_list, '\n')
    # Print the list after appending 6

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(7)  # Append 7 to the list

    print("x_list.append(7) to x_list:\n", x_list, '\n')
    # Print the list after appending 7

    time.sleep(2.5)  # Pause execution for 2.5 seconds

    x_list.insert(2, 33)  # Insert 33 at index 2 of the list

    print("x_list.insert(2, 33)=\n", x_list, '\n')
    # Print the list after inserting 33

    time.sleep(1)  # Pause execution for 1 second

    print('end of version1.\n')  # Print a footer for version 1

    time.sleep(4.5)  # Pause execution for 4.5 seconds

    # Version 2
    print("version2:\n")  # Print a header for version 2 of the \
    # demonstration

    i_index = 0  # Initialize an index variable to 0 \
    # (not used in this function)

    x_list = []  # Initialize an empty list

    print('x_list =\n ', x_list, '\n')  # Print the initial empty list

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(0)  # Append 0 to the list

    print("x_list.append(0) to x_list:\n", x_list, '\n')
    # Print the list after appending 0

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(1)  # Append 1 to the list

    print("x_list.append(1) to x_list:\n", x_list, '\n')
    # Print the list after appending 1

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list.append(2)  # Append 2 to the list

    print("x_list.append(2) to x_list:\n", x_list, '\n')
    # Print the list after appending 2

    time.sleep(2.5)  # Pause execution for 2.5 seconds

    x_list.insert(1, 3333)  # Insert 3333 at index 1 of the list

    print("x_list.insert(1, 3333)=\n", x_list, '\n')
    # Print the list after inserting 3333

    time.sleep(0.5)  # Pause execution for 0.5 seconds

    time.sleep(0.5)  # Additional 0.5-second pause (redundant)

    print('end of version2.\n\n\n')  # Print a footer for version 2 \
    # with extra new lines

    time.sleep(24.5)  # Pause execution for 24.5 seconds
while True:  # Starts an infinite loop to continuously execute the script
    if __name__ == "__main__":
        main()  # Call the main function when the script is executed directly
