# 792 -587

lst = [int(i) for i in open('inf-main/inf-main/17-271.txt')]
summ = 0
for i in lst:
    summ += i
kol, maxim = 0, -100000
kopa = summ / len(lst)
for i in range(len(lst) - 1):
    if abs(lst[i]) % 10 + abs(lst[i + 1]) % 10 == 7:
        kol += 1
        if lst[i] < kopa and lst[i + 1] < kopa:
            maxim = max(maxim, lst[i] + lst[i + 1])
print(kol, maxim)


