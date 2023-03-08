"""
Program: dictionary_ops.py
Author: Tony Ehlert
Last date modified: 3/9/2023

The purpose of this program is house a function that accepts a dictionary as an argument and then prints the
contents of the dictionary to the console.

The input is a function that accepts a dictionary

The output is a print to the console of each pair in the dictionary
"""

def print_dict(dict_to_print):
    """
    This function accepts a dictionary as an argument and prints the pairs of the dictionary to the console one per line
    :param dict_to_print: dictionary of pairs to print
    :return: none
    """
    for keys, value in dict_to_print.items():
        print(f"({keys}, {value})")