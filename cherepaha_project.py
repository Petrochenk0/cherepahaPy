import turtle
import random

turtle.begin_fill() # КОМАНДА КОТОРАЯ ПИШЕТЬСЯ В НАЧАЛЕ КОДА ЧТОБЫ ФИГУРА БЫЛА АВТОМАТИЧЕСКИ ЗАПОЛНЕНА
turtle.color("green", "red") # В ДАННОМ СЛУЧАЕ КРАСНАЯ ЧЕРЕПАХА БУДЕТ ОБВОДИТЬ ЗЕЛЁННЫМ ЦВЕТОМ

turtle.shape("turtle") # ИЗМЕНЯЕТ ВНЕШНИЙ ВИД ПЕРА ПРЕВРАЩАЯ ЕЁ В ЧЕРЕПАХУ
zvet_fona_dla_cherepahi_v_python = turtle.Screen() # ФУНКЦИЯ С ПОМОЩЬЮ КОТОРОЙ  МЫ МОЖЕМ ЗАДАТЬ ЦВЕТ ОКНУ
zvet_fona_dla_cherepahi_v_python.bgcolor("yellow") # ДАЁМ ЦВЕТ НАШЕМУ ФОНУ

turtle.pensize(4) # РАЗМЕР ВЫДЕЛЕНИЯ ПЕРА
turtle.pendown() # ПОЗВОЛЯЕТ ВКЛЮЧИТЬ ПЕРО НО ПО УМОЛЧАНИЮ ЭТО ПЕРО ВКЛЮЧЕНО

#turtle.penup() # ОСТАВЛЯЕТ ЗА ЧЕРЕПАХОЙ НЕВИДИМЫЙ СЛЕД

for i in range(0, 10): # ЦИКЛ 
    turtle.right(36) 
    for i in range(0, 5): # ЦИКЛ В ЦИКЛЕ ПОЗВОЛЯЮЩИЙ РИСОВАТЬ ЧЕРЕПАХУ
        turtle.forward(50)
        turtle.right(72)

turtle.end_fill() # ЗАПОЛНЯЕТ ФИГУРУ ЦВЕТОМ
#turtle.pendown() # ВКЛЮЧАЕТ ПЕРО ЧТОБЫ ОСТАВАЛСЯ СЛЕД ТАК ЧТО В ЭТОМ КОДЕ ОН НЕ СИЛЬНО ТО И НУЖЕН
turtle.color("red", "red") # В ЭТОМ СЛУЧАЕ БУДУТ ОБВОДИТЬСЯ КРАСНЫЕ КРАЯ С ЗАПОЛНЯТЬСЯ КРАСНЫМ ЦВЕТОМ
turtle.begin_fill()
for i in range(0, 4):  # ВИДИМО МОЖНО РИСОВАТЬ 2 ФИГУРЫ НО ОНИ БУДУТ НАКЛАДЫВАТЬСЯ
    turtle.forward(100) # ДРУГ НА ДРУГА
    turtle.right(90)
turtle.end_fill()

#turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0, 3):
    turtle.forward(180)
    turtle.right(120)
#turtle.penup() # ОТКЛЮЧАЕТ ПЕРО НО В ЭТОМ КОДЕ ОН НЕ СИЛЬНО ТО И НУЖЕН
turtle.end_fill() # НУЖЕН ДЛЯ ЗАПОЛНЕНИЯ ФИГУРЫ


lines =  random.randint(5, 20) # РАНДОМНЫЕ ЛИНИИ
turtle.color("black", "red") # ЗАДАЁМ ЦВЕТ
turtle.begin_fill() # НАЧАЛО
for randomnih_linii in range(0, lines): # СОЗДАЁМ ЦИКЛ ДЛЯ РАНДОМНЫХ ЛИИИЙ
    dlinna_peremeshenia = random.randint(25, 100) # РАНДОМНЫЙ forward
    naskolko_budet_paviornut_v_pravo = random.randint(1, 500) # РАНДОМНЫЙ right
    turtle.forward(dlinna_peremeshenia) # ЗАДАЁМ РАНДОМНЫЕ ЗНАЧЕНИЕ ДЛЯ forward
    turtle.right(naskolko_budet_paviornut_v_pravo) # ЗАДАЁМ РАНДОМНЫЕ ЗНАЧЕНИЕ ДЛЯ right
turtle.end_fill() # КОНЕЦ
turtle.done() # ПОЗВОЛЯЕТ НЕ ЗАКРЫВАТЬ ОКНО ПОСЛЕ ЗАВЕРШЕНИЯ РИСУНКА
#turtle.exitonClick()