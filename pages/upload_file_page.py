import os
import random
import time

from locators.locators import UploadFilePageLocators
from pages.base_page import BasePage


class UploadFilePage(BasePage):
    locators = UploadFilePageLocators()

    @staticmethod
    def create_file():
        file_name = f'filetest{random.randint(0, 999)}'
        file_extension = 'txt'
        path = f'{os.getcwd()}/{file_name}.{file_extension}'
        file = open(path, 'w+')
        file.write(f'Test file text {random.randint(0, 999)}')
        file.close()
        return file_name, file_extension, path

    def upload_file(self):
        self.element_is_clickable(self.locators.UPLOAD_BUTTON).click()
        file_name, file_extension, path = self.create_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        self.element_is_clickable(self.locators.CREATE_BUTTON).click()
        os.remove(path)
        return file_name, file_extension

    def parse_files_from_table(self):
        self.refresh()
        last_file_in_table = self.element_is_visible(self.locators.LAST_FILE_IN_TABLE).text
        return last_file_in_table.split()[1], last_file_in_table.split()[2]

