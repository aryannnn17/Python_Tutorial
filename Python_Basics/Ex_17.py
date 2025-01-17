class Animal():
    def __init__(self,h):
        self.habit=h
    def common(self):
        print("I have 4 legs")
    def name():
        n=input("Give me a name : ")
        print("I love this name", n,"!!!")

class Dog(Animal):
    def __init__(self):
        super().__init__("TOM")
    def name(self):
        print("TOMMY")

t=Dog()
t.name()
t.common()

