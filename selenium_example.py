from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
username = 'root'
password = 'pwd999'
driver.get(url='https://digapp-test.seal-software.net/')
print(driver.title())
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="button-login"]').click()
print('logged in..')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="button-open-menu"]').click()
time.sleep(2)
driver.find_element_by_xpath('// *[ @ id = "root"] / div[1] / div / div / div / ul[1] / li[9]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/div[1]/div/ul/li[4]/a').click()
time.sleep(2)
for i in range(1,10):
    job = driver.find_element_by_xpath('//*[@id="system-monitoring"]/div/div[2]/div/div[4]/div/table/tbody/tr['+str(i)+']').text
    print(job)
driver.close()
