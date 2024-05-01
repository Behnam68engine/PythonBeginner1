# bb6_string_integer_conversion_summation_errors
# bb1 1:00 ...1:24:36 types of print

"""
This script demonstrates different types of print statements and basic arithmetic operations.
"""

def main():
    """
    Main function to demonstrate different types of print statements
    and basic arithmetic operations.
    """
    a_value = 222  # Assigns integer value 222 to variable a_value.
    b_value = 0.1  # Assigns float value 0.1 to variable b_value.
    c_value = "Hello"  # Assigns string "Hello" to variable c_value.
    d_value = '333'  # Assigns string '333' to variable d_value.

    print('value', a_value) # Prints a label 'value' followed by the value of a_value.
    print(a_value, b_value, c_value) # Prints the values of a_value, b_value, and c_value.
    # print(a_value + d_value) # False: int & str can't be added together

    print(a_value + int(d_value))
    # Converts d_value to an integer
    # and adds it to a_value, then prints the result.

    x_value = a_value + int(d_value) + 1
    # Adds a_value and the integer representation of
    # d_value, then adds 1, and assigns it to x_value.

    print('x=', x_value) # Prints the value of x_value along with a label 'x='.
    print(str(a_value) + d_value)
    # Converts a_value to a string and concatenates
    # it with d_value, then prints the result.


if __name__ == "__main__":
    main()
    