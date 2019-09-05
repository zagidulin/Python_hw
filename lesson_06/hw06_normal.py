__author__ = 'Загидулин Артур'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, name, patronos):
        self.name = name
        self.surname = surname
        self.patronos = patronos

    def get_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronos

class Pupil(People):
    def __init__(self, surname, name, patronos, father, mother, class_room):
        People.__init__(self, surname, name, patronos)
        self.father = father
        self.mother = mother
        self.class_room = class_room

    def get_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronos[0] + '.'

    def parents(self):
        for _ in pupils:
            if self == _.get_name():
                return f'{_.father.duty}: {_.father.get_name()}\n{_.mother.duty}: {_.mother.get_name()}'

class Parent(People):
    def __init__(self, surname, name, patronos, duty):
        People.__init__(self, surname, name, patronos)
        self.duty = duty

class Teacher(People):
    def __init__(self, surname, name, patronos, subject, class_room):
        People.__init__(self, surname, name, patronos)
        self.subject = subject
        self.class_room = class_room


class_rooms = ['5 А', '7 Б', '8 А']

parents = [Parent('Аркадьев', 'Иван', 'Иванович', 'Отец'),
           Parent('Аркадьева', 'Иона', 'Ивановна', 'Мать'),
           Parent('Борисов', 'Евгений', 'Евгеньевич', 'Отец'),
           Parent('Борисова', 'Евгения', 'Евгеньевна', 'Мать'),
           Parent('Владимирский', 'Дмитрий', 'Дммитриевич', 'Отец'),
           Parent('Владимирская', 'Дарья', 'Дмитриевна', 'Мать'),
           Parent('Пушков', 'Борис', 'Борисович', 'Отец'),
           Parent('Пушкова', 'Ольга', 'Олеговна', 'Мать'),
           Parent('Антонов', 'Алексей', 'Антонович', 'Отец'),
           Parent('Антонова', 'Антонина', 'Антоновна', 'Мать'),
           Parent('Кац', 'Леонид', 'Александрович', 'Отец'),
           Parent('Непонящая', 'Оксана', 'Дмитриевна', 'Мать')]

pupils = [Pupil('Аркадьев', 'Максим', 'Иванович', parents[0], parents[1], class_rooms[0]),
            Pupil('Борисов', 'Павел', 'Евгеньевич',parents[2], parents[3], class_rooms[0]),
            Pupil('Владимирская', 'Анастасия', 'Дмитриевна', parents[4], parents[5], class_rooms[1]),
            Pupil('Пушков', 'Денис', 'Борисович', parents[6], parents[7], class_rooms[1]),
            Pupil('Антонова', 'Алена', 'Алексеевна', parents[8], parents[9], class_rooms[2]),
            Pupil('Кац', 'София', 'Леонидовна', parents[10], parents[11], class_rooms[2]),]

teachers = [Teacher('Никонов', 'Максим', 'Сергеевич', 'Математика', class_rooms),
            Teacher('Титова', 'Елена', 'Александровна', 'Биология', [class_rooms[0], class_rooms[2]]),
            Teacher('Парфенов', 'Федор', 'Матвеевич', 'Физика', [class_rooms[1], class_rooms[2]])]

# список классов
def class_lst():
    print('Список классов:')
    for _ in class_rooms:
        print(_)

# список учеников в классе
def class_pupils(class_r):
    if class_r in class_rooms:
        for _ in pupils:
            if _.class_room == class_r:
                return _.get_name()

# список предметов ученика
def subjects(pupil):
    for p in pupils:
        if pupil == p.get_name():
            for t in teachers:
                if p.class_room in t.class_room:
                    return t.subject

# родители ученика
def parents(pupil):
    for _ in pupils:
        if pupil == _.get_name():
            return f'{_.father.duty}: {_.father.get_name()}\n{_.mother.duty}: {_.mother.get_name()}'

# Учителя класса
def teacher(class_r):
    for _ in teachers:
        if class_r in _.class_room:
           return _.get_name()

