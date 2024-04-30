"""
This script demonstrates variable assignments and string indexing.
"""

def main():
    """
    Main function to demonstrate variable assignments and string indexing.
    """
    a_value = 0  # Assigns integer value 0 to variable a_value.
    b_value = 0.1  # Assigns float value 0.1 to variable b_value.
    c_value = "Hello"  # Assigns string "Hello" to variable c_value.
    print(a_value, b_value, c_value)  # Prints the values of a_value, b_value, and c_value.

    
    print(c_value[0])  # Prints the first character of the string stored in c_value.
    print(c_value[1])  # Prints the second character of the string stored in c_value.
    print(c_value[2])  # Prints the third character of the string stored in c_value.

    ''' c_value2 = 'behnam'
    print(c_value2)'''
    
    c_value = 'behnam'  # Reassigns variable c_value with string 'behnam'.
    print(c_value)  # Prints the updated value of c_value.

    #c2[0]='A'  # False

    s_value = c_value.upper()  # Converts the string stored in c_value to uppercase and assigns it to s_value.
    print(s_value)  # Prints the uppercase version of the string stored in c_value.


if __name__ == "__main__":
    main()
