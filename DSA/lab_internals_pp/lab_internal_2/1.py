import pandas as pd
data = {"a":[1,None,3],"b":[4,5,None]}
s=pd.DataFrame(data)
print(s)
print(pd.dropna())
print(pd.fillna(o))