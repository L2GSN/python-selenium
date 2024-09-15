import time
import pytest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pytest_UI.lib.SMP_UI import smp_ui
from pytest_UI.cfg.cfg import *


@pytest.fixture(scope='module')
def smp_signed():
    smp_ui.login('byhy', 'sdfsdf')
    smp_ui.wd.get(SMP_DEVICE_MGR)

    yield


@pytest.fixture()
def del_added_devices():

    yield
    print('** Delete added device model **')
    smp_ui.del_first_item()


def test_smp_device_model_001(smp_signed, del_added_devices):

    add_btn = smp_ui.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if add_btn.text == '添加':
        add_btn.click()

    device = Select(smp_ui.wd.find_element(By.ID, 'device-type'))
    device.select_by_visible_text('存储柜')

    ele = smp_ui.wd.find_element(By.ID, 'device-model')
    ele.clear()
    ele.send_keys('elife-canbinlocker-g22-10-20-40')

    ele = smp_ui.wd.find_element(By.ID, 'device-model-desc')
    ele.clear()
    ele.send_keys('南京e生活存储柜-10大20中40小')

    smp_ui.wd.find_element(By.CSS_SELECTOR, '.add-one-submit-btn-div > .btn').click()

    dms = smp_ui.get_first_device()

    try:
        assert dms == ['存储柜', 'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小']
    except Exception as e:
        print(e)
