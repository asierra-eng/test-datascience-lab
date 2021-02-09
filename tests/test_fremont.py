from src.localingest import get_fremont_dataset
import pandas as pd

def test_fremont_dataset():
    dataset = get_fremont_dataset()
    assert all(dataset.columns == [
               'Fremont Bridge Total', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk'])
    assert isinstance(dataset.index, pd.DatetimeIndex)
