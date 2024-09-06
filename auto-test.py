from selenium import webdriver
from selenium.webdriver.common.by import By


# login
def login():
    """login bu=yhySMS"""

    # Find 'username' input box and input 'byhy'
    wd.find_element(By.CSS_SELECTOR, 'input#username').clear()
    wd.find_element(By.CSS_SELECTOR, 'input#username').send_keys('byhy')

    # Find the password input box
    wd.find_element(By.CSS_SELECTOR, 'input#password').clear()
    wd.find_element(By.CSS_SELECTOR, 'input#password').send_keys('88888888')

    # Click '登陆‘ button
    wd.find_element(By.TAG_NAME, 'button').click()


def add_item(islist):
    """add item in to frame"""

    for item in islist:
        # Find the 'input 1'
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input').send_keys(item[0])

        # Find the 'input2'
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input').send_keys(item[1])

        # Find 'input3'
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea').send_keys(item[2])

        # click '创建'
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > div > button:nth-child(1)').click()


# Initialize Chrome object
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://127.0.0.1:80')

# # UI-0001
# # Find the password input frame
# element = wd.find_element(By.CSS_SELECTOR, 'input#password')
#
# # input password=88888888
# element.send_keys('88888888')
#
# # Find the '登陆' button and click
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Judge if the alert text is '请输入用户名'
# alert_text = '请输入用户名'
# if wd.switch_to.alert.text == alert_text:
#     wd.switch_to.alert.accept()
#     print('UI-0001: PASS')
#
# else:
#     print(wd.switch_to.alert.text)
#
# # UI-0002
# # Find 'username' input box and clear content
# element = wd.find_element(By.CSS_SELECTOR, 'input#username')
# element.clear()
#
# element.send_keys('byhy')
#
# # Clear content in password input box
# wd.find_element(By.CSS_SELECTOR, 'input#password').clear()
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Assert if the alert text is '请输入密码'
# alert_text = '请输入密码'
#
# if wd.switch_to.alert.text == alert_text:
#     wd.switch_to.alert.accept()
#     print('UI-0002: PASS')
#
# else:
#     print(wd.switch_to.alert.text)
#
# # UI-0003
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR, 'input#username')
# element.clear()
# element.send_keys('byh')
#
# # Find the password input box
# element = wd.find_element(By.CSS_SELECTOR, 'input#password')
# element.clear()
# element.send_keys('88888888')
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Assert if the alert text is '登录失败 : 用户名或者密码错误'
# alert_text = '登录失败 : 用户名或者密码错误'
#
# if wd.switch_to.alert.text == alert_text:
#     wd.switch_to.alert.accept()
#     print('UI-0003: PASS')
#
# else:
#     print(wd.switch_to.alert.text)
#
# # UI-0004
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR, 'input#username')
# element.clear()
# element.send_keys('byhy')
#
# # Find the password input box
# element = wd.find_element(By.CSS_SELECTOR, 'input#password')
# element.clear()
# element.send_keys('8888888')
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Assert if the alert text is '登录失败 : 用户名或者密码错误'
# alert_text = '登录失败 : 用户名或者密码错误'
#
# if wd.switch_to.alert.text == alert_text:
#     wd.switch_to.alert.accept()
#     print('UI-0004: PASS')
#
# else:
#     print(wd.switch_to.alert.text)
#
# # UI-0005
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR, 'input#username')
# element.clear()
# element.send_keys('byhy')
#
# # Find the password input box
# element = wd.find_element(By.CSS_SELECTOR, 'input#password')
# element.clear()
# element.send_keys('888888888')
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Assert if the alert text is '登录失败 : 用户名或者密码错误'
# alert_text = '登录失败 : 用户名或者密码错误'
#
# if wd.switch_to.alert.text == alert_text:
#     wd.switch_to.alert.accept()
#     print('UI-0005: PASS')
#
# else:
#     print(wd.switch_to.alert.text)

# UI-0101
# login()
# # Find the first 3 items in sidebar
# sidebar = wd.find_elements(By.CSS_SELECTOR, 'ul.sidebar-menu li')
# firs_3 = sidebar[1:4]
# target_list = ['客户', '药品', '订单']
#
# for item in firs_3:
#     print(item.get_attribute('innerText'))
#
# try:
#     assert firs_3 == target_list
#     print('UI-0101: Pass')
#
# except AssertionError:
#     print('UI-0101: Failed')


# # UI-0102
# login()
#
# # Find '添加客户‘ button, and click
# wd.find_element(By.CSS_SELECTOR, 'button > span.glyphicon').click()
#
# # Find the '客户名'
# account_name = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input')
# account_name.click()
# account_name.send_keys('南京中医院')
#
# # Find the '联系电话'
# number = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input')
# number.click()
# number.send_keys('10111112222')
#
# # Find '地址'
# address = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea')
# address.click()
# address.send_keys('南京雨花区长安路88号')
#
# # click '创建'
# wd.find_element(By.CSS_SELECTOR, '.add-one-area > div > button:nth-child(1)').click()
#
# # Add assertion
# try:
#     # Add assertion
#     assert '南京中医院' in wd.page_source
#     print('UI-0102：PASS')
# except AssertionError:
#     print('UI-0102: Failed')
#
# # UI-0103
# login()
#
# # Select search box and click, send keys '南京中医院'
# search_box = wd.find_element(By.CSS_SELECTOR, 'div.input-group > input')
# search_box.click()
# search_box.send_keys('南京中医院\n')
#
#
# # select result-item 1, click '编辑' button
# wd.find_element(By.CSS_SELECTOR, '.search-result-item:nth-of-type(3)  label:nth-child(1)').click()
#
# # change to target text
# target_text = '南京省中医院'
# account_name = wd.find_element(By.CSS_SELECTOR,
#                                '.search-result-item:nth-of-type(3) input[value = "南京中医院"] ')
# account_name.clear()
# account_name.send_keys(target_text)
#
# # click '确定' button
# wd.find_element(By.CSS_SELECTOR,
#                 '.search-result-item:nth-of-type(3)  label[type = "button"]:nth-child(1) ').click()
#
# # Add assertion
# try:
#     # Add assertion
#     assert '南京省中医院' in wd.page_source
#     print('UI-0103：PASS')
# except AssertionError:
#     print('UI-0103: Failed')

# UI-0105
# # Find 'username' input box and input 'byhy'
# username = wd.find_element(By.CSS_SELECTOR, 'input#username')
# username.clear()
# username.send_keys('byhy')
#
# # Find the password input box
# password = wd.find_element(By.CSS_SELECTOR, 'input#password')
# password.clear()
# password.send_keys('88888888')
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # switch to medicine page
# wd.get('http://127.0.0.1/mgr/#/medicines')
#
# # Click '添加药品'
# wd.find_element(By.CSS_SELECTOR, '.col-lg-12 > button').click()
#
# # Find the '药品名称'
# medicine_name = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input')
# medicine_name.click()
# medicine_name.send_keys('测试药品名-青霉素注射液')
#
# # Find the '编号'
# number = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input')
# number.click()
# number.send_keys('Test-QMS02003')
#
# # Find '描述'
# description = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea')
# description.click()
# description.send_keys('测试描述一种光谱抗生素，用于多种炎症反应')
#
# # click '创建'
# wd.find_element(By.CSS_SELECTOR, '.add-one-area > div > button:nth-child(1)').click()
#
# # Assertion
#
# try:
#     # Add assertion
#     assert '测试药品名' in wd.page_source
#     print('UI-0105：PASS')
# except AssertionError:
#     print('UI-0105: Failed')

# # UI-0106
# # Find 'username' input box and input 'byhy'
# username = wd.find_element(By.CSS_SELECTOR, 'input#username')
# username.clear()
# username.send_keys('byhy')
#
# # Find the password input box
# password = wd.find_element(By.CSS_SELECTOR, 'input#password')
# password.clear()
# password.send_keys('88888888')
#
# # Click '登陆‘ button
# wd.find_element(By.TAG_NAME, 'button').click()
#
# # Click jump link
# wd.find_element(By.CSS_SELECTOR, 'footer > div:nth-child(1) > a').click()
#
# # Get current handle
# current = wd.current_window_handle
#
# # Switch to target/teaching website
# for handle in wd.window_handles:
#     # Switch to a window
#     wd.switch_to.window(handle)
#     # grab the title and check if match with target
#     if '月黑' in wd.title:
#         # if true, break
#         break
#
# # Find elements in header
# header = wd.find_elements(By.CSS_SELECTOR, 'nav > nav:nth-child(3) li > a')
#
# # Print text
# # for item in header:
# #     print(item.get_attribute('textContent'))
#
# # Back to byhySMS
# wd.switch_to.window(current)
#
# # Click log out
#
# wd.find_element(By.CSS_SELECTOR, '.dropdown.user').click()
# wd.find_element(By.CSS_SELECTOR, '.user-footer > div.pull-right').click()
#
# log_msg = '输入用户名、密码登录'
#
# try:
#     assert log_msg in wd.page_source
#     print('UI-0106: Pass')
# except AssertionError:
#     print('UI-0106: Failed')

# UI-0107
# login()
#
# # Add medicines
# med_list = [
#     ['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
#     ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
#     ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']
#             ]
#
# # Click '添加药品'
# wd.find_element(By.CSS_SELECTOR, 'a[href = "#/medicines"]').click()
# wd.find_element(By.CSS_SELECTOR, '.col-lg-12 > button').click()
# add_item(med_list)
#
# # Add customers
# cus_list = [
#     ['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
#     ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
#     ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']
#             ]
#
# # Find '添加客户‘ button, and click
# wd.find_element(By.CSS_SELECTOR, 'a[href = "#/customers"]').click()
# wd.find_element(By.CSS_SELECTOR, 'button > span.glyphicon').click()
# add_item(cus_list)
#
# # Add orders
# wd.find_element(By.CSS_SELECTOR, 'a[href = "#/orders"]').click()
#
# # Click '添加订单'
# wd.find_element(By.CSS_SELECTOR, '.col-lg-12 > button').click()
#
# # Find the '订单名称'
# wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input').send_keys('Test-01')
#
# # Find the '客户'
# customer = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input')
# customer.click()
# customer.send_keys('2\n')
# wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) .xxx > option:nth-child(1)').click()
#
#
# # Find '药品'
# medicine = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > input')
# medicine.click()
# medicine.send_keys('1\n')
# wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) .xxx > option:nth-child(1)').click()
#
# # input number of medicine
# number = wd.find_element(By.CSS_SELECTOR, '.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > div> input')
# number.click()
# number.send_keys('100\n')
#
# # Click '创建'
# wd.find_element(By.CSS_SELECTOR, '.add-one-area > div > button:nth-child(1)').click()
#
# # Assertion
# try:
#     assert 'Test-01' in wd.page_source
#     print('UI-0107: Pass')
#
# except AssertionError:
#     print('UI-0107: Failed')

# quit
wd.quit()
