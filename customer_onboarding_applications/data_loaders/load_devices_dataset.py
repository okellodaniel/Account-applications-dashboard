import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Load device dataset from download location
    """
    filepath = './dataset/Devices.csv'

    data_dict = {
        'Id': str,
        'DeviceName': str,
        'DeviceImei': int,
    }

    return pd.read_csv(filepath,sep=',',dtype=data_dict,index_col=None)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
