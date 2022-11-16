@pytest.mark.usefixtures("example_correct_user", "example_not_correct_user")
def test_successful_registration_with_correct_username_and_password(self, example_correct_user):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/button').click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(
        example_correct_user.name)
    driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(
        example_correct_user.login)
    driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[3]").send_keys(
        example_correct_user.password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 1).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
    driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]").send_keys(
        example_correct_user.login)
    driver.find_element(By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]").send_keys(
        example_correct_user.password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
    assert WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                             "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))
    driver.quit()