from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators


class TestGoToPersonalAccount:

    def test_transition_from_constructor_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Профиль')]"))).text == "Профиль"
        driver.quit()

    def test_transition_from_order_feed_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        Locators(driver).clicking_button_order_feed()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Лента заказов')]")))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Профиль')]"))).text == "Профиль"
        driver.quit()

    def test_transition_from_constructor_not_authorized_user(self, driver):
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Вход')]"))).text == "Вход"
        driver.quit()

    def test_transition_from_order_feed_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_order_feed()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Лента заказов')]")))
        Locators(driver).clicking_button_personal_account()
        Locators(driver).clicking_button_personal_account()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Вход')]"))).text == "Вход"
        driver.quit()
