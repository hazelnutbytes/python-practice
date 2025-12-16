df1 = pd.DataFrame({'A':[1,2,3]}, index=['x','y','z'])
df2 = pd.DataFrame({'B':[4,5,6]}, index=['x','y','z'])
print(df1.join(df2))

df3 = pd.DataFrame({'A':[4,5,6]})
print(pd.concat([df1, df3]))
print(pd.concat([df1, df3], axis=1))
