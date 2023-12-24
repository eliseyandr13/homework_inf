# 202 6916

lst = [int(i) for i in open('inf-main/inf-main/17-4.txt')]
cc = 0
all_ = 0
minim = 10000
for i in lst:
    cc += i
cr = cc / len(lst)
for i in range(len(lst) - 1):
    x, y = lst[i], lst[i + 1]
    if (x > cr or y > cr) and (x + y) % 7 == 0:
        all_ += 1
        if x + y < minim:
            minim = x + y
print(all_, minim)