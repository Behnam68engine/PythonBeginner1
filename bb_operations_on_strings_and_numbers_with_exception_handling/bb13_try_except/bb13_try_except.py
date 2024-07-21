"""
This script is authored by Behnam and is created on July 21, 2024.

# bb13_try_except

This script prompts the user to enter a value and two numbers, then
calculates the result of the first number raised to the power of the
second number. It handles exceptions if non-integer values are entered.
"""

def main():
    """
    Main function to prompt the user for input and handle exceptions.
    """
    # Prompts user to enter a value
    value_input = input('Enter value:')
    # Prints the received value
    print('received =', value_input)
    try:  # Starts a try block to catch exceptions
        # Prompts user to enter an integer for base_number
        base_number = int(input('Enter Number:'))
        # Prompts user to enter an integer for power_number
        power_number = int(input('Enter Pow:'))
        # Calculates base_number raised to the power of power_number
        # and prints the result
        print(base_number ** power_number)
    except ValueError:  # Catches ValueError exceptions
        # Prints an error message if a non-integer value is entered
        print("Error! Enter Integer Value!")

while 1:  # Starts an infinite loop to repeatedly execute the code
    if __name__ == "__main__":\
        # Checks if the script is being run directly
        main()  # Calls the main function to execute the script logic
