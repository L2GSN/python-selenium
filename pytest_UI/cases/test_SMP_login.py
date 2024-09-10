from selenium.webdriver.common.by import By
from pytest_UI.lib.SMP_UI import SMP


def test_smp_login_001():

    smp_ui = SMP()
    smp_ui.login('byhy', 'sdfsdf')

    nav = smp_ui.wd. find_elements(By. TAG_NAME, 'nav')
    assert nav != []




