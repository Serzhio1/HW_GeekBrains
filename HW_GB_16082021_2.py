# решение №1
def gen_function(number):
    result_1 = (i for i in range(1, number + 1, 2))
    return result_1
print(*gen_function(15))

# решение №2
my_number = int(input('Введите число: '))
result_2 = (i for i in range(1, my_number + 1, 2))
print(*result_2)

