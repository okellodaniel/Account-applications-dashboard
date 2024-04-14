import io
import os
import pandas as pd
import requests
import zipfile

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Load tenant data from the dataset folder
    """
    
    data_dict = {
        'Id': str,
        'TenantId':str,
        'AgentCode': str,
        'DeviceId':str
    }

    return pd.read_csv('./dataset/Agents.csv',dtype=data_dict,sep=',',index_col=None)




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
