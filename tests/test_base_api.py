from unittest.mock import Mock

from api.base_api import BaseApi


def test_base_api_adds_auth_header_for_post_request():
    session = Mock()
    session.request.return_value = Mock(status_code=200)
    client = BaseApi(session=session, base_url="https://stellarburgers.education-services.ru/")

    client.post("api/test", access_token="Bearer token", json={"key": "value"})

    session.request.assert_called_once_with(
        method="POST",
        url="https://stellarburgers.education-services.ru/api/test",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer token",
        },
        json={"key": "value"},
    )
