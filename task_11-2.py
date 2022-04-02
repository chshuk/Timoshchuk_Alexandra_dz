class MyExcept(Exception):
    def __init__(self, text):
        self.text = text


try:
    divider = int(input('Введите делитель, отличный от 0:  '))
    if not divider:
        raise MyExcept('Вы ввели недопустимое значение. на ноль делить нельзя')
    res = 100 / divider
except ZeroDivisionError:
    print('На ноль делить нельзя')
except MyExcept as exc:
    print(exc)
else:
    print(f"все хорошо. результат = {res}")
finally:
    print("Hi")
