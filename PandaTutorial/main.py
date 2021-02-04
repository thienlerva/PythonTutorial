
import pandas as pd
df = pd.read_csv("weather_data.csv")
print(df)
print(df.shape)
print(df.head())
print(df.head(2))
print(df.tail())
print(df[2:5])
print(df.columns)
print(df.day)
print(df['event']) # same df.event
print(type(df.event))
print(df[['event', 'day']])

# Max, min
print(df['temperature'].max())
print(df['temperature'].mean())
print(df.describe())  # statistic of info

# Conditional operation
print(df[df.temperature >= 32])
print(df[df.temperature >= df['temperature'].max()])
print(df[['day', 'temperature']][df.temperature >= df['temperature'].max()])

# index
print(df.index)
print(df.set_index('day', inplace = True))
print(df)
print(df.loc['1/1/2017'])