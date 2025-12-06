from tkinter import *
import tkinter as tk
from tkinter import messagebox

# hàm cộng
def cong():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        kq_var.set(a + b)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số!")
        kq_var.set("")

# hàm trừ
def tru():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        kq_var.set(a - b)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số!")
        kq_var.set("")

# hàm nhân
def nhan():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        kq_var.set(a * b)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số!")
        kq_var.set("")

# hàm chia
def chia():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if b == 0:
            messagebox.showerror("Lỗi", "Không thể chia cho 0!")
            kq_var.set("")
        else:
            kq_var.set(a / b)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số!")
        kq_var.set("")

# thoát
def thoat():
    root.destroy()

root = tk.Tk()
root.title("Cộng trừ nhân chia")

# ----- CÁC NÚT BÊN TRÁI -----
btn_cong = tk.Button(root, text="Cộng", width=8, command=cong)
btn_tru  = tk.Button(root, text="Trừ",  width=8, command=tru)
btn_nhan = tk.Button(root, text="Nhân", width=8, command=nhan)
btn_chia = tk.Button(root, text="Chia", width=8, command=chia)

btn_cong.grid(row=0, column=0, padx=5, pady=5)
btn_tru.grid(row=1, column=0, padx=5, pady=5)
btn_nhan.grid(row=2, column=0, padx=5, pady=5)
btn_chia.grid(row=3, column=0, padx=5, pady=5)

# ----- CÁC NHÃN & Ô NHẬP BÊN PHẢI -----
tk.Label(root, text="số a:").grid(row=0, column=1, sticky="e", padx=5, pady=5)
tk.Label(root, text="số b:").grid(row=1, column=1, sticky="e", padx=5, pady=5)
tk.Label(root, text="kết quả:").grid(row=2, column=1, sticky="e", padx=5, pady=5)

entry_a = tk.Entry(root, width=15)
entry_b = tk.Entry(root, width=15)
entry_a.grid(row=0, column=2, padx=5, pady=5)
entry_b.grid(row=1, column=2, padx=5, pady=5)

kq_var = tk.StringVar()
entry_kq = tk.Entry(root, textvariable=kq_var, width=15)
entry_kq.grid(row=2, column=2, padx=5, pady=5)

# nút thoát
btn_thoat = tk.Button(root, text="thoát", width=8, command=thoat)
btn_thoat.grid(row=3, column=2, sticky="e", padx=5, pady=5)

root.mainloop()
