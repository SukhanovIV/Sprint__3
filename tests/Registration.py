from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestRegistration:

    def test_successful_registration_with_correct_username_and_password(self, driver, example_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_register_1()
        Locators(driver).enter_correct_name(example_correct_user)
        Locators(driver).enter_correct_email_1(example_correct_user)
        Locators(driver).enter_correct_password_1(example_correct_user)
        Locators(driver).clicking_button_register_2()
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_1))
        Locators(driver).enter_correct_email_2(example_correct_user)
        Locators(driver).enter_correct_password_2(example_correct_user)
        Locators(driver).clicking_button_login_in_1()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_place_an_order)).text == "Оформить заказ"

    def test_unsuccessful_registration_with_empty_name(self, driver, example_correct_user, example_not_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_register_1()
        Locators(driver).enter_incorrect_name(example_not_correct_user)
        Locators(driver).enter_correct_email_1(example_correct_user)
        Locators(driver).enter_correct_password_1(example_correct_user)
        Locators(driver).clicking_button_register_2()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_register_2)).text == "Зарегистрироваться"

    def test_unsuccessful_registration_with_incorrect_email(self, driver, example_correct_user, example_not_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_register_1()
        Locators(driver).enter_correct_name(example_correct_user)
        Locators(driver).enter_incorrect_email(example_not_correct_user)
        Locators(driver).enter_correct_password_1(example_correct_user)
        Locators(driver).clicking_button_register_2()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_username_already_exists)).text == "Такой пользователь уже существует"

    def test_unsuccessful_registration_with_incorrect_password(self, driver, example_correct_user, example_not_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_register_1()
        Locators(driver).enter_correct_name(example_correct_user)
        Locators(driver).enter_correct_email_1(example_correct_user)
        Locators(driver).enter_incorrect_password(example_not_correct_user)
        Locators(driver).clicking_button_register_2()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_invalid_password)).text == "Некорректный пароль"
