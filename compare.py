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

    def __init__(self, objx:pd.DataFrame=None, objy:pd.DataFrame=None):
        """Takes two objects of the shape, types and size and compares them for differeences

        :param objx: [ParamDescription], defaults to [DefaultParamVal]
        :param objy: [ParamDescription], defaults to [DefaultParamVal]

        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: a dataframe showing the differences or changes between the two objects
        :rtype: pd.DataFrame
        """

        self.objx = objx
        self.objy = objy
        
        assert(type(self.objx) == type(self.objy)), \
            "[ERROR] Objects do not have the same type"

        assert (self.objx.columns == self.objy.columns).all(), \
            "[ERROR] DataFrame column names are different"
        
        assert(self.objx.shape != self.objy.shape), \
            print('[ERROR] DataFrame shapes are not the same')

        if any(self.objx.dtypes != self.objy.dtypes):
            "Data Types are different, trying to convert"
            try:
                self.objy = self.objy.astype(self.objx.dtypes)
            except:
                '[ERROR] Unable to convert data types'

        if self.objx.index.dtype != self.objy.index.dtype:
            print("[ERROR] DataFrame index dtypes are different")
        
        if self.objx.equals(self.objy):
            return None

        
    def redact():
        """redact valid values with '--' and leave only NaN or "" visible
        """
        pass

    def nans(self, ax=1):
        ''' show any nan values in the dataframe '''
        return self.objx[self.objx.isnull().any(axis=ax)].style.background_gradient(cmap='RdYlGn', axis=ax)

    def values(self):
        return self.objx.compare(self.objy, keep_equal=False)

    def shape(self):
        return self.objx.compare(self.objy, keep_shape=True)

    def align(self):
        self.objx.compare(self.objy, align_axis='rows')

    def equality(self):
        return self.objx.equals(self.objy)

    def common_rows(self):
        df = df1.merge(df2, how = 'inner' ,indicator=False)

    def common_rows2(self):
        df = pd.concat([df1, df2])
  
        df = df.reset_index(drop=True)
        
        df_group = df.groupby(list(df.columns))
        
        idx = [x[0] for x in df_group.groups.values() if len(x) > 1]
        df.reindex(idx)

    def conditional_compare(self):
        df1['prices_match'] = np.where(df1['price_1'] == df2['price_2'], 'True', 'False')

    
    def different_values_in_same_column(self):
        set(df1.Temp).symmetric_difference(df2.Temp)

    def in_left_not_right(self):
        df = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']

    def in_right_not_left(self):
        df = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']


    def not_duplicates(self):
        pd.concat([df1,df2]).drop_duplicates(keep=False)



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

    def side_by_side(self, ix):
        df = pd.concat([self.objx.set_index(ix), self.objx.set_index(ix)], axis='columns', keys=['col1', 'col2'])
        df = df.swaplevel(axis='columns')#[df.columns[1:]]
        return df#df.style.apply(self.highlight_diff, axis=None)

    def dataframe_difference(self, which=None):
        """Find rows which are different between two DataFrames."""
        comparison_df = self.objx.merge(
            self.objy,
            indicator=True,
            how='outer'
        )
        if which is None:
            diff_df = comparison_df[comparison_df['_merge'] != 'both']
        else:
            diff_df = comparison_df[comparison_df['_merge'] == which]
        diff_df.to_csv('data/diff.csv')
        return diff_df