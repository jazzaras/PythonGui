from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')

## if you want to make the variable in the radio button an int
# r = IntVar()

## we set radio button to be the second option automatically 
# r.set('2')


# Doing multuble choices esely
MODES = [
    ('peperoni', 'peperoni'),
    ('mashrom', 'mashrom'),
    ('chess', 'chess'),
    ('oninon', 'oninon'),
]

## if you want to make the variable in the radio button an Srting
pizza = StringVar()

# u can set it to None
pizza.set('peperoni')

## anchor = W , buts all the radio circles on one side (W=west,N=north etc)

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


# Radiobutton(root, text='option1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='option2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

def clicked(value):
    myl = Label(root, text=value)  
    myl.pack()

# myl = Label(root, text=pizza.get())
# myl.pack()

# you can do that too
# try it to understand \/

mybutton = Button(root, text='click me', command=lambda: clicked(pizza.get()))
mybutton.pack()

root.mainloop()

