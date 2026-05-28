from api.user_api import UserAPI
from utils.assertions import verify_status_code
from utils.logger import logger


def test_delete_user():

    logger.info("Deleting user")

    response = UserAPI.delete_user(1)

    verify_status_code(response, 200)

    logger.info("Delete user test passed")