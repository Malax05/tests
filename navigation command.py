from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://test-origami-1.11.devsotbit.ru/')
def between():
    print(driver.title)
    driver.get('https://vk.com/')
    time.sleep(3)
    print(driver.title)
    driver.back()
    time.sleep(3)
    print(driver.title)
    driver.forward()
    time.sleep(3)
    print(driver.title)
    driver.close()

between()
