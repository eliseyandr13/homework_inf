# 832 460

lst = [int(i) for i in open('inf-main/inf-main/17-3.txt')]

cc = 0
minim = 10000
for i in range(2, len(lst)):
    if lst[i - 2] < lst[i - 1] < lst[i]:
        cc += 1
        minim = min(minim, lst[i] - lst[i - 2])
print(cc, minim)