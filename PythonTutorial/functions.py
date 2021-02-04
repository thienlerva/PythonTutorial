
def helloFunction():
    print("Hello from my function")

helloFunction()

def concatString(fname):
    print(fname + " Refsnes")

concatString("Emil")
concatString("Tobias")
concatString("Linus")

# *arg
def numOfKids(*kids):
    print("The youngest child is " + kids[2])

numOfKids("Emil", "Tobias", "Linus")

# default parameter value
def yourContry(country = "USA"):
    print("I am from " + country)

yourContry("Sweden")
yourContry("Vietname")
yourContry()
yourContry("Brazil")

def printFruits(fruits):
    for x in fruits:
        print(x)

fruits = ["apple", "banana", "cherry"]
printFruits(fruits)

def addition(a, b):
    return a + b

n = addition(4,5)
print("Total: ", n)

def getUserName():
    username = input("Enter your name: ")
    print("Username is " + username)

getUserName()