from tkinter import *
import tkinter as tk
from tkinter import messagebox

def calc_bmi():
    # lấy giá trị
    h_s = entry_height.get().strip()
    w_s = entry_weight.get().strip()
    try:
        height = float(h_s)
        weight = float(w_s)
        if height <= 0 or weight <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập chiều cao (m) và cân nặng (kg) hợp lệ.")
        return

    bmi = weight / (height * height)
    bmi_display = f"{bmi:.2f}"
    label_bmi_value['text'] = bmi_display

    # phân loại (theo WHO)
    if bmi < 18.5:
        status = "Gầy"
        risk = "Nguy cơ: Thấp"
    elif bmi < 25:
        status = "Bình thường"
        risk = "Nguy cơ: Thấp"
    elif bmi < 30:
        status = "Thừa cân"
        risk = "Nguy cơ: Tăng"
    else:
        status = "Béo phì"
        risk = "Nguy cơ: Cao"

    label_status['text'] = status
    label_risk['text'] = risk

def clear_all():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    label_bmi_value['text'] = ""
    label_status['text'] = ""
    label_risk['text'] = ""

root = tk.Tk()
root.title("Máy tính BMI")

pad = 10
frm = tk.Frame(root, padx=pad, pady=pad)
frm.pack()

tk.Label(frm, text="Nhập chiều cao (m):").grid(row=0, column=0, sticky="w")
entry_height = tk.Entry(frm, width=12)
entry_height.grid(row=0, column=1, padx=6, pady=4)
entry_height.insert(0, "1.70")  # ví dụ

tk.Label(frm, text="Nhập cân nặng (kg):").grid(row=1, column=0, sticky="w")
entry_weight = tk.Entry(frm, width=12)
entry_weight.grid(row=1, column=1, padx=6, pady=4)
entry_weight.insert(0, "65")  # ví dụ

btn_calc = tk.Button(frm, text="Tính BMI", width=12, command=calc_bmi)
btn_calc.grid(row=2, column=0, columnspan=2, pady=(6,12))

tk.Label(frm, text="BMI của bạn:").grid(row=3, column=0, sticky="w")
label_bmi_value = tk.Label(frm, text="", width=12, relief="sunken")
label_bmi_value.grid(row=3, column=1, padx=6, pady=4)

tk.Label(frm, text="Tình trạng của bạn:").grid(row=4, column=0, sticky="w")
label_status = tk.Label(frm, text="", width=12, relief="sunken")
label_status.grid(row=4, column=1, padx=6, pady=4)

tk.Label(frm, text="Nguy cơ phát triển bệnh:").grid(row=5, column=0, sticky="w")
label_risk = tk.Label(frm, text="", width=20, relief="sunken")
label_risk.grid(row=5, column=1, padx=6, pady=4)

btn_clear = tk.Button(frm, text="Thoát/Clear", width=12, command=root.destroy)
btn_clear.grid(row=6, column=0, pady=10)
btn_reset = tk.Button(frm, text="Reset", width=12, command=clear_all)
btn_reset.grid(row=6, column=1, pady=10)

# bind Enter on weight to calculate quickly
entry_weight.bind("<Return>", lambda e: calc_bmi())

root.resizable(False, False)
root.mainloop()
