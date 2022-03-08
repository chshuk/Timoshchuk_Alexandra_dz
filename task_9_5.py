class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Чертеж карандошом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Выделение маркером {self.title}')


pen = Pen('Rimm')
pencil = Pencil('Power')
handle = Handle('Gamma')
something = Stationery('Hanna')
pen.draw()
pencil.draw()
handle.draw()
something.draw()