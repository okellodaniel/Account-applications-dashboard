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


def kaggle_downloader(dataset_path):
    os.environ['KAGGLE_USERNAME'] = 'danielokello'
    os.environ['KAGGLE_KEY'] = 'bccfbb5a23280265af48816d6a03bd35'

    api = KaggleApi()
    api.authenticate()

    return api.dataset_download_files(dataset_path, path="./dataset")

def unzip_dataset(zip_filepath,dest_dir):
    """
    Unzip a zip file.

    Parameters:
    zip_filepath (str): The path to the zip file.
    dest_dir (str): The directory to extract files to.
    """
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    dataset_name = 'customer-onboarding-applications'
    url = f'danielokello/{dataset_name}'
    kaggle_downloader(url)

    unzip_dataset(f'./dataset/{dataset_name}.zip', './dataset')

    data_dict = {
    "Id": str,
    "TenantId": str,
    "AggregatorId": str,
    "ExternalReference": str,
    "AccountName": str,
    "AccountType": str,
    "AlternativeAccountType": str,
    "AlternativeMobileMoneyNumber": pd.Int64Dtype(),
    "AlternativePhoneNumber": pd.Int64Dtype(),
    "AlternativeBankName": str,
    "Tin": pd.Int64Dtype(),
    "CardNumber": pd.Int64Dtype(),
    "Channel": str,
    "Currency": str,
    "District": str,
    "Gender": str,
    "GivenName": str,
    "MaritalStatus": str,
    "MonthlyIncome": str,
    "Nin": str,
    "Occupation": str,
    "OtherName": str,
    "PhoneNumber": pd.Int64Dtype(),
    "Status": str,
    "Surname": str,
    "LivenessStatus": str,
    "LivenessScore": float,
    "CustomerPhotoMatchStatus": str,
    "PhotoMatchScore": float,
    "NumberOfFrames": pd.Int64Dtype(),
    "Village": str,
    "Nationality": str,
    "AgentCode": str,
    "AlternativeBankAccountNumber": pd.Int64Dtype()
    }

    parse_dates = ['ApplicationDate','DateOfBirth','ExpiryDate','IssueDate','ApplicationSubmittedAt','ApprovalRequestDate','ApprovalDate','DeclineDate']

    return pd.read_csv('./dataset/Applications.csv',dtype=data_dict,sep=',',index_col=None)




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
