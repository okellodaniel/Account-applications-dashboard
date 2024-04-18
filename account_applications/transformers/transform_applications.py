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
        dataframe
    1. Rename columns
    """
    data.rename(columns = {
        "Id": "id",
        "TenantId": "tenant_id",
        "AggregatorId": "aggregator_id",
        "ExternalReference": "external_reference",
        "ApplicationDate": "application_date",
        "AccountName": "account_name",
        "AccountType": "account_type",
        "AlternativeAccountType": "alternative_account_type",
        "AlternativeMobileMoneyNumber": "alternative_mobile_money_number",
        "AlternativePhoneNumber": "alternative_phone_number",
        "AlternativeBankName": "alternative_bank_name",
        "Tin": "tin",
        "CardNumber": "card_number",
        "Channel": "channel",
        "Currency": "currency",
        "DateOfBirth": "date_of_birth",
        "District": "district",
        "ExpiryDate": "expiry_date",
        "Gender": "gender",
        "GivenName": "given_name",
        "IssueDate": "issue_date",
        "MaritalStatus": "marital_status",
        "MonthlyIncome": "monthly_income",
        "Nin": "nin",
        "Occupation": "occupation",
        "OtherName": "other_name",
        "PhoneNumber": "phone_number",
        "Status": "status",
        "Surname": "surname",
        "LivenessStatus": "liveness_status",
        "LivenessScore": "liveness_score",
        "CustomerPhotoMatchStatus": "customer_photo_match_status",
        "PhotoMatchScore": "photo_match_score",
        "NumberOfFrames": "number_of_frames",
        "Village": "village",
        "Nationality": "nationality",
        "AgentCode": "agent_code",
        "ApplicationSubmittedAt": "application_submitted_at",
        "ApprovalRequestDate": "approval_request_date",
        "ApprovalDate": "approval_date",
        "DeclineDate": "decline_date",
        "AlternativeBankAccountNumber": "alternative_bank_account_number"
    }, inplace=True)

    data.drop(columns={
        'aggregator_id','other_name','number_of_frames','photo_match_score','customer_photo_match_status','liveness_score','liveness_status','aggregator_id','external_reference'
    },inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.columns[0] == 'id', 'The id column was not renamed'
