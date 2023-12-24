# 2311 1176

n, minnim, m = 0, 0, 1
for i in range(1170, 8368):
    if (i % 3 == 0 or i % 7 == 0) and all([i % 11, i % 13, i % 17, i % 19]):
        n += 1
        if m == 1: 
            minnim = i 
            m += 1
print(n, minnim)
