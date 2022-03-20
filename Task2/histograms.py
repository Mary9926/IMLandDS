import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataToHistogram.csv", sep=";")
#df.hist(bins=20)

df.plot(x='year', y='ratio', kind='hist', legend=False)

plt.xlabel("Year")
plt.ylabel("Cases per 100,000");
plt.title("Meales Cases Across States")
plt.show()