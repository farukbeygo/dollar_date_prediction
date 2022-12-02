
# some initial imports

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler


# importing our data
data = pd.read_csv("dollarRate_dataSet.csv")
print(data)

# draw a graph for data
x = data["days"]
y = data["dollar_rate"]
x = x.reshape(344, 1)
y = y.reshape(344, 1)

plt.scatter(x, y)

linear_prediction = LinearRegression()
linear_prediction.fit(x, y)
linear_prediction.predict(x)

plt.plot(x, linear_prediction.predict(x), c="red")