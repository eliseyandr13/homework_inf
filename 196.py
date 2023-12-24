# 370 209813

lst = [int(i) for i in open('inf-main/inf-main/17-10.txt')]
cc = 0
all_ = 0
for i in range(2, len(lst)):
    x, y, z = lst[i - 2], lst[i - 1], lst[i]
    if (x ** 2 == y ** 2 + z ** 2) or (x ** 2 + y ** 2 == z ** 2) or (y ** 2 == z ** 2 + x ** 2):
        cc += 1
        all_ += max(x, y, z)
print(cc, all_)