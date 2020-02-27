# task 1
'''#inp = int(input("Введите число :"))
def func(inp : int):
    if 9 < inp % 100 < 20 or inp % 10 == 0 or 4 < inp % 10 < 10:
        return str(inp ) +" рублей "
    if 1 < inp % 10 < 5:
        return str(inp) + " рубля "
    if inp % 10 == 1:
        return str(inp ) +" рубль "

print(func(inp))'''


#task2
'''#inp = int(input("Введите число :"))
def func(inp: int):
    if 9 < inp % 100 < 20 or inp % 10 == 0 or 4 < inp % 10 < 10:
        return str(inp) + " копеек "
    elif inp % 10 == 1:
        return str(inp) + " копейка "
    elif 1 < inp % 10 < 5:
        return str(inp) + " копейки "
print(func(inp))'''


#task3
'''#inp = int(input("Введите число :"))

def func(inp: int):
    finally_word = ""
    first_digit = inp % 10
    second_digit = (inp // 10) % 10
    third_digit = (inp // 100) % 10
    if third_digit != 0:
        if third_digit == 1:
            finally_word += "сто "
        elif third_digit == 2:
            finally_word += "двести "
        elif third_digit == 3:
            finally_word += "триста "
        elif third_digit == 4:
            finally_word += "четыреста "
        elif third_digit == 5:
            finally_word += "пятьсот "
        elif third_digit == 6:
            finally_word += "шестьсот "
        elif third_digit == 7:
            finally_word += "семьсот "
        elif third_digit == 8:
            finally_word += "восемьсот "
        elif third_digit == 9:
            finally_word += "девятьсот "

    if second_digit == 1:
        if first_digit == 0:
            finally_word += "десять "
            return finally_word
        elif first_digit == 1:
            finally_word += "одинадцать "
            return finally_word
        elif first_digit == 2:
            finally_word += "двенадцть "
            return finally_word
        elif first_digit == 3:
            finally_word += "тринадцать "
            return finally_word
        elif first_digit == 4:
            finally_word += "четырнадцать "
            return finally_word
        elif first_digit == 5:
            finally_word += "пятнадцать "
            return finally_word
        elif first_digit == 6:
            finally_word += "шестнадцать "
            return finally_word
        elif first_digit == 7:
            finally_word += "семнадцать "
            return finally_word
        elif first_digit == 8:
            finally_word += "восемнадцать "
            return finally_word
        elif first_digit == 9:
            finally_word += "девятнадцать "
            return finally_word
    elif second_digit == 2:
        finally_word += "двадцать "
    elif second_digit == 3:
        finally_word += "тридцать "
    elif second_digit == 4:
        finally_word += "сорок "
    elif second_digit == 5:
        finally_word += "пятьдесят "
    elif second_digit == 6:
        finally_word += "шестьдесят "
    elif second_digit == 7:
        finally_word += "семьдесят "
    elif second_digit == 8:
        finally_word += "восемьдесят "
    elif second_digit == 9:
        finally_word += "девяноста "

    if first_digit == 1:
        finally_word += "один "
    elif first_digit == 2:
        finally_word += "два "
    elif first_digit == 3:
        finally_word += "три "
    elif first_digit == 4:
        finally_word += "четыре "
    elif first_digit == 5:
        finally_word += "пять "
    elif first_digit == 6:
        finally_word += "шесть "
    elif first_digit == 7:
        finally_word += "семь "
    elif first_digit == 8:
        finally_word += "восемь "
    elif first_digit == 9:
        finally_word += "девять "
    elif first_digit == 0 and second_digit == 0 and third_digit == 0:
        finally_word += "ноль "
    return finally_word
print(func(inp))'''


#task4

'''#inp = int(input("Введите число :"))

def func(inp: int):
    finally_word = ""
    first_digit = inp % 10
    second_digit = (inp // 10) % 10
    third_digit = (inp // 100) % 10
    if third_digit != 0:
        if third_digit == 1:
            finally_word += "сто "
        elif third_digit == 2:
            finally_word += "двести "
        elif third_digit == 3:
            finally_word += "триста "
        elif third_digit == 4:
            finally_word += "четыреста "
        elif third_digit == 5:
            finally_word += "пятьсот "
        elif third_digit == 6:
            finally_word += "шестьсот "
        elif third_digit == 7:
            finally_word += "семьсот "
        elif third_digit == 8:
            finally_word += "восемьсот "
        elif third_digit == 9:
            finally_word += "девятьсот "

    if second_digit == 1:
        if first_digit == 0:
            finally_word += "десять "
            return finally_word
        elif first_digit == 1:
            finally_word += "одинадцать "
            return finally_word
        elif first_digit == 2:
            finally_word += "двенадцть "
            return finally_word
        elif first_digit == 3:
            finally_word += "тринадцать "
            return finally_word
        elif first_digit == 4:
            finally_word += "четырнадцать "
            return finally_word
        elif first_digit == 5:
            finally_word += "пятнадцать "
            return finally_word
        elif first_digit == 6:
            finally_word += "шестнадцать "
            return finally_word
        elif first_digit == 7:
            finally_word += "семнадцать "
            return finally_word
        elif first_digit == 8:
            finally_word += "восемнадцать "
            return finally_word
        elif first_digit == 9:
            finally_word += "девятнадцать "
            return finally_word
    elif second_digit == 2:
        finally_word += "двадцать "
    elif second_digit == 3:
        finally_word += "тридцать "
    elif second_digit == 4:
        finally_word += "сорок "
    elif second_digit == 5:
        finally_word += "пятьдесят "
    elif second_digit == 6:
        finally_word += "шестьдесят "
    elif second_digit == 7:
        finally_word += "семьдесят "
    elif second_digit == 8:
        finally_word += "восемьдесят "
    elif second_digit == 9:
        finally_word += "девяноста "

    if first_digit == 1:
        finally_word += "одна "
    elif first_digit == 2:
        finally_word += "две "
    elif first_digit == 3:
        finally_word += "три "
    elif first_digit == 4:
        finally_word += "четыре "
    elif first_digit == 5:
        finally_word += "пять "
    elif first_digit == 6:
        finally_word += "шесть "
    elif first_digit == 7:
        finally_word += "семь "
    elif first_digit == 8:
        finally_word += "восемь "
    elif first_digit == 9:
        finally_word += "девять "
    elif first_digit == 0 and second_digit == 0 and third_digit == 0:
        finally_word += "ноль "
    return finally_word
print(func(inp))'''


#task5

import math
inp = float(input("Введите число :"))
def func1(inp):
    if 9 < inp % 100 < 20 or inp % 10 == 0 or 4 < inp % 10 < 10:
        return str(inp ) +" рублей "
    if 1 < inp % 10 < 5:
        return str(inp) + " рубля "
    if inp % 10 == 1:
        return str(inp ) +" рубль"
def func2(inp):
    if 9 < inp % 100 < 20 or inp % 10 == 0 or 4 < inp % 10 < 10:
        return str(inp) + " копеек "
    elif inp % 10 == 1:
        return str(inp) + " копейка "
    elif 1 < inp % 10 < 5:
        return str(inp) + " копейки "

def FUNC(inp: float):
    finally_word = ""
    ruble = int(math.modf(inp)[1])
    cent = int(round(inp - ruble, 2) * 100)
    finally_word += func1(ruble)
    finally_word += func2(cent)
    return finally_word

print(FUNC(inp))