import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
del df['Unnamed: 0']
print(df)
a = []
JumboW = 0
MediumW = 0
NimbleW = 0
JumboP = 0
MediumP = 0
NimbleP = 0

for i in range(len(df.index)):
    a.append(df.loc[i, 'CARGO'])
    if df.loc[i, 'CARGO'] == 'Jumbo':
        JumboW += df.loc[i, 'WEIGHT']
        JumboP += df.loc[i, 'PRICE']
    elif df.loc[i, 'CARGO'] == 'Medium':
        MediumW += df.loc[i, 'WEIGHT']
        MediumP += df.loc[i, 'PRICE']
    elif df.loc[i, 'CARGO'] == 'Nimble':
        NimbleW += df.loc[i, 'WEIGHT']
        NimbleP += df.loc[i, 'PRICE']

Jumbo = a.count('Jumbo')
Medium = a.count('Medium')
Nimble = a.count('Nimble')

gr1 = {'Jumbo': Jumbo, 'Medium': Medium, 'Nimble': Nimble}
x1 = list(gr1.keys())
y1 = list(gr1.values())

gr2 = {'Jumbo': JumboW, 'Medium': MediumW, 'Nimble': NimbleW}
x2 = list(gr2.keys())
y2 = list(gr2.values())

gr3 = {'Jumbo': JumboP, 'Medium': MediumP, 'Nimble': NimbleP}
x3 = list(gr3.keys())
y3 = list(gr3.values())

fig, ax = plt.subplots(1, 3)


ax[0].bar(x1, y1)
ax[0].set_title('Number of flights')

ax[1].bar(x2, y2)
ax[1].set_title('Total weight')

ax[2].bar(x3, y3)
ax[2].set_title('Total price')
plt.show()

