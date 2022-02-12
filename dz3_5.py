import random


def get_jokes(*args, n=1, flag=False):
    """ Generation of n jokes using lists of args """
    jokes = []
    list_flag = []
    for i in range(n):
        joke = []
        for elem in args:
            word = random.choice(elem)
            if flag:
                while word in list_flag:
                    flag_element = True
                    for el in elem:
                        if el not in list_flag:
                            flag_element = False
                    if flag_element:
                        word = ''
                        break
                    word = random.choice(elem)
                list_flag.append(word)
            joke.append(word)
        jokes.append(' '.join(joke))
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
count = int(input('Сколько нужно шуток?  '))
for element in get_jokes(nouns, adverbs, adjectives, n=count, flag=True):
    print(element)
