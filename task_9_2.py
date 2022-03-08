class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_weight(self, weight, thickness):
        result = self._length * self._width * weight * thickness
        if result // 1000 > 0 and result % 1000 == 0:
            return f'{result // 1000} т'
        else:
            return f'{result} кг'


road = Road(15, 2000)
asphalt = road.total_weight(15, 3)
print(asphalt)
