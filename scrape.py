from selenium import webdriver

DRIVER_PATH = '/Users/jackiekinsler/projects/scraping_practice/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')