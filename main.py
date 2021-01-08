from list import *
from random import randint

lst = build_list(10, lambda x : randint(1, 10))
sorted_lst = sort(lst, lambda x, y : x < y)

show(lst)
show(sorted_lst)
