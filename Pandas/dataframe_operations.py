df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
df['D'] = df['A'] + df['B']
df.loc[1,'A'] = 100
df = df.drop(['C','D'], axis=1)
df = df.drop(2, axis=0)
df = df.rename(columns={'A':'Alpha'})
print(df)
