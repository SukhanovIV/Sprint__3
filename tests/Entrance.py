from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestEntrance:

    def test_login_via_personal_account(self, driver, example_correct_user):
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_1))
        Locators(driver).correct_login(example_correct_user)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_place_an_order)).text == "Оформить заказ"

    def test_login_via_the_main_page(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_place_an_order)).text == "Оформить заказ"

    def test_login_via_registration_form(self, driver, example_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_register_1()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_login_in_2))
        Locators(driver).clicking_button_login_in_2()
        Locators(driver).correct_login(example_correct_user)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_place_an_order)).text == "Оформить заказ"

    def test_login_via_password_recovery(self, driver, example_correct_user):
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).clicking_button_recover_password()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_login_in_2))
        Locators(driver).clicking_button_login_in_2()
        Locators(driver).correct_login(example_correct_user)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.button_place_an_order)).text == "Оформить заказ"
