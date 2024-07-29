"""
This script is authored by Behnam and is created on July, 2024.

# bb16_asctime_pp_sleep_import_time_extract_clock_time

This script demonstrates printing messages with delays and displaying \
the current time.
"""

import time  # Imports the time module to use time-related functions


def main():
    """
    Main function to print messages with delays and display the current\
         time.
    """
    print('Hi')  # Print "Hi" to the console
    time.sleep(0.5)  # Pause execution for 0.5 seconds
    print("I'm Python")  # Print "I'm Python" to the console
    time.sleep(0.5)  # Pause execution for 0.5 seconds

    current_time = time.asctime()  # Get the current time in ASCII format \
    # and store it in current_time variable

    print('Total Time1:', current_time)
    # Print the current time to the console

    # .asctime() === ascii time
    # print(t[0:2])
    # '''Mon-May--2-15:19:01-2022'''
    # Example of what the asctime format looks like

    print('Time:', current_time[11:19])  
    # Extract and print the time part of \
    # the current time, e.g., 18:56:19

    # Extracts the hour, minutes, and seconds from the current time and
    # prints it

    time.sleep(0.5)  # Pause execution for 0.5 seconds
    print('I\'m Behnam')  # Print "I'm Behnam" to the console
    time.sleep(0.5)  # Pause execution for 0.5 seconds
    print('I\'m Python')  # Print "I'm Python" to the console
    time.sleep(1)  # Pause execution for 1 second
    print('End')  # Print "End" to the console
    print('Total Time2:', current_time)  # Print the same time as before \
    # (not updated)

    # Print the current time again, which remains the same as it was \
    # when first retrieved

    # print(time.asctime()[11:13])  # Example of extracting the hour part \
    # from the current time
    time.sleep(3.5)  # Pause execution for 3.5 seconds
    print('\n\n\n')  # Print new lines for separation

while 1:  # Infinite loop to continuously execute the script
    if __name__ == "__main__":
        # Checks if the script is being run directly
        main()  
        # Call the main function when the script is executed directly
