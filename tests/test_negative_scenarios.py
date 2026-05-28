from api.user_api import UserAPI


def test_invalid_user():

    response = UserAPI.get_user(9999)

    assert response.status_code == 404