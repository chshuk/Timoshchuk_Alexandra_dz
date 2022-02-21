from itertools import zip_longest
from time import perf_counter


def klasses_gen(list_klasses):
    for klass in list_klasses:
        yield klass


def tutors_gen(list_1, list_2):
    gen_klasses = klasses_gen(list_2)
    for name in list_1:
        yield name, next(gen_klasses)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Олег']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '9B', '7A', '8Б']
start = perf_counter()
if len(tutors) > len(klasses):
    tutor_klass = (elem for elem in zip_longest(tutors,klasses))
else:
    tutor_klass = (elem for elem in zip(tutors, klasses))
print(type(tutor_klass))
print(*tutor_klass)
print(start - perf_counter())

start = perf_counter()
if len(tutors) > len(klasses):
    for _ in range(len(tutors) - len(klasses)):
        klasses.append(None)
tutor_klass = tutors_gen(tutors, klasses)
print(type(tutor_klass))
print(*tutor_klass)
print(start - perf_counter())
