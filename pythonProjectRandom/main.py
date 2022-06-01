from random import randint

import random
def random_list():
    s = [randint(a, b) for i in range(c)]
    print(s)

a = int(input("start the list: "))
b = int(input("finish the list: "))
c = int(input("number of items: "))

random_list()