import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/dollar_rate_triyears.csv")

x = pd.DataFrame(data, columns=['days'])
y = pd.DataFrame(data, columns=['dollar_rate'])

regression = LinearRegression()
regression.fit(x, y)

plt.scatter(x, y, alpha=0.3)
plt.plot(x, regression.predict(x), color='red', linewidth=2)

plt.title("dollar_rate_prediction")
plt.xlabel("days")
plt.xlim(0, 750)
plt.ylim(5, 25)
plt.ylabel("dollar_rate")

plt.savefig("dollar_rate_prediction.png")
plt.show()
