s = "Here I AM"
print(s.islower())
print(s.isalpha())
print(s.isalnum())
print(s.upper())
print(s.lower())
print(s.find('e'))
print(s.find('e' , 2))
print(s.find('e', 4))


for i in range(10):
    if i== 4 :
        continue
    if i == 7 :
        break
    print(i)

name = input("Enter your name:")
print('hello' , name)

s1 = set ([1,2 ,3])
s2 = {4,5,3}
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))


Dict = {"name": "zahra", "Age": 19, "class": "python"}
print(Dict["name"])
# zahra
print(Dict["Age"])
# 19


dict = {'Name': 'Zahra', 'Age': 19, 'Class': 'python'}
dict['Age'] = 20         # update existing entry
dict['University'] = "Amirkabir"     # Add new entry

print (dict['Age'])
# 20
print (dict['University'])
# Amirkabir


dict = {'Name': 'Zahra', 'Age': 19, 'Class': 'python'}
del dict['Name']    # remove entry with key 'Name'
dict.clear()        # remove all entries in dict
del dict            # delete entire dictionary

print("dict['Age']: ", dict['Age'])
# error
print("dict['School']: ", dict['School'])
# error

l = [1, 2, 3, 4, None]
print(l is None)
# False
print(l[0] is None)
# False
print(l[4] is None)
# True
print(1 in l)
# True
print(None in l)
# True

l1 = None
l2 = []
l3 = [None]
print(l1 is None)
# True
print(l2 is None)
# False
print(l3 is None)
# False
print(l3[0] is None)
# True



print(all([1, 0.1, True, "foo", [None]]))
# True
print(all([1, 0, True, "", [None]]))
# False
print(all([1, 0, True, "False", []]))
# False
print(any([0, False, "", []]))
# False
print(any([0, False, "", [None]]))
# True
print(any([0, False, "False", []]))
# True


f = open("test.txt", "wb")
print("Name of the file: ", f.name)
print("Closed or not : ", f.closed)
print("Opening mode : ", f.mode)
f.close()




file = open('foo.txt')
print(file)
print(file.read())


file.seek(0)
print(file.read())
#   First line.
#   This is the last line.
file.seek(1)
print(file.readline())
#   irst line.

print(file.readline())
#   This is the last line.


# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
l = list(enumerate(seasons))
print(l)
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
l =list(enumerate(seasons, start=1))
print(l)
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]




a = complex(1, 2)
b = complex(1, 2) + complex(3, 4)
c = complex(1, 2) + 2
print(a)
#   (1+2j)
print(b)
#   (4+6j)
print(c)
#   (3+2j)


