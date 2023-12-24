# 550 3136

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

m, n, minim = 0, 0, 0
for i in range(1000, 10000):
    smth = str(convert_base(i, 5, 10))
    if len(smth) >= 6 and (smth[-2:] == '21' or smth[-2:] == '23'):
        m += 1
        if n == 0:  
            minim = i
            n += 1

print(m, minim)
