# To import a module
# pip install pandas
# pip list
# conda list

import math
import json
import datetime
import calendar

person = '{"name": "John", "age": 30}'
y = json.loads(person)
print(y["age"])

#Basic python
x = 5
print(x)

#Casting
y = float(x)
print(y)
print(float("3"))
print(str(3.25))

#Get the Type
str = "John"
print(type(str))

"""python number: 
int, float, complex
"""

a = "Hello World"  # Strings are Array
print(a)
print(len(a))
print(a[0])
for x in a:
    print(x)

#check string
txt = "The best things in life are free!"
if "free" in txt:
    print('Yes, \'free\' is present.')

print('expensive' not in txt)
print(txt[:5])  # slicing from the start
print(txt[2:]) # slice to the end
print(txt[1:5]) # Get characters from position 2 to 5 (exclusive)

# Modify String
print(a.upper())
print(a.lower())
print(a.strip()) # Remove any whitespace from the beginning or the end
print(a.replace("H", "J"))
print(a.split(",")) # return ['Hello', ' World']

# "My name is John, i am " + age, not working have to use format()
age = 36
intro = "My name is John, and I am {}"
print(intro.format(age))
print("My name is John, and i am ", age)

# the format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, itemno, price))

secondOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(secondOrder.format(quantity, itemno, price))

# escape character \
print("We are the so-called \"Vikings\" from the north. \nThank you")

x = 200
print(isinstance(x, int))

# list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "strawberry"
fruits.append("banana")
print(fruits)
fruits.insert(1, "orange")
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)

# remove item
fruits.remove("banana")
fruits.pop(1)
fruits.pop()  # remove last item
print(fruits)
tropical.clear()
print(tropical)

# loop list
for x in fruits:
    print(x)

# use range and len
for i in range(len(fruits)):
    print(fruits[i])

# sort list
nums = [100, 20, 50, 30, 90, 10]
nums.sort()
print(nums)

nums.sort(reverse=True)  # sort descending
print(nums)

nums.reverse() # reverse order
print(nums)

drivingAge = 18
if age >= drivingAge:
    print("You are legal to drive")
elif age < drivingAge:
    print("It's illegal to drive")
else:
    print("Something is wrong")

# while loop
i = 1
while i < 6:
    print(i)
    i += 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# loop
for x in fruits:
    if x == "cherry":
        break
    print(x)

for x in range(len(fruits)):
    print(fruits[x])
else:
    print("Finally finished")

x = math.sqrt(64)
print(x)
print(math.pi)

print(min(3,1,9))
print(max(3,5,9,1))

x = datetime.datetime.now()
print(x)

cal = calendar.month(2016, 1)
print(cal)
print(calendar.isleap(2020))