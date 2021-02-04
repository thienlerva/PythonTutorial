import pandas as pd

dataset = {
    "car": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

print(pd._version)
myVar = pd.DataFrame(dataset)
print(myVar)