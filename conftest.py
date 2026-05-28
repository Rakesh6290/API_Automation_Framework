from api.user_api import UserAPI
from utils.logger import logger
from utils.assertions import (
    verify_status_code,
    verify_key_exists,
    verify_response_time
)


def test_get_user(user_id):

    logger.info("Fetching user")

    response = UserAPI.get_user(user_id)

    verify_status_code(response, 200)

    response_json = response.json()

    verify_key_exists(response_json, "id")

    verify_response_time(response)

    assert response_json["id"] == user_id

    logger.info("Get user test passed")