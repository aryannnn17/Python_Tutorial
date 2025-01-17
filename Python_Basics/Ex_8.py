# Problem 1
print("\nProblem-1(i) :")
india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]
user=input("Enter the city name: ")
if user in india:
    print(user,"city is in india")
elif user in pakistan:
    print(user,"city is in pakistan")
elif user in bangladesh:
    print(user,"city is in bangladesh")
else:
    print("idk",user,"city belongs to which country")

print("\nProblem-1(ii) :")
user1=input("Enter the 1st city name: ")
user2=input("Enter the 2nd city name: ")
if user1 in india and user2 in india:
    print(user1,"and",user2,"both are belong to India")
elif user1 in pakistan and user2 in pakistan:
    print(user1,"and",user2,"both are belong to Pakistan")
elif user1 in bangladesh and user2 in bangladesh:
    print(user1,"and",user2,"both are belong to Bangladesh")
else:
    print(user1,"and",user2,"both are belong to different countries")


# Problem 2
print("\nProblem-2 :")
sugar_level=int(input("Enter your sugar level: "))
if sugar_level<80 :
    print("Your sugar level is low")
elif sugar_level>100:
    print("Your sugar level is high")  
else:
    print("Your sugar level is normal")
    
