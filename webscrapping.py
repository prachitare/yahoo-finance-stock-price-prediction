# Importing the dataset

import pandas_datareader.data as web
import datetime
import requests_cache
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
start = datetime.datetime(2016, 12, 31)
end = datetime.datetime(2019, 12, 30)

f = web.DataReader("F", 'yahoo', start, end, session=session)
df = pd.DataFrame(f)
print('DataFrame:\n', df)


# default CSV
csv_data = df.to_csv('file4.csv')
print('\nCSV String:\n', csv_data)
df.to_csv('file1.csv') 
