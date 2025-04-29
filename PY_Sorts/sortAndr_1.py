num = int(input())
import random
a = list(range(num)) #ввод размера массива
random.shuffle(a)   #перемешивание массива
print(a)
m = 0
while m<(num-1):
    n = m
    while n<num:
        if a[n] < a[m]:
            a[n],a[m] = a[m],a[n]
            n += 1
        else:
            n += 1
    m += 1
print(a)