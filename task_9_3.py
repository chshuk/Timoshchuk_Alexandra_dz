class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        pass

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        return sum(self._income.values())


artist = Position("Иван", "Иванов", "художник", 43214.67, 3456)
full_name = artist.get_full_name()
full_income = artist.get_full_income()
print(f'{full_name}: {full_income}')
