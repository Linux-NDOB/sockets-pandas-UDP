import pandas as pd

dic = { "nombre": "juan", "edad": 20, "pais": "colombia"}

df = pd.DataFrame([dic])
df.to_csv('totals.csv', index=False, header=True)

print(df)
df.loc[0, ['pais']] = ['Venezuela']
print(df.loc[0, ['pais']])
