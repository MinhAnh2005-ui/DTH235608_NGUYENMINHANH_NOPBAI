import math

print("Tính log_a(x)")
a = float(input("Nhập cơ số a (>0, a≠1): "))
x = float(input("Nhập số x (>0): "))

if a > 0 and a != 1 and x > 0:
    kq = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {kq}")
else:
    print("Điều kiện không hợp lệ (a>0, a≠1, x>0).")
