__author__ = 'Загидулин Артур'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.a = point_a
        self.b = point_b
        self.c = point_c
    def square(self):
        return 0.5*abs((self.a[0] - self.c[0])*(self.b[1] - self.c[1]) - (self.b[0] - self.c[0])*(self.a[1] - self.c[1]))
    def height(self):
        height_a = 2*self.square()/(sqrt((self.b[0] - self.c[0])**2 + (self.b[1] - self.c[1])**2))
        height_b = 2*self.square()/(sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2))
        height_c = 2*self.square()/(sqrt((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2))
        return "Высота из точки {0} - {1}\n" \
               "Высота из точки {2} - {3}\n" \
               "Высота из точки {4} - {5}".format(self.a, height_a, self.b, height_b, self.c, height_c)

x = (3, 5)
y = (7, 4)
z = (1, 2)

tr1 = Triangle(x, y, z)
print("Площадь треугольника -", tr1.square())
print(tr1.height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapez:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def test(self):
        ab = sqrt((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2)
        bc = sqrt((self.b[0] - self.c[0])**2 + (self.b[1] - self.c[1])**2)
        cd = sqrt((self.c[0] - self.d[0])**2 + (self.c[1] - self.d[1])**2)
        ad = sqrt((self.a[0] - self.d[0])**2 + (self.a[1] - self.b[1])**2)
        ac = sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2) # диагональ
        bd = sqrt((self.b[0] - self.d[0])**2 + (self.b[1] - self.d[1])**2) # диагональ
        if ab == cd and ad != bc and ac == bd: # проверка равенства сторон и диагоналей и неравенства оснований
            # проверяем, что все точки не принадлежат одной прямой:
            if (self.a[0] != self.b[0] or self.a[0] != self.c[0] or self.a[0] != self.d[0]) and (self.a[1] != self.b[1] or self.a[1] != self.c[1] or self.a[1] != self.d[1]):
                return True
            else:
                return False
        else:
            return False

trapez1 = Trapez((1, 1), (4, 1), (2, 1), (5, 1))
print(trapez1.test())
trapez2 = Trapez((1, 1), (2, 3), (5, 3), (6, 1))
print(trapez2.test())