import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, ipadx=8, pady=10)

# tạo các nút
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('Clr',5,0)
]

for (text, r, c) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=equalpress).grid(row=r, column=c)
    elif text == "Clr":
        tk.Button(root, text=text, width=23, height=2, command=clear).grid(row=r, column=c, columnspan=4)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=r, column=c)

root.mainloop()
