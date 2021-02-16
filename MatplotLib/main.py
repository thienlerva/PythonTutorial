import matplotlib.pyplot as plt
import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('iphone_price.csv')
# plt.scatter(data['version'], data['price'])
# plt.show()

# Pie charts
#y = np.array([35, 25, 25, 15])
y = [35, 25, 25, 15]
label = ["Apples", "Bananas", "Cherries", "Dates"]
myExplode = [0.2, 0, 0, 0]

plt.pie(y, labels = label, autopct='%1.1f%%', explode=myExplode, shadow=True)
plt.axis('equal')  # Ensure pie is drawn as a circle
plt.show()

# model = LinearRegression()
# model.fit(data[['version']], data[['price']])
# print(model.predict([[12]]))
# print(model.predict([[30]]))

