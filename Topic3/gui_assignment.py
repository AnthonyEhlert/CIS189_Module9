import tkinter
"""
Program: gui.assignment.py
Author: Tony Ehlert
Last date modified: 3/9/2023

The purpose of this program is to create a basic GUI that contains checkboxes of different meals
and updates a label depending on what checkbox is selected. It also contains a button to exit/close the GUI

The input is data needed to create the GUI along with functions to control what each checkbox is supposed to do

The output is a GUI that displays the choices for the user and what they
selected (or a waiting label if nothing is selected) along with an exit button
"""
'''
FUNCTIONS BELOW HERE
'''


def check_breakfast():
    """
    This method changes the GUI label if the Breakfast checkbox is checked

    :return: none
    """
    if (var_bfast.get() == 1):
        # update selection_label text
        selection_label.config(text="Breakfast is your favorite?")
    else:
        # button is unchecked, update selection_label text to "Waiting"
        selection_label.config(text="Waiting")


def check_second_breakfast():
    """
    This method changes the GUI label if the 2nd Breakfast checkbox is checked

    :return: none
    """
    if (var_second_bfast.get() == 1):
        # update selection_label text
        selection_label.config(text="Second Breakfast is your favorite?")
    else:
        # button is unchecked, update selection_label text to "Waiting"
        selection_label.config(text="Waiting")


def check_lunch():
    """
    This method changes the GUI label if the Lunch checkbox is checked

    :return: none
    """
    if (var_lunch.get() == 1):
        # update selection_label text
        selection_label.config(text="Lunch is your favorite?")
    else:
        # button is unchecked, update selection_label text to "Waiting"
        selection_label.config(text="Waiting")


def check_dinner():
    """
    This method changes the GUI label if the Dinner checkbox is checked

    :return: none
    """
    if (var_dinner.get() == 1):
        # update selection_label text
        selection_label.config(text="Dinner is your favorite?")
    else:
        # button is unchecked, update selection_label text to "Waiting"
        selection_label.config(text="Waiting")


'''
FUNCTIONS ABOVE HERE
'''

# create main window
main_window = tkinter.Tk()

'''
MODULE CODE BELOW HERE
'''

# set title of main_window
main_window.title("Favorite Meal")

# create breakfast button variable and checkbox
var_bfast = tkinter.IntVar()
bfast_check = tkinter.Checkbutton(main_window, text="Breakfast", variable=var_bfast, onvalue=1, offvalue=0,
                                  command=check_breakfast).grid(row=1)

# create 2nd Breakfast button variable and checkbox
var_second_bfast = tkinter.IntVar()
second_bfast_check = tkinter.Checkbutton(main_window, text="Second Breakfast", variable=var_second_bfast, onvalue=1,
                                         offvalue=0, command=check_second_breakfast).grid(row=2)

# create Lunch button variable and checkbox
var_lunch = tkinter.IntVar()
lunch_check = tkinter.Checkbutton(main_window, text="Lunch", variable=var_lunch, onvalue=1, offvalue=0,
                                  command=check_lunch).grid(row=3)

# create Dinner button variable and checkbox
var_dinner = tkinter.IntVar()
dinner_check = tkinter.Checkbutton(main_window, text="Dinner", variable=var_dinner, onvalue=1, offvalue=0,
                                   command=check_dinner).grid(row=4)

# create waiting/selection label for row 5
selection_label = tkinter.Label(main_window, text="Waiting")
selection_label.grid(row=5)

# create exit button
exit_button = tkinter.Button(main_window, text="Exit", width=25, command=main_window.destroy)
exit_button.grid(row=6)

'''
MODULE CODE ABOVE HERE
'''

# run main_window.mainloop()
main_window.mainloop()
