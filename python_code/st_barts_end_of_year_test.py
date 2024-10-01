import random as rand
import math 
from datetime import date

a = rand.randint(1,100)
print(a)

b = math.sqrt(4)
print(b)

c = date.today()
print(c)

string = "The date today is \n" + str(c) + " " + "and the random number of the day is " + str(b) 

print(string)


if a <= 2:
    d = 1 + 1 
elif a <= 10:
    d = 10 * 2
elif a <= 30:
    d = 5 / 10
else: 
    d = 7 - 10 

print(d)


list1 = [ 'e', 'f', 'g', 'h']
list2 = [1, 2, 3, 4]
listzip = list(zip(list1, list2))
print(listzip)

list1.pop()
list1.append("i")

print(list1)


def func(arg1, arg2):
    return arg1 * arg2

print(func(2,3))

