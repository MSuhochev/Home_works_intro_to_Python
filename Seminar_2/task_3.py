# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
#  	Примеры/Тесты:
#     10 ->
#     1
#     2
#     4
#     8
# ```(*)``` **Усложнение.** Вывод оформить в одну строку: числа выводить через запятую. 
#           Для этого воспользоваться параметрами функции print
#     Примеры/Тесты:
#     10     -> 1,2,4,8,
#     10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,

num = int(input("Введите натуральное число: "))
tmp = 0
for i in range(num):
    if i % 2 == 0:
        i = 2 ** tmp
        tmp += 1
        if i > num:
            break
        print(i, end=",")
