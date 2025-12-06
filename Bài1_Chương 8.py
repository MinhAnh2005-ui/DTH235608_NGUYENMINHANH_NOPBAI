from tkinter import *
from tkinter import messagebox

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")
    entryA.focus()

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
        return
    
    if a == 0 and b == 0:
        stringKQ.set("Vô số nghiệm")
    elif a == 0 and b != 0:
        stringKQ.set("Vô nghiệm")
    else:
        x = -b / a
        stringKQ.set(f"x = {x}")

def thoatAction():
    root.destroy()

# -------------------- Giao diện --------------------
root = Tk()
root.title("PTB1")
root.minsize(height=200, width=300)

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="Phương Trình Bậc 1", fg="red",
      font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2, pady=10)

# Hệ số a
Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=W, padx=10)
entryA = Entry(root, width=25, textvariable=stringHSA)
entryA.grid(row=1, column=1)

# Hệ số b
Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=W, padx=10)
Entry(root, width=25, textvariable=stringHSB).grid(row=2, column=1)

# Nút bấm
Button(root, text="Giải", width=8, command=giaiAction).grid(row=3, column=0, pady=10)
Button(root, text="Tiếp", width=8, command=tiepAction).grid(row=3, column=1)
Button(root, text="Thoát", width=8, command=thoatAction).grid(row=3, column=2, padx=5)

# Kết quả
Label(root, text="Kết quả: ").grid(row=4, column=0, sticky=W, padx=10)
Label(root, textvariable=stringKQ).grid(row=4, column=1, sticky=W)

root.mainloop()
