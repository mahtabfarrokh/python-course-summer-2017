print("Hello World ! :D")
# Hello World ! :D


"""""
this is comment 
python course
"""""


name = "mahtab"
name2 = 'mahtab'

num =  19
num2 = int("19")
num3 = 19.27
num3 = float("19.27")

x = None

num4 = []
num4.append(10)
num4.append(20)
num4.extend([30, 40])
num4.append([50, 60])
print(num4)
print("lenght of list is:" , len(num4))
print(num4[0])
print(num4[1:3])
print(num4[2:])
print(num4[:3])

b = True
b1 = False

arith = 2 / 6
arith1 = 2 ** 3

print(True and 1 and "1")
print(False and 0 and "")

print(3 > 4)
print(4 == 4)
print(3 != 3)

grade = 82
if grade > 80:
    if grade == 90:
        print ("90")
    else:
        print(grade)
elif grade < 90:
    print("here :D ")
else:
    print("bye")

for i in range(10):
    print(x)

fruits = ['Orange' , 'Banana']
for f in fruits:
    print(fruits)

x = 0
while x < 100:
    print(x)
    x += 1

odds = [x for x in range(10) if x % 2]
list2 = [[]for x in range(10)]
list3 = [[[]for x in range(5)]for x in range(2)]
print(list2)
print(list3)

def mysum (a, b):
    return a + b

print(mysum(2,4))

def fib1 (n):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a + b
    return a

def fib2(n):
    if (n == 1 or n == 0):
        return 1
    return fib2(n-1) + fib2(n-2)

print(fib1(3))
print(fib2(3))