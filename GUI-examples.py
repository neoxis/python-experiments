from tkinter import *

##########
###MAIN###
window = Tk()
window.title("GUI Examples")

window.geometry('500x500') #size of window

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
'''Example 3 - font color'''
b = Button(window, text="Click Me", fg="blue")

b.grid(column=1, row=0)
