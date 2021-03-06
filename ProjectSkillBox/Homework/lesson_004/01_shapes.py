# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# # - треугольника
# length_triangle = 200
# point_triangle = sd.get_point(50, 400)
# angle_traingle = 0
#
# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw()
# triangle(point=point_triangle, angle=angle_traingle, length=length_triangle)
#
#
#
#
# # - квадрата
#
# length_quadro = 170
# point_quadro = sd.get_point(330, 400)
# angle_quadro = 0
#
# def quadro(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
#     v4.draw()
#
# quadro(point=point_quadro, angle=angle_quadro, length=length_quadro)
#
# # - пятиугольника
#
# length_five = 140
# point_five = sd.get_point(90, 100)
# angle_five = 0
#
# def five(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
#     v5.draw()
#
# five(point=point_five, angle=angle_five, length=length_five)
#
# # - шестиугольника
# length_six = 120
# point_six = sd.get_point(380, 100)
# angle_six = 0
#
# def six(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
#     v6.draw()
#
# six(point=point_six, angle=angle_six, length=length_six)

# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны


#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?
# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
#
def draw(point, length, range_cycle, angle_ualue):
    angle = 0
    for cycle in range(range_cycle):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        point = v1.end_point
        angle += angle_ualue
        sd.line(start_point= v1.start_point, end_point= v1.end_point, width=4)
        v1.draw()

# треугольник
length_triangle = 200
point_triangle = sd.get_point(50, 400)
range_triangle = 3
start_point = point_triangle
draw(point=point_triangle, length=length_triangle, range_cycle=range_triangle, angle_ualue=120)

# квадрат
length_square = 170
point_square = sd.get_point(330, 400)
range_square = 4
draw(point=point_square, length=length_square, range_cycle=range_square, angle_ualue=90)

# пятиугольник
length_pentagon = 140
point_pentagon = sd.get_point(90, 100)
range_pentagon = 5
draw(point=point_pentagon, length=length_pentagon, range_cycle= range_pentagon, angle_ualue=72)
# - шестиугольник
length_hexagon = 120
point_six_hexagon = sd.get_point(380, 100)
range_six_hexagon = 6
draw(point=point_six_hexagon, length=length_hexagon, range_cycle= range_six_hexagon, angle_ualue=60)



# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
sd.pause()
