# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
# int() тоже под встроенными понимается в условии? На всякий случай не использовал
    temp_1 = number*10**ndigits//1
    temp_2 = number*10**ndigits%1
    if temp_2 >= 0.5:
        return (temp_1 + 1)/(10**ndigits)
    else:
        return (temp_1) / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(712.9999967, -1))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return 'Проверьте правильность введенного номера!'
    x = int(ticket_number/1000)
    y = ticket_number - x*1000
    lst_f = [int(i) for i in list(str(x))]
    lst_s = [int(i) for i in list(str(y))]
    return sum(lst_f) == sum(lst_s)

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(217911))