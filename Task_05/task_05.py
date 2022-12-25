# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

user_number = int(input('Введите число: '))

def postitv_fib(n):
    positiv_list = [0, 1]
    for i in range(n-1):
        positiv_list.append(positiv_list[-2]+positiv_list[-1])
    return positiv_list

def negativ_fib(n):
    negativ_list = [1, 0]
    for i in range(n-1):
        negativ_list.insert(0, negativ_list[1]-negativ_list[0])
    return negativ_list

print(negativ_fib(user_number) + postitv_fib(user_number)[1:])
