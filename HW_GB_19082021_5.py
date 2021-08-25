import sys
import itertools
import itertools
system, name, hobby = sys.argv
with open('file_for_5HW.txt', 'w', encoding='utf-8') as f:
    with open(name, 'r', encoding='utf-8') as n:
        with open(hobby, 'r', encoding='utf-8') as h:
            len_n = sum(1 for i in n)
            len_h = sum(1 for i in h)
            if len_n < len_h:
                exit(1)
            n.seek(0)
            h.seek(0)
            for i, j in itertools.zip_longest(n, h, fillvalue= 'None'):
                f.write(f'"{i.strip()} - {j.strip()}" ')

            # опять же проблема с выводом None
