# 18058 876157

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

amount, maxim = 0, 0
for i in range(198372, 876194):
    if i % sum_digits(i) == 11:
        amount += 1
        if i > maxim:
            maxim = i

print(amount, maxim)