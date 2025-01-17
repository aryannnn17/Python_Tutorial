# Problem-1
print("\nProblem-1 :")
month=["January","February","March","April","May"]
expense=[2200,2350,2600,2130,2190]
print(f'In feb, you have spent {expense[1]-expense[0]} extra dollars')
print(f"In first quarter of the year your total expense is {expense[0]+expense[1]+expense[2]}")
print("i've ever spend 2000 dollars?", 2000 in expense)
month.append("June")
expense.append("1980")
print(month,expense)
expense[3]-=200
print(month,expense)


# Problem-2
print("\nProblem-2 :")
heros=["spider man","thor","hulk","iron man","captain america"]
print(len(heros))
heros.append("black Panther")
print(heros)
heros.remove("black Panther")
print(heros)
heros.insert(2,"black Panther")
print(heros)
heros[1:4]=["doctor strange"]
print(heros)
heros.sort()
print(heros)