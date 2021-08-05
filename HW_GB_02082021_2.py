rez_summa_1 = 0
rez_summa_2 = 0
main_list = []
for i in range(1, 1001, 2):
    number = i ** 3
    main_list += [number]
    temporary_summa = 0
    temporary_number = number
    while temporary_number > 0:
        temporary_summa += temporary_number % 10
        temporary_number //= 10
    if temporary_summa % 7 == 0:
        rez_summa_1 += number
for i in range(len(main_list)):
    main_list[i] += 17
    number = main_list[i]
    temporary_summa = 0
    temporary_number = number
    while temporary_number > 0:
        temporary_summa += temporary_number % 10
        temporary_number //= 10
    if temporary_summa % 7 == 0:
        rez_summa_2 += number
print(rez_summa_1)
print(rez_summa_2)

