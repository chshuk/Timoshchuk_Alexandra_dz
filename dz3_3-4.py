

def thesaurus(*args):
    dictionary_staff = {}
    for employee in args:
        first_name = employee.split(' ')[0]
        last_name = employee.split(' ')[-1]
        dictionary_staff.setdefault(last_name[0], {}).setdefault(first_name[0], []).append(employee)
    return dictionary_staff


list_staff = ['Александра Тимощук', 'Махмуд Кахтан',
              'Амира Кахтан', 'Петр Мамонов',
              'Кристина Олегова', 'Игнат Сидоров',
              'Армен Кеосаян', 'Владимир Путин',
              'Сергей Светлов', 'Михаил Косолапов',
              'Любовь Орлова', 'Вячеслав Песков', 'Олег',
              'Иосиф Висарионович Сталин']
string_staff = input("Введите сотрудников через запятую:  ")
if string_staff:
    list_staff.extend(string_staff.split(', '))
print(*list_staff, sep='\n')
dict_staff = thesaurus(*list_staff)
for item in dict_staff.items():
    print(item)
