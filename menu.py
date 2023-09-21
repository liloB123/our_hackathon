# from tkinter import *
#
# # Create object
# root = Tk('menu')
#
# # Adjust size
# root.geometry("200x200")
#
#
# # Change the label text
# def show():
#     label.config(text=clicked.get())
#
#
# # Dropdown menu options
# screens = [
#     "Home screen",
#     "Grade Level",
#     "Summaries",
#
# ]
#
# # datatype of menu text
# clicked = StringVar()
#
# # initial menu text
# clicked.set("Home")
#
# # Create Dropdown menu
# drop = OptionMenu(root, clicked, *screens)
# drop.pack()
#
# # Create button, it will change label text
# button = Button(root, text="return", command=show).pack()
#
# # Create Label
# label = Label(root, text=" ")
# label.pack()
#
# # Execute tkinter
# root.mainloop()
#
# def return_to():
#     pass


from tkinter import *
from tkinter import ttk
import sys

class GameGUI(object):

    def __init__(self, root):
        self.root = root

        self.Menu = Button(root, text="Menu", command=self.Menu)

        self.HomeButton = Button(root, text="Home", command=self.Home)

        self.GradeButton = Button(root, text="Grade Level", command=self.Grade)

        self.SummaryButton = Button(root, text="Upload Summary", command=self.summaries)

        self.ExitButton = Button(root, text="Exit",command=self.Exit)

        self.ReturnMenu = Button(root, text="Return to Main Menu", command=self.MainMenu)

        self.MainMenu()

    def Menu(self):
        self.RemoveAll()
        self.Menu.grid()
    def MainMenu(self):
        self.RemoveAll()
        self.HomeButton.grid()
        self.GradeButton.grid()
        self.SummaryButton.grid()
        self.ExitButton.grid()
        self.Menu.grid()


    def Home(self):
        self.RemoveAll()
        self.ReturnMenu.grid()
        # call screen module and run-function

    def Grade(self):
        self.RemoveAll()
        self.ReturnMenu.grid()
        # call screen module and run-function

    def summaries(self):
        self.RemoveAll()
        self.ReturnMenu.grid()
        # call screen module and run-function

    def RemoveAll(self):
        self.HomeButton.grid_remove()
        self.GradeButton.grid_remove()
        self.ExitButton.grid_remove()
        self.ReturnMenu.grid_remove()
        self.SummaryButton.grid_remove()
    def Exit(self):
        self.root.quit
        sys.exit(0)


if __name__ == '__main__':

    root = Tk()
    GameGUI = GameGUI(root)
    root.mainloop()