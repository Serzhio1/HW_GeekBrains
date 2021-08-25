maks = 0
dictionary = {}
result_list = []
with open('HW_GB_file_19082021_1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        temp_list = line.split()
        temp_tuple = (temp_list[0], temp_list[5].lstrip('"'), temp_list[6])
        result_list.append(temp_tuple)
        if dictionary.get(temp_list[0]) == None:
            dictionary.setdefault(temp_list[0], 1)
        else:
            dictionary[temp_list[0]] += 1
for i in dictionary:
    if dictionary[i] > maks:
        maks = dictionary[i]
        rez_id = i
print(rez_id, maks)
