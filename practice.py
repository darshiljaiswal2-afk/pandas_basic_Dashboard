import pandas as pd

df = pd.read_json("sample___Data.json", orient='records')
print(df)