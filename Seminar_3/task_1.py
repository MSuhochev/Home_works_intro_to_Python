# 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
# 	Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2

#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.


num = int(input("Введите число: "))
list = [1, 2, 5, 4, 5, 4, 3, 4, 5, 6]
count = 0
for idx in list:
    if num == idx:
        count += 1
print(count) if count !=0 else print(-1)


# for i in list:
#     if num == i:
#         count += 1
# if count == 0:
#     print(-1)
# else:
#     print(count)
