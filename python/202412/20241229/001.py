from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import pyperclip
import webbrowser

chrome_options = Options()

# 브라우저 꺼짐 방지
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 노출 방지
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
time.sleep(1)

driver.get('https://tickets.interpark.com/contents/genre/concert')
time.sleep(5)

such = driver.find_element(By.ID, 'SubCategory_btnCategory__i_55b')
such.send_keys(Keys.ENTER)
time.sleep(1)

concert = []



items = driver.find_elements(By.CSS_SELECTOR, 'a.link')
for item in items:
    title = item.find_element(By.CSS_SELECTOR, "li.TicketItem_goodsName__Ju76j").text
    location = item.find_element(By.CSS_SELECTOR, "li.TicketItem_placeName__ls_9C").text
    date = item.find_element(By.CSS_SELECTOR, "li.TicketItem_playDate__5ePr2").text
    
    concert.append({'제목': title, '위치': location, '날짜':date})
for c in concert:
    print(c)
    
driver.quit()