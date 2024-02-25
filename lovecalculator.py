import random
from tkinter import *
import random 
root = Tk() 
root.geometry('400x300') 
root.title('what to calculate your love ???') 
def calculate_love(): 
    digit=random.randint(40,99)
    result.config(text=digit) 
heading = Label(root, text='calculate your love with rajashree') 
heading.pack() 
slot1 = Label(root, text="your name:") 
slot1.pack() 
name1 = Entry(root, border=10) 
name1.pack() 
slot2 = Label(root, text="Your Partner Name:")
slot2.pack() 
name2 = Entry(root, border=10) 
name2.pack() 
bt = Button(root, text="Calculate", height=1, 
            width=7, command=calculate_love) 
bt.pack() 
result = Label(root, text='love between you guys:') 
result.pack() 
root.mainloop()