from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

    # Navigate to Url
url = 'https://www.google.com/maps/place/CCE+Saudi/@24.6930292,46.6840505,577m/data=!3m1!1e3!4m6!3m5!1s0x3e2f033918ed0caf:0x47db68871b88a219!8m2!3d24.69302!4d46.6835668!16s%2Fg%2F11cs4yt6wc?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D'

driver.get(url)
time.sleep(5)

title = ''
rating = ''
address = ''
work_times = ''
phone = ''
plus_code = ''
website = ''
sunday_work_times = ''
monday_work_times = ''
tuesday_work_times = ''
wednesday_work_times = ''
thrusday_work_times = ''
friday_work_times = ''
satarday_work_times = ''

try: 
    title = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[2]').text
    rating = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]').text
    address = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div/div[2]/div[1]').text
    work_times = driver.find_elements(By.CSS_SELECTOR, '.G8aQO')
    sunday_work_times = work_times[0].get_attribute('innerHTML')
    monday_work_times = work_times[1].get_attribute('innerHTML')
    tuesday_work_times = work_times[2].get_attribute('innerHTML')
    wednesday_work_times = work_times[3].get_attribute('innerHTML')
    thrusday_work_times = work_times[4].get_attribute('innerHTML')
    friday_work_times = work_times[5].get_attribute('innerHTML')
    satarday_work_times = work_times[6].get_attribute('innerHTML')
    phone = driver.find_element(By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(7) > div:nth-child(6) > button > div > div.rogA2c > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc').text
    plus_code = driver.find_element(By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(7) > div:nth-child(7) > button > div > div.rogA2c > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc').text
    website = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a/div/div[2]/div[1]').text
except NoSuchElementException as e:
    print(e.msg)

print(title)
print(rating)
print(address)
print(sunday_work_times)
print(monday_work_times)
print(tuesday_work_times)
print(wednesday_work_times)
print(thrusday_work_times)
print(friday_work_times)
print(satarday_work_times)
print(phone)
print(plus_code)
print(website)

print('='*50)
driver.quit()  