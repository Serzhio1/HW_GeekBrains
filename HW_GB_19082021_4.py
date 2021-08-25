from itertools import zip_longest
with open('file_for_4HW.txt', 'w', encoding='utf-8') as f:
    with open('HW_GB_file_19082021_3_name.txt', 'r', encoding='utf-8') as n:
        with open('HW_GB_file_19082021_3_hobby.txt', 'r', encoding='utf-8') as h:
            len_n = sum(1 for i in n)
            len_h = sum(1 for i in h)
            if len_n < len_h:
                exit(1)
            n.seek(0)
            h.seek(0)
            for i, j in zip_longest(n, h, fillvalue= 'None'):
                f.write(f'"{i.strip()} - {j.strip()}" ')

            # не понимаю, почему не печатается дефолтное знач




