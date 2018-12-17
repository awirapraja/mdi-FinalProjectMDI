import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series

data = pd.read_csv('E:\\times.csv', sep=';')
df = pd.DataFrame(data, columns=['WaktuAkses','JumlahMhs'])
df['WaktuAkses'] = pd.to_numeric(df['WaktuAkses'])
df.index = df['WaktuAkses']
del df['WaktuAkses']

df.plot(figsize=(15, 6))
print (data.describe())
plt.show()
