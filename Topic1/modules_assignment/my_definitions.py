"""
Program: my_definitions.py
Author: Tony Ehlert
Last date modified: 3/8/2023

The purpose of this program is to hold functions that will be imported and called by use_definition_module.py

The input is 4 functions (greeting that prints a friendly greeting, a function that prints the author of the code,
a print_dict that accepts a dictionary and prints the pairs one per line, and a print_set function that prints
the set one item per line).

The output is none as this file only contains functions that are to be called by another file/module
"""


def greeting():
    """
    This function simply prints a friendly greeting in the console

    :return: none
    """
    print("Hello, Welcome to CIS189.  Good Luck!")


def message():
    """
    This function simply prints the author of the code in the console

    :return: none
    """
    author = 'Tony Ehlert'
    print(f"Author: {author}")


def print_dict(dict_to_print):
    """
    This function accepts a dictionary as an argument and prints the pairs of the dictionary to the console one per line
    :param dict_to_print: dictionary of pairs to print
    :return: none
    """
    for keys, value in dict_to_print.items():
        print(f"({keys}, {value})")


def print_set(set_to_print):
    """
    This function accepts a set as an argument and prints the contents one by one and one per line
    :param set_to_print: set of items to be printed
    :return: none
    """
    for items in set_to_print:
        print(f"{items}")
