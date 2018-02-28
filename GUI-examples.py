from tkinter import *

#Button Functions#
def clicked():
        l.configure(text="Clicked!!!")

##########
###MAIN###
window = Tk()
window.title("GUI Examples")

window.geometry()       #window grows to show contents
#window.geometry('500x500') # define size of window

window.mainloop


##########
##Labels##
'''Example 1 - simple text '''
l = Label(window, text="Hello")
'''Example 2 - font '''
#l = Label(window, text="Hello", font=("Arial Bold", 75))

l.grid(column=0, row=0)         #location in window

###########
##Buttons##
'''Example 1 - simple button '''
#b = Button(window, text="Click Me")
'''Example 2 - background color '''
#b = Button(window, text="Click Me", bg="yellow")
'''Example 3 - text color '''
#b = Button(window, text="Click Me", fg="blue")
'''Example 4 - calling function '''
b = Button(window, text="Click Me", command=clicked)

b.grid(column=2, row=0)


##Entry##
#########
'''Example 1 - simple entry '''
#txt = Entry(window)
'''Example 2 - width '''
#txt = Entry(window, width=10)
'''Example 3 - background color '''
#txt = Entry(window, bg="red")
'''Example 4 - text color '''
#txt = Entry(window, fg="green")
'''Example 5 - border '''
#txt = Entry(window, bd=10)
'''Example 6 - cursor '''
#txt = Entry(window, cursor="dot")
'''Example 7 - font '''
#txt = Entry(window, font=("Arial", 15))
'''Example 8 - selected text background  color '''
#txt = Entry(window, selectbackground="pink")
'''Example 9 - selected text color '''
txt = Entry(window, selectbackground="pink", selectforeground="blue")


txt.grid(column=1, row=0)
