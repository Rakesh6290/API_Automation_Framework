from api.user_api import UserAPI
from utils.fake_data import create_user_payload
from utils.assertions import verify_status_code
from utils.logger import logger


def test_create_user():

    payload = create_user_payload()

    logger.info("Creating User")

    response = UserAPI.create_user(payload)

    verify_status_code(response, 201)

    response_json = response.json()

    assert response_json["name"] == payload["name"]

    logger.info("Create User Test Passed")