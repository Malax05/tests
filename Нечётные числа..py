from  selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://test-origami-1.11.devsotbit.ru/')
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]').click()
driver.find_element_by_id('13'). send_keys('Александр')
driver.find_element_by_id('numberFEEDBACK').send_keys('+375298055976')
driver.find_element_by_name('form_email_15').send_keys("toretto245@mail.ru")
driver.find_element_by_xpath("//div[@class='popup-window-submit_button']//input[1]").click()

driver.close()