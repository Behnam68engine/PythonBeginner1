"""
Copyright (c) 2024 Behnam

This script is authored by Behnam and is created on May 23, 2024.


bb9_float_number_before_format_letter

This script demonstrates formatting float numbers before the format letter.
"""

def main():
    """
    Main function to demonstrate formatting float numbers before the format letter.
    """
    a_value = 222  # Assigns integer value 222 to variable a_value.
    b_value = 23.97653  # Assigns float value 23.97653 to variable b_value.
    c_value = 143  # Assigns integer value 143 to variable c_value.
    d_value = 'A'  # Assigns character 'A' to variable d_value.
    e_value = 'Hello world'  # Assigns string 'Hello world' to variable e_value.
    f_value = 0x8f  # Assigns hexadecimal value 0x8f (143 in decimal) to variable f_value.

    print(f'a_value:+09d={a_value:+09d}')  
    # Formats integer a_value with sign, minimum width, and zero-padding.
    # print('a_value%%+09.5d=%+09.5d' % a_value) 
    # less readable and less concise way  
    # Formats integer a_value with sign, minimum width, and precision.

    print(f'a_value:05d={a_value:05d}')  
    # Formats integer a_value with zero-padding up to 5 digits.
    # print('a_value%%.5d=%.5d' % a_value)
    # less readable and less concise way  
    # Formats integer a_value with precision.

    print(f'a_value:5d={a_value:5d}')  
    # Formats integer a_value with minimum width.
    # print('a_value%%5d=%5d' % a_value)
    # less readable and less concise way  
    # Formats integer a_value with minimum width.

    print(f'\n\n\nb_value = {b_value}, c_value = {c_value}, '
          f'd_value = {d_value}, e_value = "{e_value}"'
          f', f_value = {f_value}')
    # Prints all remaining variables to avoid linting errors.

    # print(b_1)

if __name__ == "__main__":
    main()

# copyright
# The copyright command in the code serves as a marker indicating
# the ownership or copyright of the script.
