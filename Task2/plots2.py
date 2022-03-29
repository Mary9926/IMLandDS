import pandas as pd

exelData = pd.read_csv('us_contagious_diseases.csv')

data = exelData.loc[((exelData['year'] == 1950) | (exelData['year'] == 1960) | (exelData['year'] == 1970))
                    & (exelData['disease'] == 'Measles')]
data = pd.DataFrame(data)

data['ratio'] = data['count']*100000/data['population']
print(data)

data.to_csv('dataToHistogram.csv', sep=";", index=False, columns=['state', 'year', 'ratio'])
