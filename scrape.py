from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# options = Options()
# options.add_argument('--headless')

s = Service('/Users/jackiekinsler/projects/scraping_practice/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(service=s)

# driver.get('https://google.com')

driver.get("file:///Users/jackiekinsler/projects/scraping_practice/HTML_example.html")
# print(driver.page_source)

hayden_glacier = driver.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td/table[1]/tbody/tr[13]/td[1]/b")
print(hayden_glacier.text)

driver.quit()


