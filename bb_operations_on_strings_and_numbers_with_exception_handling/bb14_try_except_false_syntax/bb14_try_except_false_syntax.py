"""
This script is authored by Behnam and is created on July 21, 2024.

# bb14_try_except_false_syntax

This script prompts the user to enter a value, a base number, and a
power number. It calculates the result of the base number raised to
the power of the power number. It handles exceptions if non-integer
values are entered. But in the matter of fact it's showing the false
syntax (for solving it we should write the calculation inside
the "try:" part)
"""

def main():
    """
    Main function to prompt the user for input and handle exceptions.
    """
    # Prompting the user to enter a value and storing it in
    # value_input variable
    value_input = input('Enter value:')

    # Printing the received value
    print('received =', value_input)

    # Trying to convert user input to an integer for the base number
    try:
        base_number = int(input('Enter Number:'))
    # Handling the ValueError exception if non-integer value is entered
    except ValueError:
        print("Error! Enter Integer Value!")

    # Trying to convert user input to an integer for the power number
    try:
        power_number = int(input('Enter Pow:'))
    # Handling any exception (not specified) if non-integer value
    # is entered
    except ValueError:
        print("Error! Enter Integer Value!")

    # Printing the result of the base number raised to the power of
    # the power number
    # This is incorrect because it doesn't handle the case where
    # an error occurs in the above try blocks.
    print(base_number ** power_number)

    # The former code i.e. bb13_try_except.py has a better syntax
    # and don't keep on the wrong code to the error!!
    # This is false syntax because print(x**y) is run and runtime error
    # is shown because this line i.e. print(x**Y), so you should write like
    # bb13 (write the "print(base_number ** power_number)" inside try
    # like the bb13_try_except.py not external use like this code!!!'''

while 1:  # Starts an infinite loop to repeatedly execute the code
    # Running the main function if the script is executed directly
    if __name__ == "__main__":  \
        # Calls the main function to execute the script logic
        main()
