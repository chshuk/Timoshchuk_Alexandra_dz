def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


limit = int(input('введите максимальное число:  '))
gen_nums = odd_nums(limit)
print(*gen_nums)
