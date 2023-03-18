import builtins
from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.resizable(0,0)

e = Entry(root, width=45, borderwidth=5, font = "Calibri 11")
e.grid(row=0, column=0, columnspan=5, ipady=10, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))   

dij_num = 0

# if current != '' and current[-1] != '+':
#     e.delete(0, END)
#     e.insert(0,str(current) + '+')

global sign
sign = ''

def button_add():
    global f_num
    first_number = e.get()
    if first_number == '':
        print('not valid')
        return ''
    f_num = float(first_number)
    global sign
    sign = 'plus'
    print(f_num)
    if first_number == '':
        return ''
    e.delete(0, END)
    


def button_multiply():
    global f_num
    first_number = e.get()
    if first_number == '':
        print('not valid')
        return ''
    f_num = float(first_number)
    global sign
    sign = 'multi'
    print(f_num)
    if first_number == '':
        return ''
    e.delete(0, END)
    

def button_minus():
    global f_num
    first_number = e.get()
    if first_number == '':
        print('not valid')
        return ''
    f_num = float(first_number)
    global sign
    sign = 'minus'
    print(f_num)
    if first_number == '':
        return ''
    e.delete(0, END)
    

def button_divide():
    global f_num
    first_number = e.get()
    if first_number == '':
        print('not valid')
        return ''
    f_num = float(first_number)
    global sign
    sign = 'divide'
    print(f_num)
    if first_number == '':
        return ''
    e.delete(0, END)
    
    


def button_equal():
    second_number = e.get()
    if second_number == '':
        return ''
    s_num = float(second_number)
    print(s_num)
   
    if sign == 'plus':
        equal_num = s_num + f_num
        e.delete(0, END)
        e.insert(0, equal_num)
   
    if sign == 'multi':
        equal_num = s_num * f_num
        e.delete(0, END)
        e.insert(0, equal_num)

    if sign == 'minus':
        equal_num = f_num - s_num 
        e.delete(0, END)
        e.insert(0, equal_num)

    if sign == 'divide':
        equal_num = f_num / s_num
        e.delete(0, END)
        e.insert(0, equal_num)



# current = e.get()
# numbers = current.split('+')
# print(numbers)
# try:
#     for i in range(len(numbers)):
#         numbers[i] = int(numbers[i])
#     e.delete(0, END)
#     e.insert(0, sum(numbers))
# except:
#     print('not working')
#     e.delete(0, END)
    




# define buttons

button_1 = Button(root, text='1', pady=20, padx=40, command=lambda: button_click(1))
button_2 = Button(root, text='2', pady=20, padx=40, command=lambda: button_click(2) )
button_3 = Button(root, text='3', pady=20, padx=40, command=lambda: button_click(3))
button_4 = Button(root, text='4', pady=20, padx=40, command=lambda: button_click(4))
button_5 = Button(root, text='5', pady=20, padx=40, command=lambda: button_click(5))
button_6 = Button(root, text='6', pady=20, padx=40, command=lambda: button_click(6))
button_7 = Button(root, text='7', pady=20, padx=40, command=lambda: button_click(7))
button_8 = Button(root, text='8', pady=20, padx=40, command=lambda: button_click(8))
button_9 = Button(root, text='9', pady=20, padx=40, command=lambda: button_click(9))
button_0 = Button(root, text='0', pady=20, padx=40, command=lambda: button_click(0))
button_dot = Button(root, text='.', pady=20, padx=42, command=lambda: button_click('.'))

button_add = Button(root, text='+', pady=52, padx=39,command=button_add)
button_multiply = Button(root, text='x', pady=20, padx=39,command=button_multiply)
button_minus = Button(root, text='-', pady=20, padx=39,command=button_minus)
button_divide = Button(root, text='÷', pady=20, padx=39,command=button_divide)

button_equal = Button(root, bg='lightgreen', text='=', pady=20, padx=87.5,command=button_equal)
button_clear = Button(root, bg='orange', text='Clear', pady=20, padx=78.4, command=lambda: e.delete(0, END))


# put buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_dot.grid(row=5,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=4, column=4, rowspan=2)
button_multiply.grid(row=1, column=4)
button_minus.grid(row=2, column=4)
button_divide.grid(row=3, column=4)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop() 