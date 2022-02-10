from compare import Compare
import pandas as pd

dfx = pd.DataFrame({'1': [1, 2, 3], '2': [4, 5, 6]})
dfy = pd.DataFrame({'1': [4, 2, 6], '2': [3, 5, 1]})

cpare = Compare(dfx, dfy)

print(cpare.numerical_differences())
print(cpare.nans(ax=1))
print(cpare.compare_values())
print(cpare.compare_shape())
print(cpare.from_to())