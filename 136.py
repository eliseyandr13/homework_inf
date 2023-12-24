# 18979

from typing import Final


bounds: Final = (4855, 7856 + 1)

def check_digits_parity(number: int):
    return ((number % 1000) // 100 + (number % 100) // 10) % 2 == 0


array = []

for number in range(*bounds):
    if (number % 30 == 0 and number % 7 != 0 and number % 16 != 0 and check_digits_parity(number)):
        array.append(number)


# aggregate
min_number = min(array)
max_number = max(array)
average = sum(array) / len(array)

print(min_number + max_number + int(average))