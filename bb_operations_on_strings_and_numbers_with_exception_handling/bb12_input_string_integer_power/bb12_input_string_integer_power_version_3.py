"""
This script is authored by Behnam and is created on July 19, 2024.

bb12_input_string_integer_power

This script takes a string and two integers as input and calculates
the result of the base number raised to the power of the power number.
"""

# while 1:  # Starts an infinite loop to repeatedly execute the code
# while (1) unnecessary parentheses.
def main():
    """
    Main function to take user input for a string and two integers,
    and calculate the power.
    """
    # Prompts user to enter a string value
    string_input = input('Enter string value:')
    # Prints the received string value
    print('received =', string_input)
    # Prompts user to enter an integer for base_number
    # and converts it to an integer
    base_number = int(input('Enter Base Number:'))

    # Prompts user to enter an integer for power_number
    # and converts it to an integer
    power_number = int(input('Enter Power Number:'))

    # Calculates base_number raised to the power of power_number
    # and prints the result
    # print(base_number ** power_number)
    print(f"Power Calculation: {base_number ** power_number}")
    # Checks if the script is being run directly
    # if __name__ == "__main__": main()

# if __name__ == "__main__":
# main()
while 1:
    main()

    # Calls the main function to execute the script logic
