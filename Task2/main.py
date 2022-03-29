import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#task 3
exelData = pd.read_csv('us_contagious_diseases.csv')
data_1950 = exelData[(exelData['year'] == 1950)]
data_1950 = pd.DataFrame(data_1950)
data_1950['ratio'] = data_1950['count']*100000/data_1950['population']
print(data_1950)

data_1950.to_csv('data_1950.csv', sep=";", index=False, columns=['disease', 'state', 'ratio'])

data_1960 = exelData[(exelData['year'] == 1960)]
data_1960 = pd.DataFrame(data_1960)
data_1960['ratio'] = data_1960['count']*100000/data_1960['population']
print(data_1960)

data_1960.to_csv('data_1960.csv', sep=";", index=False, columns=['disease', 'state', 'ratio'])


data_1970 = exelData[(exelData['year'] == 1970)]
data_1970 = pd.DataFrame(data_1970)
data_1970['ratio'] = data_1970['count']*100000/data_1970['population']
print(data_1970)

data_1970.to_csv('data_1970.csv', sep=";", index=False, columns=['disease', 'state', 'ratio'])


if __name__ == '__main__':
    print('PyCharm')

