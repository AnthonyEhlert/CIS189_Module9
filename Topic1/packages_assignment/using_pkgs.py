"""
Program: using_pkgs.py
Author: Tony Ehlert
Last date modified: 3/9/2023

The purpose of this program is to import modules that are contained in a package and
then call the functions contained in the modules.

The input is the modules contained in the definitions package and a dictionary and a set that will be passed into
two of the functions called.

The output is messages and contents of the dictionary and set that print to the console
"""
from definitions import dictionary_ops as dict_ops, greeting, set_ops

if __name__ == "__main__":
    # create dictionary
    my_dict = {"Color 1": "Yellow", "Color 2": "Purple", "Color 3": "Blue"}

    # create set
    my_set = ("CIS189", "CIS171", "CIS175")

    # call of functions
    greeting.greeting()
    greeting.message()
    dict_ops.print_dict(my_dict)
    set_ops.print_set(my_set)