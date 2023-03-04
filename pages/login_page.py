import time

from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    login = 'start_admin'
    correct_password = 'starter12345'
    incorrect_password = 'incorrect_password'

    def fill_authorization_form(self):
        self.element_is_visible(self.locators.LOGIN_INPUT).send_keys(self.login)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(self.correct_password)

    def fill_authorization_form_incorrect(self):
        self.element_is_visible(self.locators.LOGIN_INPUT).send_keys(self.login)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(self.incorrect_password)

    def submit_authorization(self):
        self.element_is_visible(self.locators.REMEMBER_CHECKBOX).click()
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()

    def get_alert(self):
        return self.element_is_visible(self.locators.ALERT)

    def logout(self):
        self.element_is_clickable(self.locators.LOGOUT_BUTTON).click()

