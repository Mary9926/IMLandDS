from traceback import print_tb
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('yob2009.txt', header=None, names=['name','sex','count'])
df2 = pd.read_csv('yob2010.txt', header=None, names=['name','sex','count'])
df3 = pd.read_csv('yob2011.txt', header=None, names=['name','sex','count'])
df4 = pd.read_csv('yob2012.txt', header=None, names=['name','sex','count'])
df5 = pd.read_csv('yob2013.txt', header=None, names=['name','sex','count'])
df6 = pd.read_csv('yob2014.txt', header=None, names=['name','sex','count'])
df7 = pd.read_csv('yob2015.txt', header=None, names=['name','sex','count'])
df8 = pd.read_csv('yob2016.txt', header=None, names=['name','sex','count'])
df9 = pd.read_csv('yob2017.txt', header=None, names=['name','sex','count'])
df10 = pd.read_csv('yob2018.txt', header=None, names=['name','sex','count'])
sum_of_dfs = [df, df2, df3, df4, df5, df6, df7, df8, df9, df10]
all_dfs = pd.concat(sum_of_dfs)
all_dfs2 = all_dfs.groupby(['name', 'sex'])['count'].sum()
# print(all_dfs2)

girls_names = all_dfs2[(all_dfs2['name']) & (all_dfs2["sex"] == "M") & (all_dfs2["count"])]
# girls_names = pd.DataFrame(all_dfs2)
# girls_names2 = girls_names.drop
# print(girls_names)
fig = all_dfs2.plot(x = 'name' ,kind = 'line', title = 'chuj', xlabel="Names", ylabel="Count")
# fig.axvline(x = 1948) #vertical line on x = 1963 - that's when the vaccine was introduced in Cali
plt.show()
