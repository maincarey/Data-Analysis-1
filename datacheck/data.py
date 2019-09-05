import os
import urllib
import urllib.request
import pandas as pd

URL ="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

# download and cache data
def get_fremont_data(filename='fremont.csv',url=URL, force_download=False):
    if force_download or not os.path.exists(filename):urllib.request.urlretrieve(url,filename)
    data = pd.read_csv('fremont.csv', parse_dates=True, index_col='Date')
    data.columns = ('West','East')
    data['Total'] = data['West'] + data['East']
    return data
