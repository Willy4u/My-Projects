import pandas as pd

x = {
'hello': [1,3,4],
'world': [1,3,5]
}

df = pd.Dropna(x)

print(df)

