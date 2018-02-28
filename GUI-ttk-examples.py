from tkinter import *
from tkinter.ttk import *               #combobox library
from tkinter import scrolledtext        #scolled text library
from tkinter import messagebox          #message box library

#button functions#
def clicked():
        txt.delete(1.0, END)

def mes():
        '''Example 1 - show info '''
        #messagebox.showinfo('Message Title','Message Body')
        '''Example 2 - show warning '''
        #messagebox.showwarning('Message Title','Message Body')
        '''Example 3 - show error '''
        #messagebox.showerror('Message Title','Message Body')
        '''Example 4 - ask question '''
        #messagebox.askquestion('Message Title','Message Body')
        '''Example 5 - ask yes or no '''
        #messagebox.askyesno('Message Title','Message Body')
        '''Example 6 - ask yes, no, or cancel '''
        #messagebox.askyesnocancel('Message Title','Message Body')
        '''Example 7 - ask ok or cancel '''
        #messagebox.askokcancel('Message Title','Message Body')
        '''Example 8 - ask retry or cancel '''
        messagebox.askretrycancel('Message Title','Message Body')

#checkbox functions#
def tog():
        if chk_state.get()==0:
                chk_label='Yes'
                #chk_state.set(1)
        else:
                chk_label='No'
                #chk_state.set(0)

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
b1.grid(column=2, row=0)

##Combobox##
############
c = Combobox(window)
c['values']=(1,2,3,4,5)
c.current(2)

c.grid(column=0, row=0)

##Checkbutton##
###############
chk_state = IntVar()
chk_label = 'No'

chk = Checkbutton(window, text=chk_label, var=chk_state, onvalue=1, offvalue=0, command=tog)

chk.grid(column=5, row=0)


##Radiobutton##
###############



##Spinbox##
###########




##Scrolledtext##
################
'''Example 1 - Scrolled Text ''' #width/height = number of chars
txt = scrolledtext.ScrolledText(window, width=50, height=10)
txt.insert(INSERT, 'Your text goes here...')

txt.grid(column=0, row=1, columnspan=6)
