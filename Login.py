import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] = r"os.environ['PATH'] = r"C:\ThePath\You\Put\The\Selenium\Driver""
driver = webdriver.Chrome() 
driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home")
driver.implicitly_wait(5)

uln = driver.find_element_by_id('username')
pln = driver.find_element_by_id('password')

uln.send_keys('YOURUSERNAME')
pln.send_keys('YOURPASSWORD')

chscss=driver.find_element_by_id('submit')
chscss.click()
