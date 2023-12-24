# 337 10802

minim, maxim = 10000, 0
lst = [int(i) for i in open('inf-main/inf-main/17-4.txt')]
cc = 0
for i in lst:
    if (str(i)[-1] == '5' or str(i)[-1] == '7') and i % 9 != 0 and i % 11 != 0:
        cc += 1
        if i < minim:
            minim = i
        elif i > maxim:
            maxim = i

print(cc, minim + maxim)