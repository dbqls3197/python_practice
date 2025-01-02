from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

# 브라우저 꺼짐 방지
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 노출 방지
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
time.sleep(1)

driver.get('https://www.saramin.co.kr/zf_user/?NaPm=ct%3Dm4b3ersg%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3Dnull%7Chk%3D1c48c33f31cf1d91e1ceee91acd12bd0fa94f7ef')
time.sleep(5)

# 검색 실행
such = driver.find_element(By.ID, 'btn_search')
such.click()

such2 = driver.find_element(By.ID, 'ipt_keyword_recruit')
such2.send_keys("파이썬")

such3 = driver.find_element(By.ID, 'ipt_area_recruit')
such3.send_keys(Keys.ENTER)
time.sleep(1)

such4 = driver.find_element(By.ID, 'area_ipt_keyword')
a = input()
such4.send_keys(a)
time.sleep(5)


checkboxs = driver.find_element(By.CSS_SELECTOR, 'ul.list_check li')
time.sleep(1)
checkboxs.click()

such6 = driver.find_element(By.ID, 'btn_search_recruit')
such6.click()

type="checkbox"
job_list = []
current_page = 1  # 현재 페이지 번호를 추적

try:
    while True:
        # 현재 페이지에서 데이터 수집
        items = driver.find_elements(By.CSS_SELECTOR, 'div.item_recruit')
        for item in items:
            title = item.find_element(By.CSS_SELECTOR, "h2.job_tit").text
            company = item.find_element(By.CSS_SELECTOR, "strong.corp_name").text
            job_list.append({'제목': title, '회사': company})

        print(f"{len(job_list)}개의 데이터를 수집했습니다.")

        # 페이지 번호 리스트를 동적으로 가져옴
        page_numbers = driver.find_elements(By.CSS_SELECTOR, 
            '#recruit_info_list > div.content_bottom > div.pagination > a')

        moved = False
        for page in page_numbers:
            page_num = int(page.text) if page.text.isdigit() else None  # 페이지 번호 가져오기
            if page_num and page_num == current_page + 1:  # 다음 페이지 번호 찾기
                ActionChains(driver).move_to_element(page).click(page).perform()
                time.sleep(3)
                current_page = page_num  # 현재 페이지 번호 업데이트
                moved = True
                break

        # 페이지 번호로 이동하지 못하면 "다음" 버튼 클릭
        if not moved:
            try:
                next_button = driver.find_element(By.CSS_SELECTOR,
                    '#recruit_info_list > div.content_bottom > div > a.btnNext.page_move.track_event')
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()
                time.sleep(3)
                current_page += 1  # 다음 페이지로 이동했으므로 번호 증가
            except:
                print("다음 페이지가 없습니다. 크롤링 종료.")
                break

finally:
    driver.quit()

for job in job_list:
    print(job)
