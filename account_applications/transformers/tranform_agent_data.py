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
        Anything data frame

    1. Rename columns
    """
    data = data.rename(columns = {
        'Id':'id',
        'TenantId':'tenant_id',
        'DeviceId':'device_id',
        'AgentCode':'agent_code',
    })

    data = data[['id','tenant_id','device_id','agent_code']]

    return data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
