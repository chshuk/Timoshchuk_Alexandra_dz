class Array:
    def __init__(self, array_list):
        self.height = len(array_list)
        self.width = len(array_list[0])
        for el in array_list:
            if len(el) != self.width:
                raise 'Это не матрица'
        self.val = array_list

    def __str__(self):
        max_len = 0
        for elem in self.val:
            for el in elem:
                if len(str(el)) > max_len:
                    max_len = len(str(el))
        string = ""
        for elem in self.val:
            for el in elem:
                string += f"%{-max_len - 2}d" % el
            string += "\n"
        return string

    def __add__(self, other):
        if self.height == other.height and self.width == other.width:
            res = []
            for self_elem, other_elem in zip(self.val, other.val):
                res.append([])
                for sel_el, oth_el in zip(self_elem, other_elem):
                    res[-1].append(sel_el + oth_el)
            return Array(res)
        raise "матрицы должны быть одинакового размера"


a = Array([[1, 2, 3], [3, 4, 5]])
b = Array([[4, 3, 0], [2, 1, 4]])
print(a)
print(b)
c = a + b
print(c)
