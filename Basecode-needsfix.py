from tkinter import *
import os
from tkinter import messagebox, filedialog, Tk, simpledialog
import webbrowser 
from tkinter import scrolledtext
from tkinter import Menu
import datetime
 
window = Tk() 

def redo(event=None):
        textArea.event_generate("<<Redo>>")
        return

def undo(event=None):
        textArea.event_generate("<<Undo>>")
        return

def paste(event=None):
         textArea.event_ganerate("<<Paste>>")
         return

def cut(event=None):
        textArea.event_generate("<<Cut>>")
        return

def copy(event=None):
        textArea.event_generate("<<Copye>>")
        return

def tme():
    now = datetime.datetime.now()
    textArea.insert('end',now)

def select_all(event=None):
    textArea.tag_add('sel', '1.0', 'end')
    return "break"

def new_fle():
    file=filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes=(("HTML Files","*.html"),("Text Files","*.txt"),("All Files","*.*")))
    window.title(os.path.basename(file.name)+ " -Notepad")
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save","Do wish to save ?"):
            svfil()
        else:
            textArea.delete('1.0',AND)
        

def fnd_txt():
    findString= simpledialog.askstring("Find...","Enter Text")
    textData=textArea.get('1.0',END)
    occurances = textData.upper().count(findString.upper())
    if textData.upper().count(findString.upper()) ==1:
        label = massagebox.showinfo("Result:  "  ,findString +"  has once occurances,"+ str(occurances))
    elif textData.upper().count(findString.upper()) ==2:
        label = messagebox.showinfo("Result:  "  ,findString +"  has twice occurance,"+ str(occurances)) 
    elif textData.upper().count(findString.upper()) ==3:
        label = messagebox.showinfo("Result:  "  ,findString +"  has thrice occurances,"+ str(occurances))
    elif textData.upper().count(findString.upper()) >4 or textData.upper().count(findString.upper()) ==4:
        label = messagebox.showinfo("Result:  "  ,findString +"  has multiple occurances,"+ str(occurances))    
    else:
        label= messagebox.showinfo("Results","Not Found")

def opnficl():
    file=filedialog.askopenfile(parent=window, title="select a text file",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    window.title(os.path.basename(file.name)+ " -Notepad")
    if file != None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()
        
def svfil():
    file=filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes=(("HTML Files","*.html"),("Text Files","*.txt"),("All Files","*.*")))
    window.title(os.path.basename(file.name)+ " -Notepad")
    if file != None:
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
def exit():
    if messagebox.askyesno("Exit","Are you sure you want to exit"):
        window.destroy()
def helpview():
    webbrowser.open_new("html.doc")
    
def aboutnot():
 
    messagebox.showinfo('About Notepad', 'BTE \n Basic Text Editor \n Version V1.0.01 Compiled on Python \n \n Credits:\n Mustaqeem \n Ashmal \n Aijaz \n Arham')

window.title("NewDocument-BTE")
window.geometry('800x640') 
menu = Menu(window)

 
filnew_item = Menu(menu)
fntnew_item = Menu(menu)
helnew_item = Menu(menu)
vwnew_item = Menu(menu)
ednew_item = Menu(menu)

vwnew_item.add_command(label='Status Bar')

ednew_item.add_command(label='Undo',command=undo)
ednew_item.add_separator()
ednew_item.add_command(label='Cut',command=cut)
ednew_item.add_command(label='Copy',command=copye)
ednew_item.add_command(label='Paste',command=paste)
ednew_item.add_command(label='Redo',command=redo)
ednew_item.add_separator()
ednew_item.add_command(label='Fint Text',command=fnd_txt)
ednew_item.add_separator()
ednew_item.add_command(label='Select All',command=select_all)
ednew_item.add_command(label='Time/Date',command=tme)



filnew_item.add_command(label='New',command=new_fle)
filnew_item.add_command(label='Open...',command=opnfil)
filnew_item.add_command(label='Save',command=svfil)
filnew_item.add_command(label='Exit',command=exit)
 
helnew_item.add_command(label='View Help',command=helpview)
helnew_item.add_separator()
helnew_item.add_command(label='About Notepad',command=aboutnote)
menu.add_cascade(label='File', menu=filnew_item)

menu.add_cascade(label='Edit', menu=ednew_item)

menu.add_cascade(label='View', menu=vwnew_item)

menu.add_cascade(label='Help', menu=helnew_item)


#S = Scrollbar(window)
textArea = scrolledtext.ScrolledText(window, height=400, width=500)
#S.pack(side=RIGHT, fill=Y)
textArea.pack(side=LEFT, fill=Y)
#S.config(command=textArea.yview)
textArea.config()
quote = """"""
textArea.insert(END, quote)
window.config(menu=menu) 

window.mainloop()
