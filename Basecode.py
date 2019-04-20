from Tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Click Here to start typing your text\nTeditor version 1.0 \n")
mainloop()
