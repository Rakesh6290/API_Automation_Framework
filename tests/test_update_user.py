from api.user_api import UserAPI
from data.test_data import UPDATE_USER_PAYLOAD
from utils.assertions import verify_status_code
from utils.logger import logger


def test_update_user():

    logger.info("Updating user")

    response = UserAPI.update_user(
        1,
        UPDATE_USER_PAYLOAD
    )

    verify_status_code(response, 200)

    response_json = response.json()

    assert (
        response_json["name"]
        == UPDATE_USER_PAYLOAD["name"]
    )

    logger.info("Update user test passed")