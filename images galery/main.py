from tkinter import *
from typing import ChainMap 
from PIL import ImageTk, Image
import shutil, os
from tkinter import filedialog

root = Tk()
root.title('Galery')
root.geometry('400x200')
root.configure(bg='white')

directory = r'c:\Users\jazza\OneDrive\سطح المكتب\may work\tkinter\images galery\images'
images = []
name = ''

dil = ''




def open(loca):
    global directory
    top = Toplevel()
    top.title = name
    print(name)
    image = (Image.open(loca))
    width, height = image.size
    print(width, height)
    if height > 800 or width > 2500:
        image = image.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
        width, height = image.size
        print(width, height)
    
    if height > 800 or width > 2500:
        image = image.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
        width, height = image.size
        print(width, height)

    if height > 800 or width > 2500:
        image = image.resize((int(width/1.2), int(height/1.2)), Image.ANTIALIAS)
        width, height = image.size
        print(width, height)
    
    width, height = image.size
    image = ImageTk.PhotoImage(image)
    images.append(image)
    lb = Label(top, image=image).pack()    
    but = Button(top, text='return', command=top.destroy).pack()


col = 0
row = 1

multi6 = []

for num in range(100):
    multi6.append(num * 6)

# print(multi6)

col = 0
row = 1


def add(directory_name, page):
    global image
    global row
    global col
    filename = filedialog.askopenfilename(initialdir='/', title='select',  filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))
    print(filename)
    shutil.copy(filename, directory_name)
    image = (Image.open(filename))
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    bt = Button(page, image=image, command=lambda filename=filename: open(filename)).grid(row=row, column=col)
    col += 1
    if col in multi6:
        row += 1
        col = 0   


def opendil():
    global dil
    global row
    global col
    col = 0
    row = 1
    dil = filedialog.askdirectory(initialdir='/', title='select')
    file = Toplevel()
    add_button = Button(file, text='Add+', command= lambda: add(dil, file))
    add_button.grid(row=0, column=0, columnspan=6, pady=10, sticky=W+E)
    print(dil)
    for filename in os.listdir(dil):
        loca = f'{dil}/{filename}'
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image = (Image.open(f'{dil}/{filename}'))
            image = image.resize((100, 100), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            images.append(image)
            bt = Button(file, text=name, image=image, command=lambda loca=loca: open(loca)).grid(row=row, column=col)
            col += 1
            if col in multi6:
                row += 1
                col = 0        
        else:
            continue

import_img = (Image.open('import_bt.jpg'))
width, height = import_img.size
import_img = import_img.resize((int(width/5), int(height/5)), Image.ANTIALIAS)
import_img = ImageTk.PhotoImage(import_img)


dil_button = Button(root, image=import_img, border=0,command=opendil).pack()

print('hay')



root.mainloop()