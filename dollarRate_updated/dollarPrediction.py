
# some initial imports

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler


# importing our data
data = pd.read_excel("datasetDollar.xlsx")
print(data)

# draw a graph for data
x = data["days"]
y = data["dollar_rate"]
y.data["dollar_rate"].apply(lambda x: float(x.split()[0]))

# data manupulation
scaler_x = StandardScaler()
scaler_x.fit_transform(x.values[Ellipsis, None])
scaler_y = StandardScaler()
scaler_y.fit_transform(y.values[Ellipsis, None])

scaler_x = scaler_x.reshape(2291, 1)
scaler_y = scaler_y.reshape(2291, 1)


plt.scatter(x, y)

linear_prediction = LinearRegression()
linear_prediction.fit(x, y)
linear_prediction.predict(x)

plt.plot(x, linear_prediction.predict(x), c="red")