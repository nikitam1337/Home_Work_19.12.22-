# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

start_lst = [1.1, 1.2, 3.1, 5, 10.01]
next_list = []

for i in start_lst:
    next_list.append(round(i % 1, 3))
print(next_list)

max = next_list[0]
min = next_list[0]

for i in next_list:
    if i != 0 and i > max:
        max = i
    if i != 0 and i < min:
        min = i

print(max - min)
