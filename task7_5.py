import os


def degree(num):
    i = 0
    while num:
        i += 1
        num = num // 10
    return i


def stat_file(fold, i):
    count = 0
    ext = []
    for elem in os.scandir(fold):
        size_elem = elem.stat().st_size
        if (i > 0 and 10 ** (i - 1) < size_elem <= 10 ** i) or (i == 0 and size_elem <= 1):
            count += 1
            ex = os.path.splitext(elem.name)[1]
            if ex not in ext:
                ext.append(ex)
    return count, ext


folder = 'some_data'
files = {}
max_size = 0
min_size = 10000
for item in os.scandir(folder):
    size = item.stat().st_size
    if max_size < size:
        max_size = size
    if min_size > size:
        min_size = size
min_degree_key = degree(min_size)
max_degree_key = degree(max_size)
for key in range(min_degree_key, max_degree_key + 1):
    files[10 ** key] = stat_file(folder, key)
for key, item in sorted(files.items()):
    print(f'{key}: {item}')
