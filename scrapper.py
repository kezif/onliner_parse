from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options



chrome_options = Options()  # get driver
chrome_options.add_argument("--window-size=1820,980") # site is responsive. I want search bar right away
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get('https://www.onliner.by/')

#driver.find_element(By.XPATH, '')
#.get_attribute('outerHTML')
#.screenshot('aa.png')

search = driver.find_element(By.XPATH, '//*[@id="fast-search"]/form/input[1]')  # send querry
search.send_keys('ddr4')


search_frame = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fast-search-modal"]/div/div/iframe'))) 
driver.switch_to.frame(search_frame)  # switch to search result iframe


search_results = driver.find_element(By.XPATH, '//*[@id="search-page"]/div[2]/ul')  # get results

with open('to_parse.html', 'w', encoding='utf-8') as f:
    f.writelines(search_results.get_attribute('outerHTML'))

