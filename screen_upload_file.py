
from tkinter import *
import consts

def open_screen_upload_file():
    # make window and bg color
    tkWindow = Tk()
    tkWindow.geometry(consts.LAYOUT_SIZE)
    tkWindow.configure(bg=consts.BACKGROUND_COLOR)


    # make add file button
    def clicked_add_file():
        text.config(text="You should be able to upload a file now... lol.")


    click_btn = PhotoImage(file='addFile.png')
    label_add_file = Label(image=click_btn)

    button = Button(tkWindow, image=click_btn, command=clicked_add_file, borderwidth=-1)
    button.pack(pady=0)
    button.place(x=80, y=150)

    text = Label(tkWindow, text="")
    text.pack(pady=0)

    # making the image for the background button of format

    bg_format = PhotoImage(file="page_fill_bg_format.png")
    img_label_bg_format = Label(image=bg_format, ).place(x=700, y=150)


    # buttons class

    button_class = PhotoImage(file='class.png')
    label_button_class = Label(image=button_class)

    button_class_stats = Button(tkWindow, image=button_class, borderwidth=-1)
    button_class_stats.place(x=1200, y=160)

    image_write_class = PhotoImage(file="where_write_classs.png")
    img_write_class = Label(image=image_write_class, ).place(x=800, y=160)

    #button_specific_subject

    button_insubject = PhotoImage(file='specific_subject.png')
    label_button_in_subject = Label(image=button_insubject)

    button_subject_in_stats = Button(tkWindow, image=button_insubject, borderwidth=-1)
    button_subject_in_stats.place(x=1200, y=260)

    image_write_insubject = PhotoImage(file="where_write_insubject.png")
    img_write_insubject = Label(image=image_write_insubject, ).place(x=800, y=260)


    #under format
    under_image = PhotoImage(file="under_format.png")
    under_image_label = Label(image=under_image, ).place(x=700, y=360)




