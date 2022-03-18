import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_1950.csv", sep=";")
top_3 = df.nlargest(3, 'ratio')
print(top_3)
top_3 = pd.DataFrame(top_3)
print(top_3)
states = top_3['state'].values
disease = top_3['disease'].values
print(states)
x = np.arange(len(states))
w = 0.3

plt.bar(x-w, top_3['ratio'].values, width=w, label=disease[0])
plt.bar(x,  top_3['ratio'].values, width=w, label=disease[1])
plt.bar(x+w, top_3['ratio'].values, width=w, label=disease[2])

plt.xticks(x, states)

plt.ylabel('Per 100 000 people rate')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.show()



df60 = pd.read_csv("data_1960.csv", sep=";")
top_3 = df60.nlargest(3, 'ratio')
print(top_3)
top_3 = pd.DataFrame(top_3)
print(top_3)
states = top_3['state'].values
disease = top_3['disease'].values
print(states)
x = np.arange(len(states))
w = 0.3

plt.bar(x-w, top_3['ratio'].values, width=w, label=disease[0])
plt.bar(x,  top_3['ratio'].values, width=w, label=disease[1])
plt.bar(x+w, top_3['ratio'].values, width=w, label=disease[2])

plt.xticks(x, states)

plt.ylabel('Per 100 000 people rate')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.show()



df70 = pd.read_csv("data_1970.csv", sep=";")
top_3 = df70.nlargest(3, 'ratio')
print(top_3)
top_3 = pd.DataFrame(top_3)
print(top_3)
states = top_3['state'].values
disease = top_3['disease'].values
print(states)
x = np.arange(len(states))
w = 0.3

plt.bar(x-w, top_3['ratio'].values, width=w, label=disease[0])
plt.bar(x,  top_3['ratio'].values, width=w, label=disease[1])
plt.bar(x+w, top_3['ratio'].values, width=w, label=disease[2])

plt.xticks(x, states)

plt.ylabel('Per 100 000 people rate')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.show()