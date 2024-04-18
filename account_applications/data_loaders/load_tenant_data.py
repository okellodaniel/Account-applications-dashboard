import io
import os
import pandas as pd
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load tenant data from the dataset folder
    """
    
    data_dict = {
        'Id': str,
        'TenantName':str
    }

    return pd.read_csv('./dataset/Tenants.csv',dtype=data_dict,sep=',',index_col=None)




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
