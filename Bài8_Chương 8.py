from tkinter import *
import tkinter as tk
from tkinter import messagebox

def f_to_c():
    s = entry_f.get().strip()
    try:
        f = float(s)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho độ F")
        return
    c = (f - 32) * 5.0 / 9.0
    label_result['text'] = f"{c:.2f} °C"

root = tk.Tk()
root.title("Chuyển độ F → °C")

frm = tk.Frame(root, padx=12, pady=12)
frm.pack()

tk.Label(frm, text="Nhập độ F:").grid(row=0, column=0, sticky="w")
entry_f = tk.Entry(frm, width=12)
entry_f.grid(row=0, column=1, padx=6)

btn = tk.Button(frm, text="Chuyển", width=10, command=f_to_c)
btn.grid(row=0, column=2, padx=6)

tk.Label(frm, text="Độ C:").grid(row=1, column=0, sticky="w", pady=(8,0))
label_result = tk.Label(frm, text="--", width=12, relief="sunken")
label_result.grid(row=1, column=1, columnspan=2, pady=(8,0))

# Optional: bind Enter key
entry_f.bind("<Return>", lambda e: f_to_c())

root.resizable(False, False)
root.mainloop()
