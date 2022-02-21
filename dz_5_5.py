from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
repeated_elem = set()
unrepeated_elem = set()
for element in src:
    if element not in repeated_elem:
        unrepeated_elem.add(element)
    elif element in unrepeated_elem:
        unrepeated_elem.discard(element)
    repeated_elem.add(element)
result = [elem for elem in src if elem in unrepeated_elem]
print(result, perf_counter() - start)