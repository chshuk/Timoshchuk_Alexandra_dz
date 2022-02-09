list_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index_digit = -1
for i, element in enumerate(list_str):
    if i == index_digit:
        continue
    if element.isdigit():
        list_str.pop(i)
        list_str.insert(i, f'{int(element):02d}')
        list_str.insert(i, '"')
        list_str.insert(i + 2, '"')
        index_digit = i + 1
    elif element[1:].isdigit() and not element[0].isdigit():
        list_str.pop(i)
        list_str.insert(i, f'{element[0]}{int(element[1:]):02d}')
        list_str.insert(i, '"')
        list_str.insert(i + 2, '"')
        index_digit = i + 1
print(list_str)
string = ''
index = len(list_str)
for i, element in enumerate(list_str):
    if index - 2 < i <= index:
        continue
    if element == '"':
        string += ''.join(list_str[i:i+3]) + ' '
        index = i + 2
    else:
        string += element + ' '
print(string)

