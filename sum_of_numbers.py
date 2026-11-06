#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/06/26
# This program displays a total number based on the amount of times looped

import constants


def main():
    # Setting the needed variables
    total_num = 0
    current_loop = 0

    total_loops_str = input("Enter the amount of times to loop: ")

    # the try statement will make sure the code safely with invald user inputs
    try:
        # Converting the input from the user to an integer
        total_loops = int(total_loops_str)

        # Checking if the input is valid
        if total_loops <= 0:
            print(constants.ERR_MSG.format(total_loops_str))

        else:
            # Loop the requested amount of times
            while current_loop < total_loops:
                # Add to the counter and the sum
                current_loop += 1
                total_num += current_loop
                # Display the amount of times looped
                print(constants.TRACK_MSG.format(current_loop))

            # Display the sum
            print(constants.FINAL_MSG.format(total_num))

    except:
        print(constants.ERR_MSG.format(total_loops_str))


if __name__ == "__main__":
    main()
