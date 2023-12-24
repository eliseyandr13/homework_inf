# 51950 25

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

sum, n = 0, 0
for i in range(697, 3459):
    if str(convert_base(i, 16))[-1] == 'E' and str(convert_base(i, 7))[-1] == str(convert_base(i, 8))[-1]:
        sum += i
        n += 1

print(sum, n)