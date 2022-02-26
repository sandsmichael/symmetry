from compare import Compare
import pandas as pd

# dfx = pd.DataFrame({'id':[0,0,0], '1': [1, 2, 3], '2': [4, 5, 6]})
# dfy = pd.DataFrame({'id':[0,0,0], '1': [4, 2, 6], '2': [3, 5, 1]})
# print(cpare.nans(ax=1))
# print(cpare.values())
# print(cpare.shape())
# print(cpare.from_to())
# print(cpare.side_by_side())
'''
'''
def test_funcs():
    funcs = ['nans','values','shape', 'from_to', 'side_by_side']
    for func in funcs:
        # print(f"****************************** {func} ******************************")
        an_object = Compare(dfx, dfy)
        class_method = getattr(Compare, func)
        result = class_method(an_object)
        print(result)


dfx = pd.read_csv('./dummy/data1.csv')
dfy = pd.read_csv('./dummy/data2.csv')
cpare = Compare(dfx, dfy)
print(cpare.objx)
cpare.align()