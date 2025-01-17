# problem-1:
print("\nProblem_1:")
country_population={"China":143,"India":136,"USA":32,"Pakistan":21}
user=input("What do you want to do with this dictionary print/add/remove/query: ")
if user=="print":
    for key,value in country_population.items():
        print(key,"==>",value)
elif user=="add":
    country_name=input("Which country do you want to add: ")
    if country_name in country_population:
        print(country_name,"is already exist")
    else:
        population=int(input("What is the population of Country: "))
        country_population[country_name]=population
        for key,value in country_population.items():
            print(key,"==>",value)
elif user=="remove":
    country_name=input("Which country do you want to remove: ")
    if country_name in country_population:
        del country_population[country_name]
        for key,value in country_population.items():
            print(key,"==>",value)
    else:
        print("That country doesn't exist")
elif user=="query":
    country_name=input("which country's population do you want to see? :")
    if country_name in country_population:
        print(country_name,"==>",country_population[country_name])
    else:
        print("country doesn't exist")
 


 # problem-2
print("\nproblem_2 :")
stock_prices={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
user=input("what do you want to do this with this dictionary? :")
if user=="print":
    for i,j in stock_prices.items():
        avg=(j[0]+j[1]+j[2])/3
        print(i,"==>",j,"==>",round(avg,2))
elif user=="add":
    stock_name=input("Enter the stock name :")
    stock_price=int(input("Enter the stock price :"))
    if stock_name in stock_prices:
        stock_prices[stock_name]=stock_price
    else:
        stock_prices[stock_name]=stock_name[stock_price]
    for i,j in stock_prices.items():
        avg=(j[0]+j[1]+j[2]+j[4])/4
        print(i,"==>",j,"==>",round(avg,2))



#  problem-3
from math import pi
print("\nproblem_3 :")
def circle_calc(r):
    # this function calculates  the diameter , circumference and area of the circle
    pi
    d=2*r
    c=2*pi*r
    a=pi*(r**2)
    print("diameter of a circle is",round(d,2),"\ncircumference of a circle is",round(c,2),"\narea of a circle is",round(a,2),)
radius=int(input("Enter the radius of a circle: "))
circle_calc(radius)