import pandas as pd
from datetime import datetime

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 5000)

econ_data = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/econ_dec_90_15_missing_filled.csv')

'''
If you give your DataFrame a DatetimeIndex, then you can take advantage of the df.resample and df.interpolate('time') methods.

To make df.index a DatetimeIndex you might be tempted to use set_index('Year'). However, the Year by itself is not unique 
since it is repeated for each Country. In order to call resample we will need a unique index. So use df.pivot instead:
'''

# convert integer years into `datetime64` values
'''
The docs mention (and the dtype name datetime64 hints strongly) that the underlying data type are 8-byte ints. 
So in order to do numerical math on datetime64s it is sometimes necessary to use astype('i8') to convert the datetime64
to its underlying integer value.
'''

print("########## Start: ", datetime.now().time())

econ_data['YEAR'] = (econ_data['YEAR'].astype('i8')-1970).view('datetime64[Y]')
econ_data = econ_data.pivot(index='YEAR', columns='ORI')

'''
You can then use df.resample('A').mean() to resample the data with yearly frequency. You can think of resample('A') as 
chopping up df into groups of 1-year intervals.  resample returns a DatetimeIndexResampler object whose mean method 
aggregates the values in each group by taking the mean. Thus mean() returns a DataFrame with one row for every year. 
Since your original df has one datum every 5 years, most of the 1-year groups will be empty, so the mean returns NaNs 
for those years. If your data is consistently spaced at 5-year intervals, then instead of .mean() you could use .first()
or .last() instead. They would all return the same result.
'''

econ_data = econ_data.resample('A').mean()

'''
And then df.interpolate(method='time') will linearly interpolate missing NaN values based on the nearest non-NaN values
and their associated datetime index values.
'''
econ_data = econ_data.interpolate(method='time')

econ_data = econ_data.stack('ORI')
econ_data = econ_data.reset_index()
econ_data = econ_data.sort_values(by=['ORI', 'YEAR'])

print("########## End: ", datetime.now().time())


econ_data.to_csv('/Users/salma/Research/us-crime-analytics/data/econ_int_pivot.csv', index=False)