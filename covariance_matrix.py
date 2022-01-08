import pandas as pd

df = pd.DataFrame(
    {"Age": [25, 32, 37],
     "Expeorence": [2, 6, 9],
     "Salary": [2000, 3000, 3500]}
)

cov_matrix = df.cov()
print(cov_matrix)
