import tkinter as tk
from tkinter import *
import consts
from PIL import ImageTk, Image
from tkinter import Button,Label



def opening_screen():
    opening_screen = Tk()
    opening_screen.geometry(consts.LAYOUT_SIZE)
    opening_screen.configure(bg=consts.BACKGROUND_COLOR)
    img_1 = Image.open(consts.LOGO)
    logo = ImageTk.PhotoImage(img_1)
    label = Label(opening_screen , image=logo)
    label.image = logo
    label.place(x=600, y=100)

    img_2 = Image.open("find.jpg")
    find = ImageTk.PhotoImage(img_2)
    find_button = Button(opening_screen, image=find, bd=0, highlightthickness=0)
    find_button.image = find
    find_button.place(x=900, y=350)

    img_3 = Image.open("upload.jpg")
    upload = ImageTk.PhotoImage(img_3)
    upload_button = Button(opening_screen, image=upload, bd=0, highlightthickness=0)
    upload_button.image = upload
    upload_button.place(x=300, y=350)

    opening_screen.mainloop()



opening_screen()

def choose_grade_screen():
    choose_grade_screen = Tk()
    choose_grade_screen.geometry(consts.LAYOUT_SIZE)
    choose_grade_screen.configure(bg=consts.BACKGROUND_COLOR)

    img_1 = Image.open("grade.jpg")
    grade = ImageTk.PhotoImage(img_1)
    grade_label = Label(choose_grade_screen, image=grade, borderwidth=0)
    grade_label.image = grade
    grade_label.place(x=370, y=100)

    img_2 = Image.open("elementary.jpg")
    elementary = ImageTk.PhotoImage(img_2)
    elementary_button = Button(choose_grade_screen, image=elementary, bd=0, highlightthickness=0)
    elementary_button.image = elementary
    elementary_button.place(x=1000, y=350)

    img_3 = Image.open("middle.jpg")
    middle = ImageTk.PhotoImage(img_3)
    middle_button = Button(choose_grade_screen, image=middle, bd=0, highlightthickness=0)
    middle_button.image = middle
    middle_button.place(x=600, y=350)

    img_4 = Image.open("high.jpg")
    high = ImageTk.PhotoImage(img_4)
    high_button = Button(choose_grade_screen, image=high, bd=0, highlightthickness=0)
    high_button.image = high
    high_button.place(x=200, y=350)

    choose_grade_screen.mainloop()


choose_grade_screen()
