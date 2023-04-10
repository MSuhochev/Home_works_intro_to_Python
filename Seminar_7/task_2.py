# 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк 
# и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256
#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36
# ```(*)``` **Усложнение.** Сформируйте форматированный вывод с номерами строк и столбцов
# 	Примеры/Тесты:
# 	print_operation_table(lambda x,y: x**y,4,4)
# 	       1   2   3   4
# 	    ----------------
# 	1 |    1   1   1   1
# 	2 |    2   4   8  16
# 	3 |    3   9  27  81
# 	4 |    4  16  64 256
	
# 	print_operation_table(lambda x,y: x*y)
# 	       1   2   3   4   5   6
# 	    ------------------------
# 	1 |    1   2   3   4   5   6
# 	2 |    2   4   6   8  10  12
# 	3 |    3   6   9  12  15  18
# 	4 |    4   8  12  16  20  24
# 	5 |    5  10  15  20  25  30
# 	6 |    6  12  18  24  30  36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row_str = ""
        for j in range(1, num_columns+1):
            element = operation(i, j)
            row_str += f"{element}\t"
        print(row_str)
print_operation_table(lambda x,y: x**y,4,4) 
print("\n\n")
print_operation_table(lambda x,y: x*y)