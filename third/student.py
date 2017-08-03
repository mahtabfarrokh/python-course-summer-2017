from human import *
class Student (Human):
    def __init__(self , mark , name, lastname, age, uni, gender):
        self.__mark = mark
        super().__init__(name = name, age= age , uni=uni, gender=gender, lastname = lastname)

    def getmark (self):
        return  self.__mark

    def setmark (self , mark):
        self.__mark = mark

h = Student(13 , "mahtab" , "farrokh" , 19 , "amirkabir", "woman")
h.printName()
print (h.countwoman)
print (h.countman)
print("mark :" , h.getmark())

