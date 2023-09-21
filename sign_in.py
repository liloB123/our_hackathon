from tkinter import *
import consts

def open_log_in():

    tkWindow = Tk()
    tkWindow.geometry(consts.LAYOUT_SIZE)
    log_in = PhotoImage(file="log_in_im.png")
    log_in_image = Label(image=log_in, ).place(x=0, y=0)

    tkWindow.mainloop()

