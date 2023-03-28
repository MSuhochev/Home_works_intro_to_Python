# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#          Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
#     Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3

def sumnum(num1, num2):
    if num2 == 0: return num1
    return sumnum(num1 + 1, num2 - 1)
first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
print(f"Сумма чисел {first_num} и {second_num} будет равна: {sumnum(first_num, second_num)}")