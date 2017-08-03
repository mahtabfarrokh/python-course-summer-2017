x = 2
y = "hey"
def div (a , b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("zero eroor")
    except TypeError:
        print("type erorr")
    else:
        print("it's Ok")



def getName():
    age = input("Enter your age")
    try:
        print("salam")
        print("your  age: " , int(age))
    except ValueError :
        print("wrong age")
        getName()
    else :
        print("Done")

getName()


def my_age():
    age = input("Enter your age")
    age = int(age)
    if age < 0:
        raise ValueError
    print("your  age: ", int(age))
    print("Done")


while True:
    try:
        my_age()
        break
    except ValueError:
        print("wrong Answer")



def my_age2(x) :
    if x<0 or x>120 :
        raise ValueError
    print(x)
try :
    my_age2(45)
except ValueError:
    print("age is not valid")