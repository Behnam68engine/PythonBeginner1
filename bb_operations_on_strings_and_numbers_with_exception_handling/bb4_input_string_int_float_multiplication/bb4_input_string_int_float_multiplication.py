"""
This script demonstrates variable assignments and basic operations with
different data types.
"""

def main():
    """
    Main function to demonstrate variable assignments and basic operations
    with different data types.
    """
    # Prompting the user to input a string for variable x_1
    x_1 = input("Enter a string for x_1: ")
    # Printing the result of multiplying the input string x_1 by 3
    print("String x_1 * 3 = ", 3 * x_1)
    # Prompting the user to input an integer for variable x_2, then converting it to an integer
    x_2 = int(input("Enter an integer for x_2: "))
    # Printing the result of multiplying the input integer x_2 by 4
    print("Integer x_2 * 4 = ", 4 * x_2)
    # Prompting the user to input a float for variable x_3, then converting it to a float
    x_3 = float(input("Enter a float for x_3: "))
    # Printing the result of multiplying the input float x_3 by 5
    print("Float x_3 * 5 = ", 5 * x_3)
    # '''x_4 = bool(input("Enter a boolean value for x_4: "))
    # # print("Boolean x_4 * 6 = ", 6 * x_4)''' # ''' isn't very common, ''' just for docstring!!!
    # Prompting the user to input a boolean value for variable x_4
    x_4_input = input("Enter a boolean value for x_4 (True or False): ").capitalize()
    # Converting the input string to a boolean value
    if x_4_input == "True":
        x_4 = True
    elif x_4_input == "False":
        x_4 = False
    else:
        print("Invalid input. Please enter either 'True' or 'False'.")
        return  # Exit the function if the input is invalid

    print("Boolean x_4 * 6 = ", 6 * x_4)


    # Prompting the user to input another string for variable x_5
    x_5 = input("Enter another string for x_5: ")
    # Printing the result of multiplying the input string x_5 by 7
    print("String x_5 * 7 = ", 7 * x_5)


if __name__ == "__main__":
    main()
