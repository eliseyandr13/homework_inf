# 14 11350

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    

lst = [int(i) for i in open('inf-main/inf-main/17-243.txt')]
maxim = 0
for i in lst:
    if i % 107 == 0 and i > maxim:
        maxim = i
kol, minim = 0, 100000
for i in range(len(lst) - 1):
    if (lst[i] > maxim or lst[i + 1] > maxim) and ('36' in str(convert_base(lst[i], 7)) or '36' in str(convert_base(lst[i + 1], 7))):
        kol += 1
        if lst[i] + lst[i + 1] < minim:
            minim = lst[i] + lst[i + 1]
print(kol, minim)