def num_translate_adv(number):
    if number.istitle():
        return f'{dictionary.get(number.lower())}'.title()
    else:
        return f'{dictionary.get(number)}'


dictionary = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять',
              'zero': 'ноль'}

numb = input('напишите числительное от "zero" до "ten":  ')
print(num_translate_adv(numb))
