# problem_1
print("\nProblem-1 : ")
result=["heads","tails","tals","heads","tails","heads","heads","tails","tails","tails"]
count=0
for items in result:
    if items=="heads":
        count+=1
print("we got",count,"times heads on coin")        


# problem_2
print("\nProblem-2 : ")
for i in range(1,11):
    if i%2==1:
        print(i**2)


# problem_3
print("\nProblem-3 : ")
month=["january","february","march","april","may"]
expense=[2340,2500,2100,3100,2980]
a=int(input("Enter the expense : "))
for i in range(0,5):
    if a==expense[i]:
        print(expense[i],"expense ammount occured in",month[i])


# problem_4
print("\nProblem-4 : ")
for i in range(1,6):
    q=input("Are you tired? : ")
    if q=="yes":
        print("you ran",i,"km, you didn't finish the race!")
        break;
    elif i==5:
        print("you ran 5 km, Congratulations!")
        break;
    elif q=="no":
        print("you've covered",i,"km, Keep going!")
        continue;


# problem_5
print("\nProblem-5 : ")
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print("")