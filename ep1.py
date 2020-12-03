import pandas as pd
import numpy as np

df1 = pd.read_csv('transactions.csv')
df2 = df1[df1['STATUS'] == 'OK']
df3 = df2.groupby('CONTRACTOR').sum()
print(df2)
print(df3.iloc[1, 1], '- СТОЛЬКО ДЕНЯГ ПОШЛО В Umbrella Inc.')
max_1 = df1['SUM'].max()
print('ТРИ САМЫХ БОЛЬШИХ ПЛАТЕЖА, ИЗ РЕАЛЬНО ПРОВЕДЕННЫ:')
print(max_1)
df1 = df1.drop(df1[df1['SUM'] == max_1].index)
max_2 = df1['SUM'].max()
print(max_2)
df1 = df1.drop(df1[df1['SUM'] == max_2].index)
max_3 = df1['SUM'].max()
print(max_3)