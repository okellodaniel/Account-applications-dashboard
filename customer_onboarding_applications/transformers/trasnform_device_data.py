if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data = data[['Id','DeviceName','DeviceImei']]
    data = data.rename(columns={
        'Id':'id',
        'DeviceName':'device_name',
        'DeviceImei':'device_imei',
    })
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.columns[0] == 'id', 'The id column was not renamed'
