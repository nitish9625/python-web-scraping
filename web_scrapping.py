from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

company_name = input("Enter a company Name: ")
driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get('https://myco.dica.gov.mm/index.aspx')
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,'//*[@id="EntityCtrl"]/div[2]/div[6]').send_keys('details')
# names= driver.find_element(By.XPATH, '//*[@id="txtCompanyType"]')

# for name in names:
#     print(name.text)
# print(driver.title)
# names = driver.find_element(By.XPATH, '//*[@id="EntityCtrl"]/div[2]/div[6]/div[1]/div[1]')
# print(names.text)
ele = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div/input')
print(ele.is_displayed()) # check the input
print(ele.is_enabled())

ele.send_keys(company_name)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/span/span').click()
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]').click()
driver.find_element_by_tag_name('a').click()

# driver.close() 

# print(driver.title)

# driver.close() # close the browser
