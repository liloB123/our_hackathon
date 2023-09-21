
from tkinter import *
import consts

#make window and bg color
tkWindow = Tk()
tkWindow.geometry(consts.LAYOUT_SIZE)
tkWindow.configure(bg = consts.BACKGROUND_COLOR)

#make add file button
def clicked_add_file():
    text.config(text="You should be able to upload a file now... lol.")

click_btn= PhotoImage(file='addFile.png')


label_add_file= Label(image=click_btn)

button = Button(tkWindow, image=click_btn, command= clicked_add_file,borderwidth=-1)
button.pack(pady=0)
button.place(x=80, y=150)

text = Label(tkWindow, text= "")
text.pack(pady=0)

#making the image for the background button of format

bg_format = PhotoImage(file = "page_fill_bg_format.png")
img_label_bg_format = Label(image = bg_format,).place(x = 700 , y = 150)

#buttons for

tkWindow.mainloop()

