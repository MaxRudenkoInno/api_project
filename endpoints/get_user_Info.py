import requests

user_url = "https://test.behindthehands.com/api/user/info"


class GetUserInfo:
    status = None
    role = None

    def test_user_info_for_id(self):
        response = requests.get(
            url=user_url,
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6ImNkMzJmYTNhLTg2MjktNGQyOS05NjU1LTYwYjJiZGMwYjhjNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlVzZXIiLCJleHAiOjE3ODM3NTQ3MDMsImlzcyI6Imh0dHBzOi8vYmVoaW5kdGhlaGFuZHMuY29tIiwiYXVkIjoiaW5ub3dpc2UuYXBwLmxhdWZmZXIuY29tIn0.HrHLkuNMBgXQmIQGYbPwipGGh1GGrFi12xasUWP5hyY"},
        )
        self.status = response.status_code
        self.role = response.json()["role"]
        return response

    def check_response_status_is_ok(self):
        assert self.status == 200

    def check_role_is_admin(self):
        assert self.role == 1