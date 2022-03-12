import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_excel('Lab1.xlsx')
# dfa = pd.read_excel('Lab1a.xlsx')
sheet2 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz2")
sheet1 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz1")

df2 = sheet2.groupby(['state'])['n_killed'].sum()
sheet1.columns = ['state', 'population']
df3 = pd.DataFrame(df2)
sum_df = pd.merge(df3, sheet1, on="state")
print(sum_df)

names = list(df2.keys())
values = list(df2.values)
# values = list[df2.values()]

plt.bar(range(len(df2)), values, tick_label=names)
plt.xticks(rotation='vertical')
plt.show()