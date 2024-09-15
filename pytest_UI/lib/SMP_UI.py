from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_UI.cfg.cfg import *
import time


class SMP:
    """SMP UI Automation initialize object"""

    def __init__(self):
        """Chrome website initial and basic option"""

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
                                        'excludeSwitches',
                                        ['enable-logging'])

        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(5)

    def login(self, username, password):
        """input Username and password to login"""

        # get login address
        self.wd.get(SMP_LOGIN)
        time.sleep(1)

        if username is not None:
            self.wd.find_element(By.ID, 'username').send_keys(username)
        time.sleep(1)

        if password is not None:
            self.wd.find_element(By.ID, 'password').send_keys(password)
        time.sleep(1)

        # click button
        self.wd.find_element(By.TAG_NAME, 'button').click()

    def get_first_device(self):
        time.sleep(1)

        self.wd.implicitly_wait(0)
        values = self.wd.find_elements(By.CSS_SELECTOR, 'field-value')
        self.wd.implicitly_wait(5)

        device_models = []
        for idx, value in enumerate(values):
            if (idx+1) % 3 == 0:
                device_models.append(
                    [values[idx-2].text, values[idx-1].text, values[idx].text])

        return device_models

    def del_first_item(self) -> bool:
        """delete added items, delete the first by default."""

        self.wd.implicitly_wait(0)
        del_btn = self.wd.find_elements(
            By.CSS_SELECTOR, '.result-list-item:first-child > .result-list-item-btn-bar > span:first-child')
        self.wd.implicitly_wait(5)

        if not del_btn:
            return False

        del_btn[0].click()
        self.wd.switch_to.alert.accept()


smp_ui = SMP()
