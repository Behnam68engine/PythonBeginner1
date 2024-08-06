"""
This script is authored by Behnam and is created on July, 2024.

# cc1_vector

This script demonstrates the manipulation of elements in a list.
"""

import time  # Imports the time module to use time-related functions


def main():
    """
    Main function to manipulate elements in a list.
    """
    i_index = 0  # Initialize index variable to 0

    x_list = [0, 1, 2, 3, 4]  # Create a list with initial elements
    print("x_list_old[]=", x_list)  # Print the original list
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    print("x_list[3]=", x_list[3])
    # Print the element at index 3 of the list
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    x_list[3] = 77  # Update the element at index 3 to 77
    print("x_list_new[]=", x_list)
    # Print the updated list
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    print(x_list[i_index])
    # Print the element at index i_index (initially 0)
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    # print("x_list[%d]=" % i_index, x_list[i_index]) # old format
    print(f"x_list[{i_index}] =", x_list[i_index])
    # Print the element at index i_index with its index
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    i_index += 1  # Increment i_index to point to the next element
    # print("x_list[%d]=" % i_index, x_list[i_index]) # old format
    print(f"x_list[{i_index}] =", x_list[i_index])
    # Print the next element with its index
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    i_index += 1  # Increment i_index to point to the next element
    # print("x_list[%d]=" % i_index, x_list[i_index]) # old format
    print(f"x_list[{i_index}] =", x_list[i_index])
    # Print the next element with its index
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    i_index += 1  # Increment i_index to point to the next element
    # print("x_list[%d]=" % i_index, x_list[i_index]) # old format
    print(f"x_list[{i_index}] =", x_list[i_index])
    # Print the next element with its index
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    i_index += 1  # Increment i_index to point to the next element
    # print("x_list[%d]=" % i_index, x_list[i_index]) # old format
    print(f"x_list[{i_index}] =", x_list[i_index])

    # Print the next element with its index
    time.sleep(0.5)  # Pause execution for 0.5 seconds



    time.sleep(10.5)  # Pause execution for 10.5 seconds
    print("\n\n\n")  # Print new lines for separation

while 1:
    # Or while True: infinite loop to continuously execute the script
    if __name__ == "__main__":
        main()
        # Call the main function when the script is executed directly
