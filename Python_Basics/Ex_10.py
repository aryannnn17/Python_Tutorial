# problem-1:
print("\nProblem_1 : ")
def calculate_area(B,H):
    area=0.5*B*H
    return area

base=int(input("Enter the base of Triangle : "))
height=int(input("Enter the height of Triangle : "))
area=calculate_area(base,height)
print("The area of the triangle is :",area)


# problem-2:
print("\nProblem_2 : ")
def calculate_area(B,H,S):
    area=0
    if S=="triangle":
        area=0.5*B*H
        return area
    elif S=="rectangle":
        area=B*H
        return area

shape=input("Enter the shape of the body : ")
base=int(input("Enter the base of body : "))
height=int(input("Enter the height of body : "))
area=calculate_area(base,height,shape)
print("The area of the",shape,"is :",area)


# problem-3:
print("\nProblem_3 : ")
def print_pattern(n):
    for i in range(0,n):
        for j in range (0,i+1):
            print("*",end="")
        print("")

num=int(input("Enter the number : "))
print_pattern(num)