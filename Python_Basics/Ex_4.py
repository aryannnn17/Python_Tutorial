#problem_1
street="parvat patiya"
city="surat"
country="India"
# using + operator
address=street+"\n"+city+"\n"+country
print(address)
# using triple quote
address='''parvat patiya
surat
India'''
print(address)
# using f-string
address=f'{street}\n{city}\n{country}'
print(address)


# problem_2
print("\nProblem-2 :")
str1="Earth revolves around the sun"
print(str1[6:14])
print(str1[-3:])


# problem_3
print("\nProblem-3 :")
fruits=8
vegies=4
str2=f'I eat {str(vegies)} veggies and {str(fruits)} fruits daily'
print(str2)


# problem_4
print("\nProblem-4 :")
s='maine 200 banana khaye'
print(s)
s=s.replace('banana','samosa')
s=s.replace('200','10')
print(s)