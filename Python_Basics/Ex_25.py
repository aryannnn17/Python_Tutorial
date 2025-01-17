def check(f):
    def factorial_check(x):
        if type(x)==int and x>0:
            return f(x)
        else:
            raise Exception("This number is not non negative integer")
    return factorial_check

@check
def calculate_factorial(n):
    if n==1:
        return 1
    else:
        return n*calculate_factorial(n-1)


for i in range(1,11):
    print("factorial of",i,"is",calculate_factorial(i))

i=1.345
try:
    print("factorial of",i,"is",calculate_factorial(i))
except Exception as e:
    e.print_Exception()

i=-4
try:
    print("factorial of",i,"is",calculate_factorial(i))
except Exception as e:
    e.print_Exception()
