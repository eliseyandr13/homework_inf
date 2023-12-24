# 9069 505554

m, n, maxim = 0, 0, 0
for i in range(1007, 746002):
    smth = [int(j) for j in str(i)]
    if int(str(i)[0]) == max(smth) and str(i).count('5') >= 2 and str(i).count('5') % 2 == 0:
        n += 1
        if i > maxim and str(i)[:2] == '50':
            maxim = i
print(n, maxim)