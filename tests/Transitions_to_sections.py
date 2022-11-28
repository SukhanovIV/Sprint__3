from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestTransitionsToSections:

    def test_transitions_to_bread_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(
                Locators.button_place_an_order))
        Locators(driver).find_branded_sauce_space_sauce()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.sauce_with_antarian_flathead_spikes))
        Locators(driver).find_fluorescent_bread_r2_d3()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.fluorescent_bread_r2_d3))

    def test_transitions_to_sauce_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(
                Locators.button_place_an_order))
        Locators(driver).find_branded_sauce_space_sauce()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.sauce_with_antarian_flathead_spikes))

    def test_transitions_to_filling_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_login_in_account))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(
                Locators.button_place_an_order))
        Locators(driver).find_beef_meteorite()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.fillet_Luminescent_tetraodontimform))

    def test_transitions_to_bread_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_stellar_burgers))
        Locators(driver).find_branded_sauce_space_sauce()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.sauce_with_antarian_flathead_spikes))
        Locators(driver).find_fluorescent_bread_r2_d3()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.fluorescent_bread_r2_d3))

    def test_transitions_to_sauce_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_stellar_burgers))
        Locators(driver).find_branded_sauce_space_sauce()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.sauce_with_antarian_flathead_spikes))

    def test_transitions_to_filling_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                Locators.button_stellar_burgers))
        Locators(driver).find_beef_meteorite()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Locators.fillet_Luminescent_tetraodontimform))
