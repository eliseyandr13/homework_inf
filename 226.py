# 550 2378

lst = [int(i) for i in open('inf-main/inf-main/17-4.txt')]
sum_of = 0
for i in lst:
    sum_of += i
col, minim = 0, 10000
for i in range(len(lst) - 1):
    if (lst[i] < (sum_of / len(lst)) or lst[i + 1] < (sum_of / len(lst))) and '4' not in str(lst[i]) and '4' not in str(lst[i + 1]):
        col += 1
        if lst[i] + lst[i + 1] < minim:
            minim = lst[i] + lst[i + 1]
print(col, minim)
