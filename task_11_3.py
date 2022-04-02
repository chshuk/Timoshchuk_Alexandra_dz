class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Stop(Exception):
    def __init__(self, text):
        self.text = text


elem_list = []
while True:
    try:
        element = input("Введите число: ")
        if element == 'stop':
            raise Stop('Вы остановили работу скрипта')
        if not element.isdigit():
            raise MyError('Вводите только числа!')
    except MyError as err:
        print(err)
    except Stop as err:
        print(err)
        break
    else:
        elem_list.append(int(element))
for elem in elem_list:
    print(elem)
