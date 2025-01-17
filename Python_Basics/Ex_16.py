# problem-1
print("\nProblem_1:")

class employee:
    def __init__(self,i,n):
        self.id=i
        self.name=n
    def Id(self):
        print("ID : ",self.id)
    def Name(self):
        print("Name : ",self.name)

emp=employee(1,"Aryan")
emp.Id()
emp.Name()
print('')
emp=employee(2,"Coder")
emp.Id()
emp.Name()
