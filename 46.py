# 350 -7008

m, n, minim = 0, 0, 0
for i in range(-7018, -3791):
    if i % 6 == 0 and i % 7 != 0 and i % 19 != 0 and str(i)[-1] != '2':
        m += 1
        if n == 0:
            n += 1
            minim = i

print(m, minim)