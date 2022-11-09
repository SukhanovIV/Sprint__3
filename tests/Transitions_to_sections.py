import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransitionsToSections:

    @pytest.mark.usefixtures("example_correct_user")
    def test_transitions_to_bread_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='text text_type_main-large mb-5 mt-10']")))
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))
        driver.find_element(By.XPATH, "(//*[@class='AppHeader_header__link__3D_hX'])[1]").click()
        element = driver.find_element(By.XPATH, "//*[@alt='Краторная булка N-200i']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()

    def test_transitions_to_sauce_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='text text_type_main-large mb-5 mt-10']")))
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))
        driver.find_element(By.XPATH, "(//*[@class='AppHeader_header__link__3D_hX'])[1]").click()
        element = driver.find_element(By.XPATH, "//*[@alt='Соус фирменный Space Sauce']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()

    def test_transitions_to_filling_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='text text_type_main-large mb-5 mt-10']")))
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))
        driver.find_element(By.XPATH, "(//*[@class='AppHeader_header__link__3D_hX'])[1]").click()
        element = driver.find_element(By.XPATH, "//*[@alt='Говяжий метеорит (отбивная)']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()

    def test_transitions_to_bread_not_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        element = driver.find_element(By.XPATH, "//*[@alt='Соус фирменный Space Sauce']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element_2 = driver.find_element(By.XPATH, "//*[@alt='Краторная булка N-200i']")
        driver.execute_script("arguments[0].scrollIntoView();", element_2)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()

    def test_transitions_to_sauce_not_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        element = driver.find_element(By.XPATH, "//*[@alt='Соус фирменный Space Sauce']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()

    def test_transitions_to_filling_not_authorized_user(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        element = driver.find_element(By.XPATH, "//*[@alt='Говяжий метеорит (отбивная)']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))
        driver.quit()
