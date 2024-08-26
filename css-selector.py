from selenium import webdriver
from selenium.webdriver.common.by import By


# initialize Chrome and set element waiting time to 5 sec
wd = webdriver.Chrome()
wd.implicitly_wait(5)

# Open target website
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# find element by Webdriver element
element = wd.find_element(By.ID, 'container')

# find element by element.find
spans = element.find_elements(By.ID, 'layer1')