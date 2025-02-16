import pandas as pd

data = {
    'ages': [14, 18, 24, 42],
    'height': [165, 180, 176, 184]
}

df = pd.DataFrame (data, index=['james', 'Bob', 'Amy', 'Dave'])

print(df.loc['Bob'])
