from selenium import webdriver
from selenium.webdriver.common.by import By


# create Chrome webdriver object
wd = webdriver.Chrome()
wd.implicitly_wait(5)

# open target website by Get method
wd.get('https://www.byhy.net/_files/stock1.html')

# select element by id='kw'
element = wd.find_element(By.ID, 'kw')

# input content into selected element
element.send_keys('通讯\n')

# clear input frame and input '科技'
element.clear()
element.send_keys('科技\n')

# select the first result
element = wd.find_element(By.ID, '1')

# print the text and attribute
print(element.text)
print(element.get_attribute('class'))

pass

wd.quit()