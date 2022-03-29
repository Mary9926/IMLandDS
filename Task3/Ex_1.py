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

all_dfs = pd.DataFrame(all_dfs)
#print(all_dfs)
all_dfs2 = all_dfs.groupby(['name', 'sex'], as_index=False)['count'].sum()

all_dfs2 = pd.DataFrame(all_dfs2)
#print(all_dfs2)
#all_dfs2.to_csv('all_dfs2.csv', sep=";", index=False, columns=['name', 'sex', 'count'])


girls_names = all_dfs2.loc[(all_dfs2['sex'] == 'F')]
girls_names = pd.DataFrame(girls_names)
print(girls_names)

boys_names = all_dfs2.loc[(all_dfs2['sex'] == 'M')]
boys_names = pd.DataFrame(boys_names)
print(boys_names)


top_3Girls = girls_names.nlargest(3, 'count')
top_3Boys = boys_names.nlargest(3, 'count')

print("top_3Girls")
print(top_3Girls)
print("top_3Girls")
print(top_3Boys)

fig = top_3Girls.plot(x = 'name' ,kind = 'bar', title = 'top 3 girls names', xlabel="Names", ylabel="Count")
plt.show()
fig = top_3Boys.plot(x = 'name' ,kind = 'bar', title = 'top 3 boys names', xlabel="Names", ylabel="Count")
plt.show()