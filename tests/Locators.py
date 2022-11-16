from selenium.webdriver.common.by import By
import pytest

class Locators:

    button_login_in_account = [By.XPATH, './/button']  # Кнопка "Войти в аккаунт"
    button_register_1 = [By.XPATH, ".//a[text()='Зарегистрироваться']"]  # Кнопка "Зарегистрироваться" № 1
    name_entry_button = [By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[1]"]  # Кнопка ввода "Имени"
    email_entry_button = [By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[2]"]  # Кнопка ввода "email"
    password_entry_button = [By.XPATH, "(//*[@class='text input__textfield text_type_main-default'])[3]"]  # Кнопка ввода "Пароля"
    button_register_2 = [By.XPATH, ".//button[text()='Зарегистрироваться']"]  # Кнопка "Зарегистрироваться" № 2
    button_login_in = [By.XPATH, "//button[text()='Войти']"]  # Кнопка "Войти"
    button_personal_account = [By.XPATH, ".// p[text() = 'Личный Кабинет']"]  # Кнопка "Личный кабинет"
    button_profile = [By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]  # Кнопка "Профиль"

    def __init__(self, driver):
        self.driver = driver

    def going_to_the_website(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def clicking_button_login_in_account(self):
        self.driver.find_element(*self.button_login_in_account).click()

    def clicking_button_register_1(self):
        self.driver.find_element(*self.button_register_1).click()

    def enter_correct_name(self, example_correct_user):
        self.driver.find_element(*self.name_entry_button).send_keys(example_correct_user.name)

    def enter_correct_email(self, example_correct_user):
        self.driver.find_element(*self.email_entry_button).send_keys(example_correct_user.login)

    def enter_correct_password(self, example_correct_user):
        self.driver.find_element(*self.password_entry_button).send_keys(example_correct_user.password)

    def clicking_button_register_2(self):
        self.driver.find_element(*self.button_register_2).click()

    def clicking_button_login_in(self):
        self.driver.find_element(*self.button_login_in).click()

    def clicking_button_personal_account(self):
        self.driver.find_element(*self.button_personal_account).click()

    def clicking_button_profile(self):
        self.driver.find_element(*self.button_profile).click()

    @pytest.mark.usefixtures("example_correct_user", "example_not_correct_user")
    def correct_registration(self, example_correct_user):
        self.going_to_the_website()
        self.clicking_button_login_in_account()
        self.clicking_button_register_1()
        self.enter_correct_name(example_correct_user)
        self.enter_correct_email(example_correct_user)
        self.enter_correct_password(example_correct_user)
        self.clicking_button_register_2()
        self.clicking_button_login_in()
        return

    @pytest.mark.usefixtures("example_correct_user", "example_not_correct_user")
    def correct_login(self, example_correct_user):
        self.enter_correct_email(example_correct_user)
        self.enter_correct_password(example_correct_user)
        self.clicking_button_login_in()