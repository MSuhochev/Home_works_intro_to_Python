# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
# с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# 	Примеры/Тесты:
# 	385916 >>> yes
# 	123456 >>> no

num_ticket = int(input("Введите шестизначный номер Вашего билетика: "))
num_1 = num_ticket // 1000
num_2 = num_ticket % 1000
sum_num_1 = 0
sum_num_2 = 0
while num_1 > 0:
    temp = num_1 % 10
    sum_num_1 = sum_num_1 + temp
    num_1 = num_1 // 10
while num_2 > 0:
    temp = num_2 % 10
    sum_num_2 = sum_num_2 + temp
    num_2 = num_2 // 10
if sum_num_1 == sum_num_2:
    print("YES")
else:
    print("NO")

print()
print("(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор")

num_ticket = int(input("Введите любое шестизначное целочисленое число: "))
num_1 = num_ticket // 1000
num_2 = num_ticket % 1000
sum_num_1 = 0
sum_num_2 = 0
while num_1 > 0:
    temp = num_1 % 10
    sum_num_1 = sum_num_1 + temp
    num_1 = num_1 // 10
while num_2 > 0:
    temp = num_2 % 10
    sum_num_2 = sum_num_2 + temp
    num_2 = num_2 // 10
like = "YES" if sum_num_1 == sum_num_2 else "NO"
print(like)