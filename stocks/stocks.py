import pandas as pd
import matplotlib.pyplot as plt

path = "data.csv"
data = pd.read_csv(path, parse_dates=[0])

print data[" Open"].mean()
plt.plot(data["Date"], data[" OI"])
# plt.show()
