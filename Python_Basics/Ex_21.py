def square_generator(number):
    for n in number:
        yield n*n
        n+=1
        
arr=[1,2,3,6,7]
square_number=[]
for i in square_generator(arr):
    square_number.append(i)
print(square_number)

