"""
Copyright (c) 2024 Behnam

This script is authored by Behnam and is created on May 13, 2024.


bb8_string_index_print

This script demonstrates printing substrings using string indexing.
"""

def main():
    """
    Main function to demonstrate printing substrings using string indexing.
    """
    a_value = 222  # Assigns integer value 222 to variable a_value.
    b_value = 23.97643  # Assigns float value 23.97643 to variable b_value.
    c_value = 128  # Assigns integer value 128 to variable c_value.
    d_value = 'A'  # Assigns character 'A' to variable d_value.
    
    # Print variables in the specified format
    # print(f"a_value = {a_value},\nb_value = {b_value},\n\
    # c_value = {c_value},\nd_value = {d_value}\n\n\n") 
    # Console print problems

    # Print variables in the specified format
    print(f"a_value = {a_value},\nb_value = {b_value},\n"
      f"c_value = {c_value},\nd_value = {d_value}\n\n\n")
    # Prints the variables a_value, b_value,
    # c_value, and d_value in the specified format.

    
    e_value = 'Hello World AND Hello PYTHON'  
    # Assigns string 'Hello World AND Hello PYTHON' to variable e_value.

    #print(10* 'BehnamEbi')
    print(10 * 'PYTHON 1 ')  # Prints 'PYTHON 1' repeated 10 times.
    #character index from 0 to n-1
    print("\n\na\n\n")  # Prints character 'a'.
    
    print("Array index start with '0'")  
    # Prints explanation about array index starting from 0.
    
    print("print  e_value with index >=4 & < 7 i.e 4,\
    5 & 6 of <<Hello World AND Hello PYTHON>>:1")
    # Semi-error print in two line in terminal with tap in the 2nd line!!!

    print("print  e_value with index >=4 & < 7 i.e 4, "\
    "5 & 6 of <<Hello World AND Hello PYTHON>>:2")
    # True print in two line in terminal!!!

    # print(("print  e_value with index >=4 & < 7 i.e 4,
    # 5 & 6 of <<Hello World AND Hello PYTHON>>:"))
    # False syntax

    

    
    print("print  e_value with index >=4 & < 7 i.e 4, "
        "5 & 6 of <<Hello World AND Hello PYTHON>>:3")
    # Prints a message indicating the range of characters with indices
    #  from 4 to less than 7 (i.e., 4, 5, and 6) 
    # within the string 'Hello World AND Hello PYTHON', followed by ":3".

    print("print  e_value with index >=4 & < 7 i.e 4, " + 
        "5 & 6 of <<Hello World AND Hello PYTHON>>:4")
    # Prints a similar message, but using string concatenation
    # instead of a single string, 
    # followed by ":4".

    print(e_value[4:7]+"\n")
    # Prints the substring of e_value starting from index 4
    # and including index 4 up to index 6 and excluding index 7.
    # Array index start with '0'
    # o W

    print("print e_value with index >=4 i.e 4 to end index of" +
        "<<Hello World AND Hello PYTHON>>:")
    print(e_value[4:] ,"\n")
    # print(e_value[4:] "\n") # False syntax!   
    # Prints the substring of e_value starting from index 4 till the end.
    # o World AND Hello PYTHON
     
    
    print("print e_value with index <4 & i.e 0 to 3 of"
    "<<Hello World AND Hello PYTHON>>:")
    print(e_value[:4])
    print()  
    # Prints the substring of e_value starting from index 0 up to index 3.
    # Hell

if __name__ == "__main__":
    main()

# copyright
# The copyright command in the code serves as a marker indicating
# the ownership or copyright of the script.
