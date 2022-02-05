duration = int(input("Введите продолжительность в секундах:  "))

print(f" {duration} сек соответствует: ")
if duration < 60:
    print(f"{duration} сек")
else:
    minute = duration // 60
    sec = duration % 60
    if minute < 60:
        print(f"{minute} мин {sec} сек")
    else:
        hours = minute // 60
        minute = minute % 60
        if hours < 24:
            print(f"{hours} час {minute} мин {sec} сек")
        else:
            day = hours // 24
            hours = hours % 24
            print(f"{day} дн {hours} час {minute} мин {sec} сек")
