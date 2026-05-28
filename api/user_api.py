from api.base_api import BaseAPI
from utils.config import BASE_URL


class UserAPI(BaseAPI):

    @classmethod
    def get_user(cls, user_id):

        return cls.get(
            f"{BASE_URL}/users/{user_id}"
        )

    @classmethod
    def create_user(cls, payload):

        return cls.post(
            f"{BASE_URL}/users",
            payload
        )

    @classmethod
    def update_user(
        cls,
        user_id,
        payload
    ):

        return cls.put(
            f"{BASE_URL}/users/{user_id}",
            payload
        )

    @classmethod
    def delete_user(cls, user_id):

        return cls.delete(
            f"{BASE_URL}/users/{user_id}"
        )