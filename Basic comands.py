from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://test-origami-1.11.devsotbit.ru/')

driver.maximize_window()


print(driver.title)
print(driver.current_url)

driver.find_element_by_class_name('product-card-inner__title-link').click()

time.sleep(5)

driver.close()

