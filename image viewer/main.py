from tkinter import * 
from PIL import ImageTk, Image
import os

root = Tk()
root.title('image viewer')


directory = r'c:\Users\jazza\Desktop\me\programing\GUI\Python\image viewer\images'
images = []

# getting images from folder 
# and making them a tkimage(ImageTk)
# and opening them 
# and finally appending them to images list

for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        x = filename.split('\&')
        name = x.pop()
        image = (Image.open(f'images\{name}'))
        image = image.resize((450, 350), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        print(image)
        images.append(image)
        continue
    else:
        continue
 
# the status bar

status = Label(root, bd=1, relief=SUNKEN, anchor=E ,text=f'image 1 of {len(images)}')

# the picture

my_lable = Label(image=images[0])
my_lable.grid(row=0, column=0, columnspan=3)

def forword(image_num):
    global my_lable
    global button_back
    global button_forward
    global status

    
    my_lable.grid_forget()

    my_lable = Label(image=images[image_num-1])
    button_forward = Button(root, text='>>',command=lambda: forword(image_num + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_num - 1))
    
    status = Label(root, bd=1, relief=SUNKEN, anchor=E ,text=f'image {image_num} of {len(images)}')
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    # if it is the last image : DISABLE

    if image_num == len(images):
        button_forward = Button(root, text='>>', state=DISABLED)


    my_lable.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    




def back(image_num):
    global my_lable
    global button_back
    global button_forward

    my_lable.grid_forget()

    my_lable = Label(image=images[image_num-1])
    button_forward = Button(root, text='>>',command=lambda: forword(image_num + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_num - 1))
    
    status = Label(root, bd=1, relief=SUNKEN, anchor=E ,text=f'image {image_num} of {len(images)}')
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    # if it is the first image : DISABLE

    if image_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)


    my_lable.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='>>',command=lambda: forword(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1, column=2, pady=10)

# the sticky strich the lable fron W TO E (WEST TO EAST)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()