import time
import threading
from tkinter import *

def convert(string):
    list1 = []
    list1[:0] = string
    return string
str1 = 'Hey I am Mahin Bin Hasan . . .'

name=convert(str1)
def t():
    i = 0
    n = ''
    while i < len(name):
        n = n + name[i]
        h.config(text = n)
        time.sleep(0.05)
        i = i + 1
    t()
def th():
    f = threading.Thread(target=t).start()
root = Tk()
root.geometry('500x200')
root.title('GGGGGGGGGGGGGGG')

h = Label(root,text = '' ,font=('',15))
h.pack()
th()
root.mainloop()