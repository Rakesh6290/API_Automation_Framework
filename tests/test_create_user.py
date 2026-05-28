from api.user_api import UserAPI
from data.test_data import CREATE_USER_PAYLOAD
from utils.assertions import verify_status_code
from utils.logger import logger


def test_create_user():

    logger.info("Creating User")

    response = UserAPI.create_user(
        CREATE_USER_PAYLOAD
    )

    verify_status_code(response, 201)

    response_json = response.json()

    assert (
        response_json["name"]
        == CREATE_USER_PAYLOAD["name"]
    )

    logger.info("Create User Test Passed")