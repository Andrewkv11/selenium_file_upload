from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "label[class='MuiFormControlLabel-root']")
    ALERT = (By.CSS_SELECTOR, "div[class='MuiAlert-message']")
    LOGOUT_BUTTON = (By.XPATH, "//div[contains(@class, 'MuiToolbar-roo')]//button")


class UploadFilePageLocators:
    UPLOAD_BUTTON = (By.XPATH, "//div[contains(@class, 'MuiGrid-container')]//button")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='upload_file']")
    CREATE_BUTTON = (By.XPATH, "//div[contains(@class, 'MuiDialogActions-root')]//button[2]")
    LAST_FILE_IN_TABLE = (By.XPATH, "//tr[@class='MuiTableRow-root'][1]")
