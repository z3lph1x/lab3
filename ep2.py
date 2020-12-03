import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('flights.csv')
del df['Unnamed: 0']
print(df)

df2 = df.groupby('CARGO').sum()
print(df2)
JP = df2.iloc[0, 0]
MP = df2.iloc[1, 0]
NP = df2.iloc[2, 0]
JW = df2.iloc[0, 1]
MW = df2.iloc[1, 1]
NW = df2.iloc[2, 1]
J = 0
M = 0
N = 0

for i in range(650):
	if (df.loc[i,'CARGO']=='Jumbo'):
		J+=1
	if (df.loc[i,'CARGO']=='Medium'):
		M+=1
	if (df.loc[i,'CARGO']=='Nimble'):
		N+=1

PRICE = {'Jumbo': JP, 'Medium': MP, 'Nimble': NP}
fig, ax = plt.subplots(1,3)

ax[1].bar(range(len(PRICE)), list(PRICE.values()))
ax[1].set_xticks(range(len(PRICE)))
ax[1].set_xticklabels(list(PRICE.keys()))
ax[1].set_title('PRICE')

WEIGHT = {'Jumbo': JW, 'Medium': MW, 'Nimble': NW}

ax[2].bar(range(len(WEIGHT)), list(WEIGHT.values()))
ax[2].set_xticks(range(len(WEIGHT)))
ax[2].set_xticklabels(list(WEIGHT.keys()))
ax[2].set_title('WEIGHT')

NUMBER = {'Jumbo': J, 'Medium': M, 'Nimble': N}

ax[0].bar(range(len(NUMBER)), list(NUMBER.values()))
ax[0].set_xticks(range(len(NUMBER)))
ax[0].set_xticklabels(list(NUMBER.keys()))
ax[0].set_title('NUMBER')

plt.show()
