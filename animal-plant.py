from selenium import webdriver
from selenium.webdriver.common.by import By


# initialize Chrome and set element waiting time to 5 sec
wd = webdriver.Chrome()
wd.implicitly_wait(5)

# Open target website
current_window = wd.current_window_handle

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
wd.execute_script("window.open('https://cdn2.byhy.net/files/selenium/sample1.html', '_blank');")

wd.switch_to.window(wd.window_handles[1])

# find element by css selector / search id = container
elements = wd.find_elements(By.CSS_SELECTOR, '#container')

for element in elements:
    print(element.get_attribute('outerHTML'))


wd.quit()