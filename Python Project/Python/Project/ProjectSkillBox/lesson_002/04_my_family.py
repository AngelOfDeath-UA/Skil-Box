#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа', 'Мама', 'Брат']


# список списков приблизителного роста членов вашей семьи
father = [[my_family[0],195]]
mother = [[my_family[1],165]]
brother = [[my_family[2],187]]

my_family_height = father[0][1] + mother[0][1] + brother[0][1]

#print(int(my_family_height))
print('Рост отца - ' + str(father[0][1]) + ' см')
print('Общий рост моей семьи - ' + str(my_family_height) + ' см')


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см