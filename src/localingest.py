import os
from urllib.request import urlretrieve

import pandas as pd

from pathlib import Path, PureWindowsPath

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
PROJECT = 'test-datascience-lab'

def get_fremont_dataset(project_name=PROJECT, url=URL, force_download=False):
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

    if Path.cwd().parts[-1]==project_name:
        filename = PureWindowsPath(
            Path.cwd()).joinpath('data', 'fremont.csv')
    else:
        filename = PureWindowsPath(
            Path.cwd()).parents[0].joinpath('data', 'fremont.csv')

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    dataset = pd.read_csv(filename, index_col='Date')
    try:
        dataset.index = pd.to_datetime(dataset.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        dataset.index = pd.to_datetime(dataset.index)
    return dataset

#dataset = get_fremont_dataset()
#print(dataset.head())
