import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogout:

    @pytest.mark.usefixtures("example_correct_user")
    def test_logout_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))
        driver.find_element(By.XPATH, "//*[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.quit()

