# 646 3312617
n, m = 0, 0
for i in range(2738, 7515):
    if i % 7 == 0 and i % 19 != 0:
        n += 1
        m += i
print(n, m)