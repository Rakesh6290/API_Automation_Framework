from api.user_api import UserAPI
from utils.logger import logger
from utils.assertions import (
    verify_status_code,
    verify_response_time
)

def test_get_user():

    logger.info("Fetching user")

    response = UserAPI.get_user(2)

    verify_status_code(response, 200)

    verify_response_time(response)

    response_json = response.json()

    assert response_json["id"] == 2

    logger.info("Get user test passed")