def oscillate(start, end):
    for i in range(start, end + 1):
        yield i
        if i != 0 and i != end:   
            yield -i

# Thử chạy
for n in oscillate(-3, 4):   
    print(n, end=' ')
