from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_UI.cfg.cfg import *


def test_smp_login_001():

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)

    # get login address
    wd.get(SMP_ADDRESS_LOGIN)

    # enter username and password
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.ID, 'password').send_keys('sdfsdf')

    # click button
    wd.find_element(By.TAG_NAME, 'button').click()

    # check page source change
    nav = wd.find_elements(By.TAG_NAME, 'nav')

    assert nav != []
    wd.quit()
