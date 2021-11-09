# Open Browser

# Author: @andvsilva
# date 2021-11-09

import webbrowser
from tkinter import *

root = Tk( )

root.title('Open Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')
    
mygoogle = Button(root, text='Open the Google', command=google).pack(pady=20)
root.mainloop()
    