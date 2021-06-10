a = 1
b = 2
print(a + b)
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://test-tehang-system-env-3.teyixing.com/login')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//nz-card[@id='login']/div[2]/nz-spin/div/div/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys('111190')
driver.find_element_by_xpath("//nz-card[@id='login']/div[2]/nz-spin/div/div/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys('@12345678')
driver.find_element_by_xpath('//div[@id="login-form-wrapper"]/form/nz-form-item[3]/button').click()
time.sleep(3)
driver.find_element_by_id('_se-1').send_keys("君合")
driver.find_element_by_xpath('//input[@id="_se-1"]/../../../../../se[5]/div[2]/div/span/button[1]').click()
time.sleep(2)
driver.find_element_by_link_text('选择').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@style="float:right;"]/button[2]').click()
time.sleep(5)
driver.quit()

