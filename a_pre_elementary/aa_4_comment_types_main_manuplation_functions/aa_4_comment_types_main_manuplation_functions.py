"""
This script demonstrates the usage of functions and comments in Python.
"""

import time
import os

# Function definition: f_x1
def f_x1():
    """
    Print a large number.
    """
    print(3333555553)

# Function definition: main
def main():
    """
    Perform arithmetic operations and print the result.

    Parameters:
        None

    Returns:
        None
    """
    a_1 = 10
    b_1 = 20
    c_1 = a_1 * b_1
    print(c_1)
    # """print(c_1)"""

# Function definition: f_x2
def f_x2():
    """
    Print a large number.

    Parameters:
        None

    Returns:
        None
    """
    print(3333555553)

# Get the current working directory using os.getcwd()
print("cwd\n\n")
cwd = os.getcwd()
print(f"\nCurrent working directory:\n {cwd}\n\n")

# Call function f_x1
f_x1()

# Introduce a delay of 3 seconds using time.sleep()
time.sleep(3)

# Call function f_x2
f_x2()

# Statement to indicate 'f_x2()' is run before 'main()'
'f_x2() is run before main()!!!!'

# Conditional execution using '__name__'
# String statement has no effectpylint(pointless-string-statement)
# String statement has no effectpylint(pointless-string-statement)
if __name__ == "__main__":
    print(3)
    main()

# ---------------------- single line comment by Number sign or # yeah ### and..
# you see later # are uneffective!
# Maximum comment correcter per line should be #79

'''------------------------------------
    ----------------------------------
    ----------------------------
    ----------
    ---------------------------------
    ---- Multiple line comment or long comment by at least 3 ' or " i.e.  """
    or '''
'''single " or ' "'are considered as single line comment just like # but with
 different colors! They are also used another ' or " at the end of each line
'and double "" or '' are uneffective on code!'''
'sigle line comment'
"single line comment again"
# single line comment again again!
