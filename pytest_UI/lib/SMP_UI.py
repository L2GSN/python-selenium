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


smp_ui = SMP()
