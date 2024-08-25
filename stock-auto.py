from selenium import webdriver
from selenium.webdriver.common.by import By


# create Chrome webdriver object
wd = webdriver.Chrome()
wd.implicitly_wait(5)

# open target website by Get method
wd.get('https://www.byhy.net/_files/stock1.html')

# select element by using id='kw'
element = wd.find_element(By.ID, 'kw')

# input content into selected element
element.send_keys('通讯\n')
elements = wd.find_elements(By.ID, '1')

for element in elements:
    print(element.text)

pass
