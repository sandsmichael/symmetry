from comparison import Comparison
import pandas as pd

dfx = pd.DataFrame({'1': [1, 2, 3], '2': [4, 5, 6]})
dfy = pd.DataFrame({'1': [4, 5, 6], '2': [3, 2, 1]})

Comparison(dfx, dfy)
