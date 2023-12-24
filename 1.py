# 2151 9630

n, last = 0, 0
for i in range(1014, 9638, 3):
    if i % 3 == 0 and all([i % 11, i % 13, i % 17, i % 19]):
        n += 1
        if i > last: last = i
print(n, last)