
from selenium import webdriver

wait = WebDriverWait(driver, 10)
pagination = driver.find_element(By.XPATH, "//div[contains(text(),'entries')]").text

total_page = int(pagination[pagination.find('of') + 3:pagination.find('entries') - 1:])

driver.execute_