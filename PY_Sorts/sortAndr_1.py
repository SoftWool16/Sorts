num = int(input())
import random
string = ""      #создание пустого списка
a = list(range(num)) #ввод размера массива
random.shuffle(a)   #перемешивание массива
for b in a:
    string += (" | " + str(b))
print(string)


def ids(n1, n2):
    if n1 > n2:
        s = a.pop(n1)
        a.insert(n2, s)
        print(a)
        string2 = ""
        s = a.pop(n1)
        a.insert(n2, s)
        for b in a:
            string2 += (" | " + str(b))
        print(string2)
    else:
        print("--------код хуйня--------")


def lst(num):
    for n1 in range(num):
        for n2 in range(num):
            n2 += 1
            if n1 > n2:
                ids(n1, n2)


for s in range(num):
    if s <= num:
        lst(num)
    else:
        print("--------конец--------")
