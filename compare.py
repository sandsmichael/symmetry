import pandas as pd 
import numpy as np

class Compare:
    """[Summary]

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]


    Examples:
    
    """ 



    def __init__(self, objx=None, objy=None):

        self.objx = objx
        self.objy = objy
        
        assert(type(self.objx) == type(self.objy))

        assert (self.objx.columns == self.objy.columns).all(), \
            "DataFrame column names are different"

        if any(self.objx.dtypes != self.objy.dtypes):
            "Data Types are different, trying to convert"
            self.objy = self.objy.astype(self.objx.dtypes)

        if self.objx.equals(self.objy):
            return None

        if self.objx.shape != self.objy.shape:
            print("DataFrame shapes are different")
            return None
        
        if isinstance(self.objx.index, pd.RangeIndex):
            return None

        if self.objx.index.dtype != self.objy.index.dtype:
            print("DataFrame index dtypes are different")
            return None

        # if isinstance(self.objx, pd.DataFrame) & isinstance(self.objy, pd.DataFrame):
        #     CompareFrames(self.objx, self.objy)

        # if isinstance(self.objx, pd.Series) & isinstance(self.objy, pd.Series):
        #     CompareSeries(self.objx, self.objy)

        
    def redact():
        """redact valid values with '--' and leave only NaN or "" visible
        """
        pass

    def nans(self, ax=1):
        return self.objx[self.objx.isnull().any(axis=ax)].style.background_gradient(cmap='RdYlGn', axis=ax)

    def values(self):
        return self.objx.compare(self.objy, keep_equal=False)

    def shape(self):
        return self.objx.compare(self.objy, keep_shape=True)

    def from_to(self):
        ne_stacked = (self.objx != self.objy).stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(self.objx != self.objy)
        changed_from = self.objx.values[difference_locations]
        changed_to = self.objy.values[difference_locations]
        return pd.DataFrame({'from': changed_from, 'to': changed_to}, index=changed.index)


    def highlight_diff(data, color='yellow'):
        attr = 'background-color: {}'.format(color)
        other = data.xs('First', axis='columns', level=-1)
        return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''),
                            index=data.index, columns=data.columns)

    def side_by_side(self):
        df = pd.concat([self.objx.set_index('id'), self.objx.set_index('id')], axis='columns', keys=['1', '2'])
        df = df.swaplevel(axis='columns')[df.columns[1:]]
        return df.style.apply(self.highlight_diff, axis=None)

