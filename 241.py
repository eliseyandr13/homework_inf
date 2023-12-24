# 1344 7751

lst = [int(i) for i in open('inf-main/inf-main/17-1.txt')]
sum_of = 0
for i in lst:
    sum_of += i
tope = sum_of / len(lst)
kol, maxim = 0,  0
for i in range(2, len(lst)):
    if [lst[i - 2] < tope, lst[i - 1] < tope, lst[i] < tope].count(True) >= 2 and ['5' in str(lst[i - 2]), '5' in str(lst[i - 1]), '5' in str(lst[i])].count(True) >= 2:
        kol += 1
        if lst[i - 2] + lst[i - 1] + lst[i] > maxim:
            maxim = lst[i - 2] + lst[i - 1] + lst[i]

print(kol, maxim)