def gen_function(number):
    for i in range(1, number + 1, 2):
        yield i
my_number = gen_function(15)
print(next(my_number)) # считываем элементы по-одному
print(*gen_function(15)) # считали все сразу

