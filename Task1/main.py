import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import openpyxl
from openpyxl import writer
from pandas import ExcelWriter
from pandas import ExcelFile

sheet2 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz2")
sheet1 = pd.read_excel('gun_violence_data_2013_2018.xlsx', sheet_name="Arkusz1")

#first task
group_data = sheet2.groupby(['state'], as_index=False)['n_killed'].sum()
print(group_data)
plt.bar(group_data['state'], group_data['n_killed'])
plt.show()

#task 2
murder_rate = group_data['n_killed'] / sheet1['population']
print(murder_rate)


newCsv = pd.merge(sheet1, group_data['n_killed'], on=sheet1['state'], how ='left')
print(newCsv)


if __name__ == '__main__':
    print('PyCharm')
