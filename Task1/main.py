import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Lab1.xlsx')
dfa = pd.read_excel('Lab1a.xlsx')

df2 = df.groupby(['state'])['n_killed'].sum()
dfa.columns = ['state', 'population']
df3 = pd.DataFrame(df2)
sum_df = pd.merge(df3, dfa, on="state")
print(sum_df)
