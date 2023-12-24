# 18021 76432

def ok(x):
  count = 2
  q = round(x ** 0.5)
  if q * q == x:
    count += 1
    q -= 1
  for i in range(2, q + 1):
    if x % i == 0:
      count += 2
  return count > 15

cc, maxim = 0, 0
for x in range(12356, 76435 + 1):
  if ok(x):
    cc += 1
    maxim = x

print(cc, maxim)