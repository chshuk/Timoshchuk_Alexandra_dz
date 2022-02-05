for percent in range(1, 200):
    if 5 < percent % 100 < 20:
        str_percent = "процентов"
    elif percent % 10 == 1:
        str_percent = "процент"
    elif 1 < percent % 10 < 5:
        str_percent = "процента"
    else:
        str_percent = "процентов"
    print(percent, str_percent)
