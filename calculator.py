from tkinter import *
import re
math = ''

root = Tk()
root.title("Simple Calculator")

BOARD = [['1', '2', '3', '+'],
         ['4', '5', '6', '-'],
         ['7', '8', '9', '*'],
         ['=', '0', '/', 'CC']]

e = Entry(root,width=50, borderwidth=7, bg = "black", fg = "white")
e.grid(row=0, column=0, columnspan=4, padx=25, pady=10)

def Click():
    pass

def add(num):
    sign = re.compile("[\d*][\W][\d*]")
    if num == 'cc':
        e.delete(0, END)
    # elif sign.finditer(num):
    #     current = e.get()
    #     e.delete(0, END)
    #     STR = str(current) + str(num)
    #     e.insert(0, STR)
    elif num == "=":
        STR = str(e.get())
        condition = re.search(sign, STR)
        if condition != None: 
            STR = str(eval(e.get()))
            e.delete(0, END)
            e.insert(0, STR)
        else: print("not working")
    else:
        current = e.get()
        e.delete(0, END)
        STR = str(current) + str(num)
        e.insert(0, STR)

    

# Number
btn_1 = Button(root, text = '1', padx=40, pady=20, command=lambda: add(1))
btn_2 = Button(root, text = '2', padx=40, pady=20, command=lambda: add(2))
btn_3 = Button(root, text = '3', padx=40, pady=20, command=lambda: add(3))
btn_4 = Button(root, text = '4', padx=40, pady=20, command=lambda: add(4))
btn_5 = Button(root, text = '5', padx=40, pady=20, command=lambda: add(5))
btn_6 = Button(root, text = '6', padx=40, pady=20, command=lambda: add(6))
btn_7 = Button(root, text = '7', padx=40, pady=20, command=lambda: add(7))
btn_8 = Button(root, text = '8', padx=40, pady=20, command=lambda: add(8))
btn_9 = Button(root, text = '9', padx=40, pady=20, command=lambda: add(9))
btn_0 = Button(root, text = '0', padx=40, pady=20, command=lambda: add(0))

btn_A = Button(root, text = '+', padx=40, pady=20, command=lambda: add('+'))
btn_S = Button(root, text = '-', padx=40, pady=20, command=lambda: add('-'))
btn_M = Button(root, text = '*', padx=40, pady=20, command=lambda: add('*'))
btn_D = Button(root, text = '/', padx=40, pady=20, command=lambda:add('/'))
btn_E = Button(root, text = '=', padx=40, pady=20, command=lambda: add('='))
btn_CC = Button(root, text = 'CC', padx=40, pady=20, command=lambda: add('cc'))

btn_1.grid(row=1,column=0)
btn_2.grid(row=1,column=1)
btn_3.grid(row=1,column=2)
btn_A.grid(row=1,column=3)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_S.grid(row=2,column=3)

btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)
btn_M.grid(row=3,column=3)

btn_CC.grid(row=4,column=0)
btn_0.grid(row=4,column=1)
btn_E.grid(row=4,column=2)
btn_D.grid(row=4,column=3)

btn_click = Button(root, text = e.get(), command=Click)

root.mainloop()


# Tried and failed
"""
btn = []
for i in range(4):
    for j in range(4):
        btn.append(Entry(root, text=BOARD[i][j], command=add))
        btn[-1].grid(row = i, column = j+1, padx=40, pady=20)
        """
