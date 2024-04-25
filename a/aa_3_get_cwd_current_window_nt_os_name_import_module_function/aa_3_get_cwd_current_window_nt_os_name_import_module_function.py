"""
This script demonstrates the usage of functions and prints 
some messages using the tkinter library and os module.
"""

# Import necessary modules
# from tkinter import *
from tkinter import Button, Label, Tk  # Import Button, Label, and Tk classes from tkinter
import time  # Import time module
import os  # Import os module

# Define function f_x
def f_x(a):
    """
    Print messages based on the value of the input parameter 'a'.

    Parameters:
        a (int): The input integer parameter.

    Returns:
        None
    """
    print(3)  # Print 3
    if a > 3:  # Check if a is greater than 3
        print("Behnam0")  # Print "Behnam0" if condition is true
    else:  # If condition is false
        print(240)  # Print 240

# Define function fx3
def fx3():
    """
    Print messages based on the value of the local variable 'b'.

    Parameters:
        None

    Returns:
        None
    """
    b = 4  # Assign 4 to variable b
    print(3)  # Print 3
    if b > 4:  # Check if b is greater than 4
        print("Behnam333")  # Print "Behnam333" if condition is true
    elif b == 4:  # If b is equal to 4
        print(244444444)  # Print 244444444
    else:  # If none of the above conditions are true
        print("Hey")  # Print "Hey"

# Create the main window using Tkinter
root = Tk()  # Create the main window

# Create a label widget
label = Label(root, text="Welcome to tkinter!")  # Create a label widget with the text "Welcome to tkinter!"
label.pack()  # Pack the label widget into the main window

# Create a button widget
button = Button(root, text="Click me!")  # Create a button widget with the text "Click me!"
button.pack()  # Pack the button widget into the main window

# Run the Tkinter event loop
root.mainloop()  # Start the Tkinter event loop

# Call function f_x with argument 3
f_x(3)  # Call function f_x with argument 3
print("\n")  # Print a newline character

# Call function f_x with argument 4
f_x(4)  # Call function f_x with argument 4
print("\n")  # Print a newline character

# Call function fx3
fx3()  # Call function fx3
print("\n\n\n\n\n")  # Print multiple newline characters

# Introduce a delay of 2 seconds using time.sleep()
time.sleep(2)  # Introduce a delay of 2 seconds

# Call function fx3
fx3()  # Call function fx3
print("\n\n\n\n\n")  # Print multiple newline characters

# Call function fx3
fx3()  # Call function fx3
print("\n")  # Print a newline character

# Print "hello1"
print("hello1")  # Print "hello1"

# Print operating system name
print(os.name)  # Print the name of the operating system
print("\n\n")  # Print multiple newline characters

# Print current working directory
print(os.getcwd())  # Print the current working directory
print("\n\n")  # Print multiple newline characters

# Print "hello2" followed by a newline character
print("hello2\n")  # Print "hello2" followed by a newline character

# Take user input
x = input()  # Prompt the user for input

# End of the script
