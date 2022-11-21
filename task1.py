# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random
import numpy as np 

print("Таблица оценок по группам:")
a = np.random.randint(2, 6, size = (3, random.randint(20, 30)))
print(a)
b = np.mean(a, axis = 1)
print("Среднее арифметическое оценок каждой группы:")
print(b)
ind = np.argmax(b)
print(f'Строка группы с максимальной средней оценкой - {ind + 1}, лучший средний балл = {b[ind]}')