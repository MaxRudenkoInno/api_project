import pytest
from endpoints.get_user_Info import GetUserInfo

@pytest.fixture
def url_creator():
    return GetUserInfo()