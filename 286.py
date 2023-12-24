# 1703 2281

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
    
def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
    
lst = [int(i) for i in open('inf-main/inf-main/17-282.txt')]
minim = 10000
for i in range(len(lst)):
    if lst[i] % 21 == 0 and lst[i] < minim:
        minim = lst[i]
sum_min = getSum(convert_base(abs(minim), 8))
kol = 0
minimin = 10000
for i in range(len(lst) - 1):
    if getSum(convert_base(abs(lst[i]), 8)) == sum_min or getSum(convert_base(abs(lst[i + 1]), 8)) == sum_min:
        kol += 1
        if lst[i] + lst[i + 1] < minimin:
            minimin = lst[i] + lst[i + 1]
print(kol, minimin)