from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('training')
root.geometry()

### FRAMES ###

# frame = LabelFrame(root, text='Personal Inoformation', padx=5, pady=5)
# frame.pack(padx=10, pady=10)

# b = Button(frame, text='click me')
# b.pack()

### messagebox types
# showinfo, showerror, showwarning, askokcancel, askquestion, askyesno

# def pop():
# 	res = messagebox.askq uestion ('popup', 'HelloWorld!')
# 	Label(root, text=res).pack()

# myb = Button(root, text='pop',  command=pop)
# myb.pack()

### FILE DIALOG 

# filename = filedialog.askopenfilename(initialdir='/', title='select', filetypes=(('png files', '*.png'), ('all files', '*.*')))
# my_l = Label(root, text=filename).pack()


### SLIDER(SCROLL)
img = Image.open('training.png')
img = ImageTk.PhotoImage(img)


l = Label(root, image=img).pack()

def size(va):
	root.geometry(f'{ver.get()}x{ver.get()}')


ver = Scale(root, from_=500, to=1000, command=size)
ver.set(1000)
ver.pack()
root.mainloop()