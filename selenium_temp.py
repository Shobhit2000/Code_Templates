from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "D:\codes\gathered_personal\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.kaggle.com")

print(driver.title)

search=driver.find_element(By.CLASS_NAME,"sc-kngDgl.ehkNQC")
search.send_keys(Keys.RETURN)
time.sleep(4) 
search_page=driver.find_element(By.CLASS_NAME,"sc-EmgEd.ehTgdj.searchTarget")
search_page.clear()
search_page.send_keys("database")
search_page.send_keys(Keys.RETURN)
time.sleep(4) 
result_page=driver.find_element

time.sleep(4) 

#link=driver.find_element(By.LINK_TEXT,"Global Terrorism Database")
#linked=element=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.LINK_TEXT,'2'))
#link.click()

#time.sleep(4) 
#driver.quit() #closes the browser


try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"rmwc-icon.rmwc-icon--ligature.google-material-icons.sc-gKXOVf.jWAFrv.sc-keNpes.cRhnBY")))
    element.click()
    #time.sleep(10)
finally:
    driver.close() #closes the tab