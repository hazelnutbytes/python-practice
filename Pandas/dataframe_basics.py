import pandas as pd
data = {'Name':['A','B','C'],'Age':[20,25,30]}
df = pd.DataFrame(data)
print(df)
print(df['Age'])
print(df.loc[1])
print(df.iloc[0:2])
