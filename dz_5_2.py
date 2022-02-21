limit_2 = int(input('Введите максимальное число:  '))
nums_gen = (num for num in range(1, limit_2 + 1, 2))
print(*nums_gen)
