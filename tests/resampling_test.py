import pandas as pd
import numpy as np
import random

data = {'datetime' : pd.date_range(start='1/15/2018',
                                  end='02/14/2018',
                                  freq='D')\
                     .append(pd.date_range(start='1/15/2018',
                                           end='02/14/2018',
                                           freq='D')),
        'house' : ['house1' for i in range(31)]
                  + ['house2' for i in range(31)],
        'readvalue' : [0.5 + 0.5*np.sin(2*np.pi/30*i)
                       for i in range(31)]\
                     + [0.5 + 0.5*np.cos(2*np.pi/30*i)
                       for i in range(31)]}
df0 = pd.DataFrame(data, columns = ['datetime',
                                    'house',
                                    'readvalue'])

print(df0)

print()

#Randomly drop half the reads
random.seed(42)
df0 = df0.drop(random.sample(range(df0.shape[0]),
                             k=int(df0.shape[0]/2)))


'''
To interpolate the data, we can make use of the groupby()-function followed by resample(). 
However, first we need to convert the read dates to datetime format and set them as the index of our dataframe:
'''
df = df0.copy()
df['datetime'] = pd.to_datetime(df['datetime'])
df.index = df['datetime']
del df['datetime']


'''
Since we want to interpolate for each house separately, we need to group our data by ‘house’ before we can use the resample() function with the option ‘D’ to resample the data to a daily frequency.
The next step is then to use mean-filling, forward-filling or backward-filling to determine how the newly generated grid is supposed to be filled
'''

df_res = df.groupby('house').resample('D').mean().head(4)

print(df_res)
# then can call inerpoalte on df_res to interpolate the NaN values between 2 points
