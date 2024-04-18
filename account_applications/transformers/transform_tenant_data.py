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
        Anything (data frame)
    """
    # Specify your transformation logic here
    """ 
    1. remove Unammed column
    2. Refactor the column Names 
    """

    data = data[['Id','TenantName']]

    data = data.rename(columns={
        'Id':'id',
        'TenantName':'tenant_name'
    })

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.columns[0] == 'id', 'The id column was not renamed'
