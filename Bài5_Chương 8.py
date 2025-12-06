import tkinter as tk
from tkinter import messagebox

def ok_click():
    old = old_pass.get()
    new1 = new_pass.get()
    new2 = new_pass2.get()

    if new1 != new2:
        messagebox.showerror("Lỗi", "Mật khẩu mới không khớp!")
        return
    
    if old == "":
        messagebox.showerror("Lỗi", "Chưa nhập mật khẩu cũ!")
        return
    
    messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")

def cancel_click():
    root.destroy()

root = tk.Tk()
root.title("Enter New Password")

tk.Label(root, text="Old Password:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="New Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

old_pass = tk.Entry(root, show="*", width=25)
new_pass = tk.Entry(root, show="*", width=25)
new_pass2 = tk.Entry(root, show="*", width=25)

old_pass.grid(row=0, column=1, padx=10, pady=5)
new_pass.grid(row=1, column=1, padx=10, pady=5)
new_pass2.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="OK", width=10, command=ok_click).grid(row=3, column=0, pady=10)
tk.Button(root, text="Cancel", width=10, command=cancel_click).grid(row=3, column=1, pady=10)

root.mainloop()
