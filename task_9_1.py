from time import sleep
from itertools import zip_longest


class TrafficLight:
    colors = ('\033[41m', '\033[43m', '\033[42m')

    def __init__(self, *colors):
        self.__colors = colors

    def running(self, *times):
        for attr, arg in zip_longest(TrafficLight.colors, self.__colors):
            if not attr == arg:
                print('Неверный порядок режимов')
                exit(-1)
        for color, time in zip(self.__colors, times):
            print(f"{color}    {time}    \033[0m")
            sleep(time)


red = '\033[41m'
yellow = '\033[43m'
green = '\033[42m'
traffic = TrafficLight(red, yellow, green)
traffic.running(7, 2, 4)
