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
    print('\n** Delete all items **\n')
    smp_ui.del_all_items()

    yield
    print('\n** Delete added device model **\n')
    smp_ui.del_first_device()


@pytest.mark.parametrize('d_type, d_model, d_desc', [
    ('存储柜', 'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小'),
    ('存储柜', '字'*100, '南京e生活存储柜-10大20中40小'),
    ('电瓶车充电站', 'bokpower-charger-g22-220v450w', '杭州bok 2022款450瓦 电瓶车充电站'),
    ('洗车站', 'njcw-carwasher-g22-2s', '南京e生活2022款洗车机 2个洗车位'),
    ('汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站'),
])
def test_smp_device_model_001_301(d_type, d_model, d_desc, smp_signed, del_added_devices):

    smp_ui.add_device_model(d_type, d_model, d_desc)

    dms = smp_ui.get_first_device()

    try:
        assert dms == [d_type, d_model, d_desc]
    except Exception as e:
        print(e)


@pytest.fixture()
def exist_charger():
    print('\n** delete all items, then add a charger station **\n')
    smp_ui.del_all_items()
    smp_ui.add_device_model('电瓶车充电站', 'bokpower-charger-g22-220v450w', '杭州bok 2022款450瓦 电瓶车充电站')
    time.sleep(0.1)

    yield

    print('\n** delete the just added item **\n')
    smp_ui.del_first_device()


def test_smp_device_model_501(smp_signed, exist_charger):

    modify = smp_ui.wd.find_element(By.CSS_SELECTOR, '.result-list-item:first-child .btn-no-border:nth-child(2)')

    if modify.text == '修改':
        modify.click()

    ele = smp_ui.wd.find_element(By.CSS_SELECTOR, '.result-list-item .field:nth-child(2) >.input-xl:nth-child(2)')
    ele.clear()
    ele.send_keys('Test, update model')

    ele = smp_ui.wd.find_element(By.CSS_SELECTOR, '.result-list-item .field:nth-child(3) >.input-xl:nth-child(2)')
    ele.clear()
    ele.send_keys('Test, update description')

    smp_ui.wd.find_element(By.CSS_SELECTOR, '.result-list-item:first-child .btn-no-border:nth-child(1)').click()

    update = smp_ui.get_first_device()

    try:
        assert update == ['电瓶车充电站', 'Test, update description', 'Test, update model']
    except Exception as e:
        print(e)


def test_smp_device_model_601(smp_signed, exist_charger):

    btn_del = smp_ui.wd.find_element(By.CSS_SELECTOR, '.result-list-item:first-child .btn-no-border:nth-child(2)')

    if btn_del.text == '删除':
        btn_del.click()
        smp_ui.wd.switch_to.alert.accept()

    update = smp_ui.get_first_device()

    try:
        assert update == []
    except Exception as e:
        print(e)
