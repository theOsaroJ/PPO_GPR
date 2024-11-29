import pandas as pd
data = pd.read_csv('All_excluding_prior.csv')
print(data.head())

from random import shuffle
# shuffle the data
sdata = data.sample(frac=1)
print(sdata.head())
print(sdata.shape)

sdata.to_csv('Splitting.csv', index=False)
