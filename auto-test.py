from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize Chrome object
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://127.0.0.1')

# UI-0001
# # Find the password input frame
# element = wd.find_element(By.CSS_SELECTOR, 'input#password')
#
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

# UI-0002
# Find 'username' input box and clear content
element = wd.find_element(By.CSS_SELECTOR,'input#username')
element.clear()

element.send_keys('byhy')

# Clear content in password input box
wd.find_element(By.CSS_SELECTOR, 'input#password').clear()

# Click '登陆‘ button
wd.find_element(By.TAG_NAME, 'button').click()

# Judge if the alert text is '请输入密码'
alert_text = '请输入密码'
if wd.switch_to.alert.text == alert_text:
    wd.switch_to.alert.accept()
    print('UI-0002: PASS')

else:
    print(wd.switch_to.alert.text)

# UI-0003
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR,'input#username')
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

# UI-0004
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR,'input#username')
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

# UI-0005
# # Find 'username' input box and input 'byh'
# element = wd.find_element(By.CSS_SELECTOR,'input#username')
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

# UI-0101
# # Find 'username' input box and input 'byh'
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
# # Find sidebar
# sidebar = wd.find_elements(By.CSS_SELECTOR, 'section.sidebar > ul a[href]')
# sidebar_3 = sidebar[:3]
#
# for element in sidebar_3:
#     print(element.get_attribute('innerText'))

pass
