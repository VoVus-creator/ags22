# -- coding: utf-8 --
from math import prod
 
a = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {a}')
print(f'Сумма элементов списка равна: {sum(a)}')
print(f'Произведение элементов списка: {prod(a)}')