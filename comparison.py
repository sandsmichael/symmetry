import pandas as pd 
from compareframes import CompareFrames
from compareframes import CompareSeries

class Comparison():

    def __init__(self, objx, objy):

        self.objx = objx
        self.objy = objy

        print(type(self.objx), type(self.objy))
        
        assert(type(self.objx) == type(self.objy))

        if isinstance(self.objx, pd.DataFrame) & isinstance(self.objy, pd.DataFrame):
            CompareFrames(self.objx, self.objy)

        if isinstance(self.objx, pd.Series) & isinstance(self.objy, pd.Series):
            CompareSeries(self.objx, self.objy)

            
        