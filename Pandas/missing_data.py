import pandas as pd
import numpy as np
df = pd.DataFrame({'A':[1,2,3],'B':[4,np.nan,6],'C':[7,8,np.nan]})
print(df.isnull())
print(df.dropna())
print(df.fillna(0))
