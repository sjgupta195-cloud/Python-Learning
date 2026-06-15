class student :

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("Hii I am ",self.name)

suraj = student("suraj")
amit = student("amit")

amit.introduce()