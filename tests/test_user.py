import requests

from endpoints.get_user_Info import GetUserInfo

def test_user_info(url_creator):
    user_url = "https://test.behindthehands.com/api/user/info"
    user_id = "cd32fa3a-8629-4d29-9655-60b2bdc0b8c4"
    # Send request userinfo
    url_creator.test_user_info_for_id()
    # check staus code
    url_creator.check_response_status_is_ok()
    # Check role
    url_creator.check_role_is_admin()
