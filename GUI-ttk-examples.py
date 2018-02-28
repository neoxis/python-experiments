from tkinter import *
from tkinter.ttk import *               #combobox library
from tkinter import scrolledtext        #scolled text library
from tkinter import messagebox          #message box library

#button functions#
def clicked():
        txt.delete(1.0, END)

def mes():
        messagebox.showinfo('Message Title','Message Body')


##########
###MAIN###
window =Tk()
window.title("GUI-ttk Examples")
window.geometry()
window.mainloop

##Button##
##########
''' Clear '''
b = Button(window, text="Clear", command=clicked)
b.grid(column=1, row=0)
''' Message Box '''
b1 = Button(window, text="Message", command=mes)
b1.grid(column=1, row=1)

##Combobox##
############
c = Combobox(window)
c['values']=(1,2,3,4,5)
c.current(2)
c.grid(column=0, row=0)

##Checkbutton##
###############





##Radiobutton##
###############



##Scrolledtext##
################
'''Example 1 - Scrolled Text ''' #width/height = number of chars
txt = scrolledtext.ScrolledText(window, width=50, height=10)
txt.insert(INSERT, 'Your text goes here...')

txt.grid(column=0, row=1)
