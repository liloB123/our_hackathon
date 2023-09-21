import tkinter as tk

#creating screen
root = tk.Tk()
root.mainloop()

#Adjust size
root.geometry("500x300")

# Add image file
#bg = PhotoImage(file = "")

gui = tk.Tk(className='Python Examples - Window Color')
gui.configure(bg='blue')

# Show image using label
#label1 = Label( root, image = )
#label1.place(x = 0, y = 0)

label2 = tk.Label(root, text = "Welcome")
label2.pack(pady = 50)

# Create Frame
frame1 = tk.Frame(root)
frame1.pack(pady = 20 )
