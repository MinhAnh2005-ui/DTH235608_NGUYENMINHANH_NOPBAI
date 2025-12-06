from tkinter import *
import tkinter as tk
from tkinter import messagebox

can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def convert():
    try:
        year = int(entry_year.get())
        can_name = can[(year + 6) % 10]
        chi_name = chi[(year + 8) % 12]
        result_var.set(f"{can_name} {chi_name}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm hợp lệ!")

root = tk.Tk()
root.title("Đổi Năm Dương → Âm")

tk.Label(root, text="Nhập năm dương:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)

entry_year = tk.Entry(root, width=15, font=("Arial", 12))
entry_year.grid(row=0, column=1, padx=10, pady=10)

btn = tk.Button(root, text="Chuyển", font=("Arial", 12), width=10, command=convert)
btn.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Năm âm:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue").grid(row=1, column=1, columnspan=2)

root.mainloop()
