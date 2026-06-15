class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age 

class student(person) :
    def introduce(self):
        print("Hii I am", self.name, "and I am", self.age,"years old")

suraj = student("Suraj",22)

suraj.introduce()