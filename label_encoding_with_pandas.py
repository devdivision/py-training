import pandas as pd

# create the dataframe
df = {'Position': ['Customer Service', 'Manager', 'Director',
                   'Manager'], 'Salary': [44000, 75000, 90000, 65000]}
df = pd.DataFrame(df)

# create label for position
df['label'] = pd.factorize(df['Position'])[0]

print(df)
