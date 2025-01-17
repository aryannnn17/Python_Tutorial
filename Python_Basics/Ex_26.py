import time
import threading

def calculate_area(l,w):
    for i in range(0,len(l)):
        print("\nArea of a",str(i+1),"th Square is",str(l[i]*w[i]))
        time.sleep(1)

def calculate_peripheral(l,w):
    for i in range(0,len(l)):
        print("\nPeripheral of a",str(i+1),"th Square is",str(2*(l[i]+w[i])))
        time.sleep(1)

length=[2,6,4,6]
width=[7,3,5,6]
start_time=time.time()

t1=threading.Thread(target=calculate_area,args=(length,width,))
t2=threading.Thread(target=calculate_peripheral,args=(length,width,))

t1.start()
t2.start()

t1.join()
t2.join()
# for i in range(0,len(length)):
#     print("Area of a",i+1,"Square is",calculate_area(length[i],width[i]))
#     time.sleep(1)
# for i in range(0,len(length)):
#     print("Peripheral of a",i+1,"Square is",calculate_peripheral(length[i],width[i]))
#     time.sleep(1)
finish_time=time.time()
print("Program took",(finish_time-start_time),"seconds")