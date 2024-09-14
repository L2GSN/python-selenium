import time
import pytest

from selenium.webdriver.common.by import By
from pytest_UI.lib.SMP_UI import SMP

# Create a Chrome object
smp_ui = SMP()


def test_smp_login_001():
    smp_ui.login('byhy', 'sdfsdf')

    nav = smp_ui.wd.find_elements(By.TAG_NAME, 'nav')
    assert nav != []


@pytest.fixture()
def alert_clear():
    yield

    try:
        smp_ui.wd.switch_to.alert.accept()
    except Exception as e:
        print(e)


@pytest.mark.parametrize('username, password, expect', [
        (None, 'sdfsdf', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byhy', 'sdfsdff', '登录失败： 用户名或者密码错误'),
        ('byhy', 'sdfsd', '登录失败： 用户名或者密码错误'),
        ('byh', 'sdfsdf', '登录失败： 用户名不存在'),
        ('byhyy', 'sdfsdf', '登录失败： 用户名不存在'),
    ])
def test_smp_login_002_007(username, password, expect, alert_clear):

    smp_ui.login(username, password)
    time.sleep(1)

    alert = smp_ui.wd.switch_to.alert
    time.sleep(1)

    assert alert.text == expect
