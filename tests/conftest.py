import pytest

class UserRegistration:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

@pytest.fixture
def example_correct_user():
    return UserRegistration(name='Иван', login='IvanSukhanov4027@yandex.ru', password='123456')

@pytest.fixture
def example_not_correct_user():
    return UserRegistration(name='', login='IvanSukhanov400', password='12345')