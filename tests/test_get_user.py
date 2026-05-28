import pytest

from data.test_data import USER_IDS
from api.user_api import UserAPI
from utils.assertions import (
    verify_status_code,
    verify_response_time
)


@pytest.mark.parametrize("user_id", USER_IDS)
def test_get_user(user_id):

    response = UserAPI.get_user(user_id)

    verify_status_code(response, 200)

    verify_response_time(response)

    assert response.json()["id"] == user_id