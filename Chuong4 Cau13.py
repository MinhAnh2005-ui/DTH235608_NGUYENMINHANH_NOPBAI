def tong_uoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def so_hoan_thien(n):
    return tong_uoc(n) == n

def so_thinh_vuong(n):
    return tong_uoc(n) > n

# Test
n = int(input("Nhập số n: "))
if so_hoan_thien(n):
    print(n, "là số hoàn thiện")
elif so_thinh_vuong(n):
    print(n, "là số thịnh vượng")
else:
    print(n, "không phải số hoàn thiện cũng không phải số thịnh vượng")
