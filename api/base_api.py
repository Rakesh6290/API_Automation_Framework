import requests


class BaseAPI:

    session = requests.Session()

    @classmethod
    def get(cls, endpoint):
        return cls.session.get(endpoint)

    @classmethod
    def post(cls, endpoint, payload):
        return cls.session.post(
            endpoint,
            json=payload
        )

    @classmethod
    def put(cls, endpoint, payload):
        return cls.session.put(
            endpoint,
            json=payload
        )

    @classmethod
    def delete(cls, endpoint):
        return cls.session.delete(endpoint)