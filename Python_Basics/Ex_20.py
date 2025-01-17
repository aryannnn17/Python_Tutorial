def square_sequence():
    i=1
    while(1):
        yield i*i
        i+=1
    
for i in square_sequence():
    if i>100:
        break
    print(i)