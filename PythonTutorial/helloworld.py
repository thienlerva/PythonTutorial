# run script python helloworld.py

x = "Hello World"
print(x)

fruits = []
fruits.append("orange")
print(fruits)

colors = ["yellow", "green", "blue"]
colors.append("gray")
colors.sort()
print(colors)

numList = [50, 100, 65, 82, 23]
numList.sort(reverse = True)
print(numList)

def comparable(n):
	return abs(n - 50)

numList.sort(key = comparable)
print(numList)

sortFruits = ["banana", "Orange", "Kiwi", "cherry"]
sortFruits.sort(key = str.lower)
print(sortFruits)

sortFruits.reverse()
print(sortFruits)

f = open("demofile.txt", "a")
f.write("This is first line")
f.close()

f = open("demofile.txt", "r")
print(f.read())

import pandas as pd 

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)