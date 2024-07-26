"""
This script is authored by Behnam and is created on July, 2024.

# bb15_try_except_second_false_syntax

This script prompts the user to enter a value, a base number, and a \
power number. It calculates the result of the base number raised to \
the power of the power number. It handles exceptions if non-integer \
values are entered.
"""

def main():
    """
    Main function to prompt the user for input and handle exceptions.
    """
    # Prompting the user to enter a value and storing it in value_input variable
    value_input = input('Enter value:')

    # Printing the received value
    print('received =', value_input)

    # Trying to convert user input to an integer for the base number
    try:
        base_number = int(input('Enter Number:'))
    # Handling any exception (not specified) if non-integer value
    #  is entered
    except ValueError:  # except ValueError:
        # ValueError is a keyword.
        print("Error! Enter Integer Value!")

    # Trying to convert user input to an integer for the power number
    try:
        power_number = int(input('Enter Pow:'))
    # Handling any exception (not specified) if non-integer value
    # is entered
    except ValueError:  # except ValueError:
        # ValueError is a keyword.
        print("Error! Enter Integer Value!")

    # Trying to calculate the result and print it
    try:
        result = base_number ** power_number
        print(f"The result of {base_number} raised to the power of \
{power_number} is {result}")
    except UnboundLocalError as e_1:
        # Handling any exceptions that might occur during the calculation
        # This handles cases where base_number or power_number are not defined
        print(f"An error occurred: {e_1}")
        # pass  # This line is commented out but would be used to do nothing

    # The two former codes i.e. bb13_try_except have a better syntax \
    # and don't keep on the wrong code to the error!!

# This is also incorrect syntax because when you enter a non-integer \
# value, the print(x**y) statement will continue to execute. Even \
# though a runtime error is not displayed, unlike in bb13_try_except, \
# it prompts unnecessarily for the power input!!!
while 1:  # Infinite loop to continuously prompt the user
    # Running the main function if the script is executed directly
    if __name__ == "__main__": \
        main()
        # Calls the main function to execute the script logic
