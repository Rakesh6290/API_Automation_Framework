from faker import Faker

fake = Faker()


def create_user_payload():
    return {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }