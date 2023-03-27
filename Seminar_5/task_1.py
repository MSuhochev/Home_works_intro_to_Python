#  5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
#     Примеры/Тесты:
#     <function_name>(2,0) -> 1    <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8    <function_name>(2,4) -> 16

def exponentiation(a, b):
    if b == 0: return 1
    if b == 1: return a
    if b != 1: return (a * exponentiation(a, b - 1))
first_num = int(input("Введите число: "))
second_num = int(input("В какую степень вы хотите возвести введённое число?: "))
print(exponentiation(first_num, second_num))