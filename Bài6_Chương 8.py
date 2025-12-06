import tkinter as tk

root = tk.Tk()
root.title("Button Styles")

styles = ["flat", "raised", "sunken", "ridge", "groove", "solid"]

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i in range(6):
    tk.Label(frame, text=f"borderwidth = {i+1}").grid(row=i, column=0, padx=5, pady=5)
    
    for j, s in enumerate(styles):
        btn = tk.Button(frame, text=s, relief=s, borderwidth=i+1, width=10)
        btn.grid(row=i, column=j+1, padx=5, pady=5)

root.mainloop()
