for i in range (1, 101):
    number = i
    digit = i % 10
    if digit == 1 and number != 11:
        print(f'{i} процент')
    elif (5 <= digit <= 9) or (digit == 0) or (number == 11) or (12 <= number <= 14):
        print(f'{i} процентов')
    else:
        print(f'{i} процента')


