import pandas as pd
import csv

sheet2 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz2")
sheet1 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz1")

#task2
group_data = sheet2.groupby(['state'], as_index=False)['n_killed'].sum()
group_data['murder_rate'] = group_data['n_killed'] / sheet1['population']
group_data.rename(columns={"n_killed": "murder_total"}, inplace=True)

new_csv = pd.merge(sheet1, group_data, on="state")
print(new_csv)
new_csv.to_csv('data.csv', sep=";", index=False)


if __name__ == '__main__':
    print('PyCharm')
