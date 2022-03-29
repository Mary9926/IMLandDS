import pandas as pd
import matplotlib.pyplot as plt

sheet2 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz2")
sheet1 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz1")

#task 1
df2 = sheet2.groupby(['state'])['n_killed'].sum()
print(df2)
sheet1.columns = ['state', 'population']
df3 = pd.DataFrame(df2)
sum_df = pd.merge(df3, sheet1, on="state")
print(sum_df)

names = list(df2.keys())
values = list(df2.values)

plt.bar(range(len(df2)), values, tick_label=names)
plt.xticks(rotation='vertical')
plt.show()

#task2
group_data = sheet2.groupby(['state'], as_index=False)['n_killed'].sum()
group_data['murder_rate'] = group_data['n_killed'] / sheet1['population']
group_data.rename(columns={"n_killed": "murder_total"}, inplace=True)

new_csv = pd.merge(sheet1, group_data, on="state")
print(new_csv)
new_csv.to_csv('data.csv', sep=";", index=False)



if __name__ == '__main__':
    print('PyCharm')
