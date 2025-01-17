class Adult(Exception):
    def __init__(self,str):
        self.exception=str
    def AdultException(self):
        print("i am in ",self.exception)
try:
    raise Adult("AdultException")
except Exception as e:
    print("Error occured: ",e)

print("\n\n*********Problem_2**********\n")
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Person_age(self):
        print("I'm",self.age,"years old.") 
    def Person_name(self):
        print("Hey! My name is",self.name)
    def get_minor_age(self):
        if self.age>=18:
            try:
                raise Adult("My age is Above 18")
            except Exception as e:
                print("AdultException:",e)
        else:
            return self.age

user_1=Person(input("Enter your name: "),int(input("Enter your age:")))
user_1.Person_name()
user_1.Person_age()
user_1.get_minor_age()