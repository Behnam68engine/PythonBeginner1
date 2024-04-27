"""
This script demonstrates variable assignments and string indexing.
"""

def main():
    """
    Main function to demonstrate variable assignments and string indexing.
    """
    # Assigning values to variables
    a_value = 0  # Assigning integer value 0 to variable a_value
    b_value = 0.1  # Assigning float value 0.1 to variable b_value
    c_value = "Hello"  # Assigning string "Hello" to variable c_value
    
    # Printing the values of variables
    print(a_value, b_value, c_value)

    # Accessing characters of the string and printing them
    print(c_value[0])  # Printing the first character of string c_value
    print(c_value[2])  # Printing the third character of string c_value
    print(c_value[1])  # Printing the second character of string c_value
    print(c_value[3])  # Printing the fourth character of string c_value
    
    # Attempting to modify a string character (will raise an error)
    # c_value[1] = t
    # c_value[1]='A'  # False

    # Explaining why the above attempts are false
    # c_value[1] = A === False, Because inner elements cannot be changable

    # Demonstrating that the entire string variable can be reassigned
    '''c_value = "Behnam"
    print(c_value)'''

    # Explaining that reassigning the entire string variable is possible
    # True, Because the whole string variable can be changable


if __name__ == "__main__":
    main()
    