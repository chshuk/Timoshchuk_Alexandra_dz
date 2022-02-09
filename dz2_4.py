list_stuff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in list_stuff:
    string = element.split(' ')[-1]
    print(f'Привет, {string.title()}!')