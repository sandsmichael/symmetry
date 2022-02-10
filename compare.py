import pandas as pd 
import numpy as np

class Compare:

    def __init__(self, objx, objy):

        self.objx = objx
        self.objy = objy

        print(type(self.objx), type(self.objy))
        
        assert(type(self.objx) == type(self.objy))

        # if isinstance(self.objx, pd.DataFrame) & isinstance(self.objy, pd.DataFrame):
        #     CompareFrames(self.objx, self.objy)

        # if isinstance(self.objx, pd.Series) & isinstance(self.objy, pd.Series):
        #     CompareSeries(self.objx, self.objy)

            

    def numerical_differences(self):
        """compare two frames of the same rxc structure and labels to report any numerical differences
        """
        return self.objx - self.objy

    def redact_valid():
        """redact valid values with '--' and populate only incorrect values based on param
        """
        pass

    def nans(self, ax):
        return self.objx[self.objx.isnull().any(axis=ax)]

    def compare_values(self):
        return self.objx.compare(self.objy, keep_equal=False)

    def compare_shape(self):
        return self.objx.compare(self.objy, keep_shape=True)

    def from_to(self):
        ne_stacked = (self.objx != self.objy).stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(self.objx != self.objy)
        changed_from = self.objx.values[difference_locations]
        changed_to = self.objy.values[difference_locations]
        return pd.DataFrame({'from': changed_from, 'to': changed_to}, index=changed.index)
