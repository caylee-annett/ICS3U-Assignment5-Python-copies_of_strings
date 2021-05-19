#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints copies of a string


def main():
    # This function prints the new string
    loop_counter = 0

    # Input
    print("This program prints copies of a string as many times as you want.")
    print("")
    entered_string = input("Enter a string: ")
    number_as_string = input("Enter a positive integer for the number of "
                             "times to repeat the string: ")

    # Process & Output
    while True:
        try:
            number_as_integer = int(number_as_string)

            if number_as_integer > 0:
                break
            else:
                number_as_string = input("{} is not a valid input. Enter a "
                                         "positive integer: ".
                                         format(number_as_string))
        except Exception:
            number_as_string = input("{} is not a valid input. Enter a "
                                     "positive integer: ".
                                     format(number_as_string))
    for loop_counter in range(number_as_integer + 1):
        new_string = loop_counter * entered_string
    print("")
    print("The new string is: {}".format(new_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
