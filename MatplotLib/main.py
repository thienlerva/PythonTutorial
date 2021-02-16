import matplotlib.pyplot as plt
import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('iphone_price.csv')
# plt.scatter(data['version'], data['price'])
plt.show()
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[12]]))
print(model.predict([[30]]))

