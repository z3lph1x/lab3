import pandas as pd
import numpy as np

df1 = pd.read_csv('transactions.csv')
df2 = df1[df1['STATUS'] == 'OK']
df3 = df2.groupby('CONTRACTOR').sum()
print(df2)
print(df3.iloc[1, 1], '- СТОЛЬКО ДЕНЯГ ПОШЛО В Umbrella Inc.')
print('ТРИ САМЫХ БОЛЬШИХ ПЛАТЕЖА, ИЗ РЕАЛЬНО ПРОВЕДЕННЫХ:')
dfs = df2.sort_values(by='SUM', ascending=False)
print(dfs.iloc[0, 3])
print(dfs.iloc[1, 3])
print(dfs.iloc[2, 3])
