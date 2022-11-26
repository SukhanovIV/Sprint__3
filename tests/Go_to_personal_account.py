from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestGoToPersonalAccount:

    def test_transition_from_constructor_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.title_assemble_burger))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_profile)).text == "Профиль"

    def test_transition_from_order_feed_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.title_assemble_burger))
        Locators(driver).clicking_button_order_feed()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Locators.button_order_feed))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_profile)).text == "Профиль"

    def test_transition_from_constructor_not_authorized_user(self, driver):
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_login)).text == "Вход"

    def test_transition_from_order_feed_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_order_feed()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Locators.button_order_feed))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            Locators.title_login)).text == "Вход"
