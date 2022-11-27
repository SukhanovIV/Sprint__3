import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class UserRegistration:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password


@pytest.fixture
def example_correct_user():
    return UserRegistration(name='Иван', login='IvanSukhanov3914@yandex.ru', password='123456')


@pytest.fixture
def example_not_correct_user():
    return UserRegistration(name='', login='IvanSukhanov366', password='12345')


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def email():
    fake = Faker()
    yield fake.email()
