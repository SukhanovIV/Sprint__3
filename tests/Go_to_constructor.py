from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestGoToConstructor:

    def test_transition_in_constructor_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_designer()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.title_assemble_burger)).text == "Соберите бургер"

    def test_transition_in_constructor_authorized_user_from_stellar_burgers(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located(Locators.title_profile))
        Locators(driver).clicking_button_stellar_burgers()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.title_assemble_burger)).text == "Соберите бургер"

    def test_transition_in_constructor_authorized_user_from_order_feed(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Locators.title_profile))
        Locators(driver).clicking_button_order_feed()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Locators.button_designer))
        Locators(driver).clicking_button_designer()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.title_assemble_burger)).text == "Соберите бургер"

    def test_transition_in_constructor_not_authorized_user(self, driver):
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Locators.title_login))
        Locators(driver).clicking_button_designer()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.title_assemble_burger)).text == "Соберите бургер"
