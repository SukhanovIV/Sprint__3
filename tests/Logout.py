from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestLogout:

    def test_logout_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(
                Locators.title_profile))
        Locators(driver).clicking_button_exit()
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.title_login)).text == "Вход"
