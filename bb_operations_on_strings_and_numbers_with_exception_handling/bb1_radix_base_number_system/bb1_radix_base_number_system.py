"""
This script demonstrates various operations with hexadecimal and binary literals,
as well as mutual displacement between two variables.
"""

def main():
    """
    Main function to demonstrate operations with hexadecimal and binary literals,
    as well as mutual displacement between two variables.
    """
    # Hexadecimal literals
    a_1 = 0xCD
    a_2 = 0b11001101  # Binary literal
    a_3 = 205
    a_4 = 0Xcd
    a_5 = 0B11001110  # Binary literal (shift + alt for Farsi/English input is very important in
                     # copy-paste operations)
    print(a_1)  # Print hexadecimal value a_1
    print(a_2)  # Print binary value a_2
    print(a_3)  # Print decimal value a_3
    print(a_4)  # Print hexadecimal value a_4
    print(a_5)  # Print binary value a_5

    # Decimal literals and conversions
    a_6 = 0x80
    a_7 = 0b10000000
    a_8 = 128
    print("a_6:0x80=", a_6)     # Print hexadecimal value of a_6
    print("a_7:0b10000000=", a_7)  # Print binary value of a_7
    print("a_8:128decimal=", a_8)  # Print decimal value of a_8

    # Mutual Displacement x->y $$ y->x:
    x_1 = 69
    y_1 = 5050
    print("x_1_old = ", x_1)  # Print updated value of x_1 before mutual displacement
    print("y_1_old = ", y_1)  # Print updated value of y_1 before mutual displacement
    x_1 = x_1 ^ y_1   # Mutual displacement operation
    y_1 = x_1 ^ y_1   # Mutual displacement operation
    x_1 = x_1 ^ y_1   # Mutual displacement operation
    print("x_1_new = ", x_1)  # Print updated value of x_1 after mutual displacement
    print("y_1_new = ", y_1)  # Print updated value of y_1 after mutual displacement

    # Swapping variables without using a temporary variable
    x_2 = 300000
    y_2 = 4000
    x_2, y_2 = y_2, x_2  # Swapping variables using tuple unpacking
    print("x_2=", x_2)  # Print updated value of x_2 after swapping
    print("y_2=", y_2)  # Print updated value of y_2 after swapping


if __name__ == "__main__":
    main()
    