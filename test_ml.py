import pytest
import os
import pandas as pd
from sklearn.model_selection import train_test_split


@pytest.fixture(scope="session")
def data():
    project_path = r"C:\Users\SamrL\PycharmProjects\Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    return df


def test_data_split(data):
    """
    Checks that train and test data splits correctly by 80/20 and has all columns.
    """
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    assert train.shape[1] == test.shape[1], 'Train/Test column counts do not match'
    assert round(train.shape[0] / (train.shape[0] + test.shape[0]), 1) == 0.8, 'Train/Test data split not 80/20'


def test_column_count(data):
    """
    Checks that the input data has the expected number of columns.
    """
    assert data.shape[1] == 15, 'Unexpected number of columns'


def test_for_null(data):
    """
    Null values are encoded as '?' in the original data and no nulls are expected.
    This tests for any non encoded nulls.
    """
    assert data.isnull().sum().sum() == 0, 'Data contains non encoded nulls'
