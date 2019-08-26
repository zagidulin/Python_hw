# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibo_l = [1, 1]
    i = 0
    while i < n-1:
        fibo_l.append(fibo_l[-2] + fibo_l[-1])
        fibo_l.pop(0)
        i += 1
    while len(fibo_l) < m-n+1:
        fibo_l.append(fibo_l[-2] + fibo_l[-1])
    return fibo_l
print(fibonacci(1, 12))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    i = 0
    while i < len(origin_list):
        temp_list = origin_list[i:]
        x = min(temp_list)
        y = temp_list.index(x)
        origin_list[i], origin_list[y + i] = x, origin_list[i]
        origin_list = origin_list
        i = i + 1
    sorted_list = print(origin_list)
    return sorted_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, a):
    after = []
    for i in a:
        if func(i) == True:
            after.append(i)
    print(after)

my_filter(lambda x: x > 0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def parallelogramm(A1, A2, A3, A4):
    '''Определяет являются ли заданные точками вершинами параллелограмма в т.ч. частных случаев - квадрата, прямоугольника, ромба'''
    lng_A1A2 = math.sqrt((A1[0] - A2[0]) ** 2 + (A1[1] - A2[1]) ** 2)
    lng_A2A3 = math.sqrt((A2[0] - A3[0]) ** 2 + (A2[1] - A3[1]) ** 2)
    lng_A3A4 = math.sqrt((A3[0] - A4[0]) ** 2 + (A3[1] - A4[1]) ** 2)
    lng_A4A1 = math.sqrt((A4[0] - A1[0]) ** 2 + (A4[1] - A1[1]) ** 2)
    if lng_A1A2 == lng_A2A3 and lng_A3A4 == lng_A4A1:
        print("YES!")
    elif lng_A1A2 == lng_A3A4 and lng_A2A3 == lng_A4A1:
        print("YES!")
    elif lng_A1A2 == lng_A4A1 and lng_A2A3 == lng_A3A4:
        print("YES!")
    else:
        print("NO!")
a = [2,3]
b = [5,6]
c = [12,6]
d = [9,2]
parallelogramm(a, b, c, d)
a[1] = 2
parallelogramm(a, b, c, d)