from tkinter import *
from tkinter import messagebox
from math import sqrt

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")
    entryA.focus()

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
        return
    
    if a == 0:
        # Trở về phương trình bậc 1
        if b == 0:
            if c == 0:
                stringKQ.set("Vô số nghiệm")
            else:
                stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set(f"x = {-c/b}")
        return

    # PT bậc 2
    delta = b*b - 4*a*c

    if delta < 0:
        stringKQ.set("Vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        stringKQ.set(f"x1 = x2 = {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        stringKQ.set(f"x1 = {x1}, x2 = {x2}")

def thoatAction():
    root.destroy()

# -------------------- Giao diện --------------------
root = Tk()
root.title("PTB1")     # theo mẫu đề
root.minsize(height=230, width=310)

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="Phương Trình Bậc 2", fg="red",
      font=("tahoma", 16)).grid(row=0, columnspan=2, pady=10)

# Hệ số a
Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=W, padx=10)
entryA = Entry(root, width=25, textvariable=stringHSA)
entryA.grid(row=1, column=1)

# Hệ số b
Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=W, padx=10)
Entry(root, width=25, textvariable=stringHSB).grid(row=2, column=1)

# Hệ số c
Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=W, padx=10)
Entry(root, width=25, textvariable=stringHSC).grid(row=3, column=1)

# Nút bấm
Button(root, text="Giải", width=8, command=giaiAction).grid(row=4, column=0, pady=10)
Button(root, text="Tiếp", width=8, command=tiepAction).grid(row=4, column=1)
Button(root, text="Thoát", width=8, command=thoatAction).grid(row=4, column=2, padx=5)

# Kết quả
Label(root, text="Kết quả: ").grid(row=5, column=0, sticky=W, padx=10)
Label(root, textvariable=stringKQ).grid(row=5, column=1, sticky=W)

root.mainloop()
