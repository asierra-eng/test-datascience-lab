import os
# import numpy
from urllib.request import urlretrieve

import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
FILENAME = '../../data/fremont.csv'


def get_fremont_dataset(filename=FILENAME, url=URL, force_download=False):
    """
    The function is created to download and cache the dataset in the data folder
    for EMS capstone project.

    Prameters
    ---------
        filename : string (optional)
            Represents the location where we want to cache the data set
        
        url : string(optional)
            Represents the web location of the dataset being analyzed

        force_download : bool (optional)
            if True, force redownload of the dataset
    
    Returns
    -------
        data : pandas.DataFrame
            The fremont bridge data set ready to use in JupyterNotebooks
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    dataset = pd.read_csv(filename, index_col='Date', parse_dates=True)
    return dataset