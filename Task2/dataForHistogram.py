import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
exelData = pd.read_csv('us_contagious_diseases.csv')
#1950
data = exelData.loc[(exelData['year'] == 1950)& (exelData['disease'] == 'Measles')]
data = pd.DataFrame(data)

data['ratio'] = data['count']*100000/data['population']
print(data)

data.to_csv('1950.csv', sep=";", index=False, columns=['state', 'year', 'ratio'])


#1960

data = exelData.loc[(exelData['year'] == 1960)& (exelData['disease'] == 'Measles')]
data = pd.DataFrame(data)

data['ratio'] = data['count']*100000/data['population']
print(data)

data.to_csv('1960.csv', sep=";", index=False, columns=['state', 'year', 'ratio'])


#1970

data = exelData.loc[(exelData['year'] == 1970)& (exelData['disease'] == 'Measles')]
data = pd.DataFrame(data)

data['ratio'] = data['count']*100000/data['population']
print(data)

data.to_csv('1970.csv', sep=";", index=False, columns=['state', 'year', 'ratio'])
