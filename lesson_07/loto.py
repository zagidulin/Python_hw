import random

class Box:
    def __init__(self):
        self.barrels = [_ for _ in range (1, 91)]

class Card:
    def __init__(self, who):
        self.who = who
        self.card_blank = [['' for _ in range(9)] for _ in range(3)]
        self.card_nums = random.sample(range(1, 91), 15)
    def get_card(self):
        for j in range(3):
            index_ = random.sample(range(8), 5)
            for k in range(5):
                self.card_blank[j][index_[k]] = self.card_nums[0]
                self.card_nums.pop(0)
    def __str__(self):
        print(f'Карточка {self.who+"а"}'.center(25, "-"))
        for j in self.card_blank:
            for k in j:
                print(f'{k}'.rjust(2), end = " ")
            print()
        return "-"*25
    def card_check(self, n):
        for j in range(3):
            if n in self.card_blank[j]:
                self.card_blank[j][self.card_blank[j].index(n)] = "X"
                return True
                break
            else:
                continue
            return False

class Game:
    def __init__(self, **kwargs):
        pass

    def start_game(self):
        box = Box()
        card_p = Card("Игрок")
        card_c = Card("Компьютер")
        card_p.get_card()
        card_c.get_card()

        luck_p = luck_c = 0
        game = 1

        while len(box.barrels) > 0 and game == 1:
            print(card_p)
            print(card_c)
            n = random.choice(box.barrels)
            box.barrels.remove(n)
            print("Номер бочонка: ", n)
            print(len(box.barrels), "- осталось бочонков")
            answer = input("Вычеркнуть номер из карточки Игрока? (y/n)\n")
            while True:
                if answer == "y":
                    if card_p.card_check(n):
                        luck_p += 1
                        break
                    else:
                        print("Такого номера нет в карточке Игрока.\nИгра окончена. Вы проиграли")
                        game = 0
                        break
                elif answer == "n":
                    if card_p.card_check(n):
                        print("Такой номер есть в карточке Игрока.\nИгра окончена. Вы проиграли")
                        game = 0
                        break
                    else:
                        break
                else:
                    answer = input("Введен некорректный ответ.\nВычеркнуть номер из карточки Игрока? (y/n)\n")
                    continue

            if card_c.card_check(n):
                luck_c += 1
            else:
                pass

            if luck_p == 15:
                if luck_c == 15:
                    print("Ничья")
                    game = 0
                else:
                    print(card_p)
                    print("Вы победили!")
                    game = 0
            elif luck_c == 15:
                print(card_c)
                print("Вы проиграли!")
                game = 0
            else:
                continue

play = Game()
play.start_game()