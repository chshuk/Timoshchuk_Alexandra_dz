numbers = []
for i in range(500):
    numbers.append((i * 2 + 1) ** 3)
sum_list = 0
for element in numbers:
    sum_el = 0
    el = element
    while True:
        sum_el += el % 10
        el = el // 10
        if el == 0:
            break
    if sum_el % 7 == 0:
        sum_list += element
print(f" сумма элементов равна {sum_list}")
sum_list17 = 0
for element in numbers:
    element += 17
    sum_el = 0
    el = element
    while True:
        sum_el += el % 10
        el = el // 10
        if el == 0:
            break
    if sum_el % 7 == 0:
        sum_list17 += element
print(f' сумма элементов+17 равна {sum_list17}')
