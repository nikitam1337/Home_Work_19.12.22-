# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 5, 6]
result = []
count = -1

if len(lst) % 2 != 0:
    for i in range(round((len(lst))/2)+1):
        result.append(lst[i]*lst[count])
        count -= 1
else:
    for i in range(round((len(lst))/2)):
        result.append(lst[i]*lst[count])
        count -= 1
print(result)
