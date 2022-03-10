import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib
import openpyxl
from openpyxl import writer
from pandas import ExcelWriter
from pandas import ExcelFile

sheet2 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz2")
sheet1 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz1")

#print("Column headings:")
#print(sheet2.columns)

group_data = sheet2.groupby(['state'], as_index=False)['n_killed'].sum()
print(group_data)


"""
print(len(group_data))
print(len(sheet1['population']))
murder_rate = group_data['n_killed'].values / sheet1['population'].values
print(murder_rate)
"""
#plt.plot(sheet1['population'])
#sheet1.head()
#plt.plot(group_data['n_killed'])
#plt.show()



header = ['state', 'population', 'mourders_total', 'murder_rate']
data = [
    [group_data['state'], sheet1['population'], group_data['n_killed'], '0']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
