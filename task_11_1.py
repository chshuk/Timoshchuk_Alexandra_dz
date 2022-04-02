class Date:
    def __init__(self, date_str):
        self.date_str = date_str
        self.day = 0
        self.month = 0
        self.year = 0

    @classmethod
    def transformation(cls, obj):
        date_list = obj.date_str.split('-')
        obj.day = int(date_list[0])
        obj.month = int(date_list[1])
        obj.year = int(date_list[2])
        return f'Число - {obj.day}, месяц - {obj.month}, год - {obj.year}'

    @staticmethod
    def validation(obj):
        mon = obj.month
        day = obj.day
        year = obj.year
        if 0 < mon < 13:
            if (mon in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32) \
                    or (mon in [4, 6, 9, 11] and 0 < day < 31)\
                    or (mon == 2 and 29 > day > 0 != year % 4)\
                    or (mon == 2 and 30 > day > 0 == year % 4):
                return "все хорошо"
        return "неверная дата"


date = Date('01-04-2022')
date.transformation(date)
print(date.validation(date))
str_date_1 = input("Введите дату в формате 'число-месяц-год':  ")
date_1 = Date(str_date_1)
Date.transformation(date_1)
print(Date.validation(date_1))
