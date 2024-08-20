from selenium import webdriver
from selenium.webdriver.common.by import By


# create Chrome webdriver object
wd = webdriver.Chrome()

# open target website by Get method
wd.get('https://www.byhy.net/_files/stock1.html')

# select element by using id
element = wd.find_element(By.ID, 'kw')

