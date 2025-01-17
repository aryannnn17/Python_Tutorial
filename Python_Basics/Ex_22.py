integer=[i for i in range(5)]
binary=[format(i,'b') for i in integer]
binary_dict={a:b for a,b in zip(integer,binary)}
print("integer -->",integer,"\nbinary -->",binary,"\nbinary dictionary -->",binary_dict)

print("\nProblem-2 :")
num=[1,4,-6,3,-5,-7,9,7]
num_inverse=[-i for i in num]
print("integer -->",num,"\ninteger inverse -->",num_inverse)

print("\nProblem-3 :")
num2=[1,-1,2,-2,3,-3]
sq_num2={i**2 for i in num2}
print("integer -->",num2,"\nsquare integer set -->",sq_num2)