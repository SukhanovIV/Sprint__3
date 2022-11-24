from selenium.webdriver.common.by import By


class Locators:
    button_login_in_account = [By.XPATH, './/button']  # Кнопка "Войти в аккаунт"
    button_register_1 = [By.XPATH, ".//a[text()='Зарегистрироваться']"]  # Кнопка "Зарегистрироваться" № 1
    name_entry_button = [By.XPATH,
                         "(//*[@class='text input__textfield text_type_main-default'])[1]"]  # Кнопка ввода "Имени" для регистрации
    email_entry_button_1 = [By.XPATH,
                            "(//*[@class='text input__textfield text_type_main-default'])[2]"]  # Кнопка ввода "email" для регистрации
    password_entry_button_1 = [By.XPATH,
                               "(//*[@class='text input__textfield text_type_main-default'])[3]"]  # Кнопка ввода "Пароля" для регистрации
    email_entry_button_2 = [By.XPATH,
                            "(//*[@class='text input__textfield text_type_main-default'])[1]"]  # Кнопка ввода "email" для входа
    password_entry_button_2 = [By.XPATH,
                               "(//*[@class='text input__textfield text_type_main-default'])[2]"]  # Кнопка ввода "Пароля" для входа
    button_register_2 = [By.XPATH, ".//button[text()='Зарегистрироваться']"]  # Кнопка "Зарегистрироваться" № 2
    button_login_in_1 = [By.XPATH, "//button[text()='Войти']"]  # Кнопка "Войти" № 1
    button_login_in_2 = [By.XPATH, "//a[contains(text(),'Войти')]"]  # Кнопка "Войти" № 2
    button_recover_password = [By.XPATH,
                               "// a[contains(text(), 'Восстановить пароль')]"]  # Кнопка "Восстановить пароль"
    button_personal_account = [By.XPATH, ".//p[contains(text(),'Личный Кабинет')]"]  # Кнопка "Личный кабинет"
    button_exit = [By.XPATH, "// button[contains(text(), 'Выход')]"]  # Кнопка "Выход"
    button_designer = [By.XPATH, "//p[contains(text(),'Конструктор')]"]  # Кнопка "Конструктор"
    button_order_feed = [By.XPATH, "//p[contains(text(),'Лента Заказов')]"]  # Кнопка "Лента заказов"
    button_stellar_burgers = [By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']"]  # Кнопка "stellar_burgers"
    button_bread = [By.XPATH, "//span[contains(text(),'Булки')]"]  # Кнопка "Булки"
    button_sauce = [By.XPATH, "//span[contains(text(),'Соусы')]"]  # Кнопка "Соусы"
    button_filling = [By.XPATH, "//span[contains(text(),'Начинки')]"]  # Кнопка "Начинки"

    def __init__(self, driver):
        self.driver = driver

    def clicking_button_login_in_account(self):
        self.driver.find_element(*self.button_login_in_account).click()

    def clicking_button_register_1(self):
        self.driver.find_element(*self.button_register_1).click()

    def enter_correct_name(self, example_correct_user):
        self.driver.find_element(*self.name_entry_button).send_keys(example_correct_user.name)
        return example_correct_user

    def enter_correct_email_1(self, example_correct_user):
        self.driver.find_element(*self.email_entry_button_1).send_keys(example_correct_user.login)
        return example_correct_user

    def enter_correct_password_1(self, example_correct_user):
        self.driver.find_element(*self.password_entry_button_1).send_keys(example_correct_user.password)
        return example_correct_user

    def enter_correct_email_2(self, example_correct_user):
        self.driver.find_element(*self.email_entry_button_2).send_keys(example_correct_user.login)
        return example_correct_user

    def enter_correct_password_2(self, example_correct_user):
        self.driver.find_element(*self.password_entry_button_2).send_keys(example_correct_user.password)
        return example_correct_user

    def enter_incorrect_name(self, example_not_correct_user):
        self.driver.find_element(*self.name_entry_button).send_keys(example_not_correct_user.name)
        return example_not_correct_user

    def enter_incorrect_email(self, example_not_correct_user):
        self.driver.find_element(*self.email_entry_button_1).send_keys(example_not_correct_user.login)
        return example_not_correct_user

    def enter_incorrect_password(self, example_not_correct_user):
        self.driver.find_element(*self.password_entry_button_1).send_keys(example_not_correct_user.password)
        return example_not_correct_user

    def clicking_button_register_2(self):
        self.driver.find_element(*self.button_register_2).click()

    def clicking_button_login_in_1(self):
        self.driver.find_element(*self.button_login_in_1).click()

    def clicking_button_login_in_2(self):
        self.driver.find_element(*self.button_login_in_2).click()

    def clicking_button_recover_password(self):
        self.driver.find_element(*self.button_recover_password).click()

    def clicking_button_personal_account(self):
        self.driver.find_element(*self.button_personal_account).click()

    def clicking_button_exit(self):
        self.driver.find_element(*self.button_exit).click()

    def clicking_button_designer(self):
        self.driver.find_element(*self.button_designer).click()

    def clicking_button_stellar_burgers(self):
        self.driver.find_element(*self.button_stellar_burgers).click()

    def clicking_button_order_feed(self):
        self.driver.find_element(*self.button_order_feed).click()

    def clicking_button_bread(self):
        self.driver.find_element(*self.button_bread).click()

    def clicking_button_sauce(self):
        self.driver.find_element(*self.button_sauce).click()

    def clicking_button_filling(self):
        self.driver.find_element(*self.button_filling).click()

    def correct_login(self, example_correct_user):
        self.enter_correct_email_2(example_correct_user)
        self.enter_correct_password_2(example_correct_user)
        self.clicking_button_login_in_1()
        return example_correct_user
