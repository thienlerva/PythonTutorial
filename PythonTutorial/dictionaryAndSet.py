# Dictionary is unordered, duplicates not allowed

carDict = {
    "branch": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(carDict)
print(carDict["branch"])
print(len(carDict))
print(type(carDict))

# get value
print(carDict.get("colors"))  # same as carDict["colors"]

# get Keys
print(carDict.keys())

# change value
carDict.update({"year": 2020}) # same as carDict["year"] = 2020

# Adding items
carDict.update({"price": 19000}) # same carDict["price'] = 19000

# Remove items
carDict.pop("model")
print(carDict)

# clear dictionary
#carDict.clear()

# Loop dictionary
for x in carDict:
    print(x)  # print keys

for x in carDict:
    print(carDict[x]) # print values

for x in carDict.values():
    print(x)

for x in carDict.keys():
    print(x)

for x, y in carDict.items():
    print(x, y)


# Set is unordered, unchanged
print("Learn Set")
fruits = {"apple", "banana", "cherry"}
print(fruits)

for x in fruits:
    print(x)

# Add item
fruits.add("orange")

# Remove item
fruits.remove("banana")

# Join set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Union method returns a new set with all items from both sets
set3 = set1.union(set2)
print(set3)

# Update method inserts the items in set2 into set1
# union and update will exclude any duplicate items
set1.update(set2)
print(set1)

# intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# intersection() will return a new set that only contains the items that are present in both sets
z = x.intersection(y)
print(z)

# symmetric_difference_update() will keep only the elements that are NOT present in both sets
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() will return a new set that contains only the elements that are NOT present in both sets
z = x.symmetric_difference(y)
print(z)
