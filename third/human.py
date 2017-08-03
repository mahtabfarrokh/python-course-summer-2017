class Human ():
    count = 0
    countwoman = 0
    countman = 0
    def __init__(self, name, lastname, age, uni, gender ):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.university = uni
        self.gender = gender
        Human.count += 1
        self.gen()
    def gen (self):
        if self.gender == "woman":
            Human.countwoman += 1
        else:
            Human.countman += 1

    def printName (self):
        print(self.name + " " + self.lastname)

