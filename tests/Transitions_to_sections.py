from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators


class TestTransitionsToSections:

    def test_transitions_to_bread_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element_1 = driver.find_element(By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")
        driver.execute_script("arguments[0].scrollIntoView();", element_1)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]")))
        element_2 = driver.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
        driver.execute_script("arguments[0].scrollIntoView();", element_2)
        assert WebDriverWait(driver, 1).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")))
        driver.quit()

    def test_transitions_to_sauce_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element = driver.find_element(By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]")))
        driver.quit()

    def test_transitions_to_filling_authorized_user(self, driver, example_correct_user):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
        Locators(driver).clicking_button_login_in_account()
        Locators(driver).correct_login(example_correct_user)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element = driver.find_element(By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Филе Люминесцентного тетраодонтимформа')]")))
        driver.quit()

    def test_transitions_to_bread_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element_1 = driver.find_element(By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")
        driver.execute_script("arguments[0].scrollIntoView();", element_1)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]")))
        element_2 = driver.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
        driver.execute_script("arguments[0].scrollIntoView();", element_2)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")))
        driver.quit()

    def test_transitions_to_sauce_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element = driver.find_element(By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]")))
        driver.quit()

    def test_transitions_to_filling_not_authorized_user(self, driver):
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        element = driver.find_element(By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Филе Люминесцентного тетраодонтимформа')]")))
        driver.quit()
