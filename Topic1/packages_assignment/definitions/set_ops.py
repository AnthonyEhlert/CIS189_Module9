"""
Program: set_ops.py
Author: Tony Ehlert
Last date modified: 3/9/2023

The purpose of this program is to house a function that accepts a set as an argument and then prints
the contents of the set to the console.

The input is function and set of items

The output is a print to the console of the items contained in the set
"""
def print_set(set_to_print):
    """
    This function accepts a set as an argument and prints the contents one by one and one per line
    :param set_to_print: set of items to be printed
    :return: none
    """
    for items in set_to_print:
        print(f"{items}")