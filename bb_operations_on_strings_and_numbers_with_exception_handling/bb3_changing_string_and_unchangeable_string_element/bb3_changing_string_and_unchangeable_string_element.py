"""
This script demonstrates variable assignments and string indexing.

Functions:
    main: Main function to demonstrate variable assignments and string indexing.
"""

def main():
    """
    Main function to demonstrate variable assignments and string indexing.
    """
    a_value = 0  # Assigning integer value 0 to variable a_value
    b_value = 0.1  # Assigning float value 0.1 to variable b_value
    c_value = "Hello"  # Assigning string "Hello" to variable c_value

    print(a_value, b_value, c_value)  # Printing the values of variables a_value, b_value, and c_value

    print(c_value[0])  # Printing the first character of string c_value
    print(c_value[2])  # Printing the third character of string c_value
    print(c_value[1])  # Printing the second character of string c_value
    print(c_value[3])  # Printing the fourth character of string c_value

    # c_value[1] = t  # Attempting to modify the second character of string c_value, which will raise an error
    # c_value[1]='A'  # Attempting to modify the second character of string c_value, which will raise an error

    # c_value[1] = A === False, Because inner elements cannot be changable

    c_value = "Behnam"  # Reassigning the entire string variable c_value to "Behnam"
    print(c_value)
    # True, Because the entire string variable can be changed

    if c_value[0] == c_value[2]:  # Checking if the first character of c_value is equal to the third character
        print(2)  # If condition is true, printing 2


if __name__ == "__main__":
    main()  # Calling the main function if the script is executed directly
