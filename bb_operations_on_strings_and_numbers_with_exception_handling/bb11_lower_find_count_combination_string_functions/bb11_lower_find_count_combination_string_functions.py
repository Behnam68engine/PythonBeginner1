""" Copyright (c) 2024 Behnam
This script is authored by Behnam and is created on May 24, 2024.
bb11_lower_find_count_combination_string_functions
This script demonstrates the usage of string functions lower(),
find(), and count().
"""

def main():
    """
    Main function to demonstrate the usage of string functions lower(),
    find(), and count().
    """
    a_value = 222  # Assigns integer value 222 to variable a_value.
    b_value = 23.97643  
    # Assigns float value 23.97643 to variable b_value.
    c_value = 128  # Assigns integer value 128 to variable c_value.
    d_value = 'A'  # Assigns character 'A' to variable d_value.
    e_value = 'oh woRlD, Hello World AND Hello PYTHON world ,o twoworlddd'  
    # Assigns string to variable e_value.

    print("\n\n")  # Prints newline characters for formatting.
    print('e = ', e_value)  # Prints the value of e_value.
    print("\n\n")  # Prints newline characters for formatting.

    s1_value = e_value.lower()  
    # Converts e_value to lowercase and assigns it to s1_value.
    # print(10* 'Behnam')
    print('lower e = ', s1_value)  # Prints the lowercase version of
    # e_value.
    print("\n\n")  # Prints newline characters for formatting.

    s2_value = s1_value.find('world')  
    # Finds the index of the first occurrence of 'world' in s1_value and
    # assigns it to s2_value.
    print('place of first character of first "world" = ', s2_value)  
    # Prints the index of the first 'world' occurrence.
    print("\n\n")  # Prints newline characters for formatting.

    s3_value = s1_value.count('world')  
    # Counts the occurrences of 'world' in s1_value and assigns it to
    # s3_value.
    print('Number of "world" = ', s3_value)  # Prints the count of
    # 'world' occurrences.
    print("\n\n")  # Prints newline characters for formatting.

    print('combination (lower & count) ->, Number of "world" =  ', 
          e_value.lower().count('world'))  
    # Prints the count of 'world' occurrences in e_value after converting
    # it to lowercase.
    print("\n\n")  # Prints newline characters for formatting.

    print('combination (lower & find) ->,place of first character of'
          'first "world" = ', e_value.lower().find('world'))  
    # Prints the index of the first 'world' occurrence in e_value after
    # converting it to lowercase.
    print("\n\n")  # Prints newline characters for formatting.

    print('combinationNonexistedWord(lower & count) ->, Number of'
          ' "NonexistedWord" = ', e_value.lower().count('NonexistedWord'))  
    # Prints the count of 'NonexistedWord' occurrences in e_value
    # after converting it to lowercase.
    print("\n\n")  # Prints newline characters for formatting.

    print('combinationNonexistedWord(lower & find) ->, place of first'
          ' character of "NonexistedWord" = '
          , e_value.lower().find('NonexistedWord'))  
    # Prints the index of the first 'NonexistedWord' occurrence in
    # e_value after converting it to lowercase.
    print("\n\n")  # Prints newline characters for formatting.

    # Using unused variables in a print statement to avoid pylint warnings

    print(f"a_value: {a_value}, b_value: {b_value}, c_value: {c_value},"
          f" d_value: {d_value}, e_value: {e_value}")  
    # Prints the values of variables a_value, b_value,
    # c_value, d_value, and e_value.
    print("\n\n")  # Prints newline characters for formatting.

if __name__ == "__main__":
    main()

# copyright
# The copyright command in the code serves as a marker indicating
# the ownership or copyright of the script.
