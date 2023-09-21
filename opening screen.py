#
# from tkinter import *
# from tkinter.ttk import *
#
# import consts
#
# root = Tk()
# root.geometry(consts.LAYOUT_SIZE)
#
#
# button_1 = Button(root, text ='hello' , bg = "blue", fg = "white")
# # button_1.place(relx = 0.8, rely = 0.5, anchor = CENTER)
# button_1.pack()
#
# # button_2 = Button(root, text ='להדפיס')
# # button_2.place(relx = 0.2, rely = 0.5, anchor = CENTER)
#
# root.mainloop()
from tkinter import *
import consts

tkWindow = Tk()
tkWindow.geometry(consts.LAYOUT_SIZE)
tkWindow.configure(bg=consts.BACKGROUND_COLOR)

b1 = Button(tkWindow, text='למצוא סיכום', bg='#eac4d5')
b1.place(x=300, y=120)

b2 = Button(tkWindow, text='לשתף סיכום', bg='#eac4d5')
b2.place(x=100, y=120)

tkWindow.mainloop()