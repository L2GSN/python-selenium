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


def test_smp_device_model_001(smp_signed, del_added_devices):

    smp_ui.add_device_model('存储柜', 'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小')

    dms = smp_ui.get_first_device()

    try:
        assert dms == ['存储柜', 'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小']
    except Exception as e:
        print(e)
