# 587 -9996

def valid(x):
    return str(x)[-1] == '6' and x % 3 == 0

minim, all_ = 0, 0
lst = [int(i) for i in open('inf-main/inf-main/17-1.txt')]
for i in range(len(lst) - 1):
    if valid(lst[i]) or valid(lst[i + 1]):
        all_ += 1
        cc = min([lst[i], lst[i + 1]])
        if cc < minim:
            minim = cc

print(all_, minim)