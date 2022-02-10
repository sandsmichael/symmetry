from compare import Compare
import pandas as pd

dfx = pd.DataFrame({'id':[0,0,0], '1': [1, 2, 3], '2': [4, 5, 6]})
dfy = pd.DataFrame({'id':[0,0,0], '1': [4, 2, 6], '2': [3, 5, 1]})

cpare = Compare(dfx, dfy)

print(cpare.nans(ax=1))
print(cpare.values())
print(cpare.shape())
print(cpare.from_to())
print(cpare.side_by_side())