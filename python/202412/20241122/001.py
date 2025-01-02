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

a = pyautogui.prompt('아이디를 입력하세요')

b = pyautogui.password('비밀번호를 입력하세요:')

c = pyautogui.prompt('이메일을 입력해주세요:')

d = pyautogui.confirm('어떤 메일을 보내시겠습니까?',
    buttons=['가입안내','합격안내','계약서']
)
toname = '손유빈'
if d =='가입안내':
    to_subject = '[테스트] 가입안내입니다.'
    to_content =  f'{toname}님 가입을 환영합니다.\n\n최고의 서비스로 최선을 다하겠습니다. \n\n 감사합니다.'
elif d =='합격안내':
    to_subject = '[테스트] 합격결과입니다.'
    to_content =  f'''{toname}님 이번 면접에 최종 합격 하였습니다. \n
저희 가족이 되심을 축하합니다.
입사일은 2025년 5월 1일 입니다.\n
감사합니다.'''
elif d =='계약서':
    to_subject = '[테스트] 점심 계약서.'
    to_content = f'''{toname}님 최종 계약서 내용입니다.\n
    귀하는 2024년 12월 4일 ~ 2025년 4월 24일까지 점심을 사기로 하였습니다.\n
    # 계약자 A:{toname}
    # 계약자 B:이순신'''
    


driver = webdriver.Chrome(options = chrome_options)

time.sleep(2)
#driver.imlicitly_wait(5)

driver.maximize_window()

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')
id = driver.find_element(By.CSS_SELECTOR,"#id")
id.click()
pyperclip.copy(a)
pyautogui.hotkey('ctrl','v')

time.sleep(1)

pw = driver.find_element(By.CSS_SELECTOR,'#pw')
pw.click()
pyperclip.copy(b)
pyautogui.hotkey('ctrl','v')

time.sleep(1)

login_btn = driver.find_element(By.CSS_SELECTOR,'span.btn_text')
login_btn.click()

time.sleep(10)

maile = driver.find_element(By.CSS_SELECTOR,'a.link_service')
maile.click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])

time.sleep(2)

maile_write = driver.find_element(By.CSS_SELECTOR,'.item.button_write')
maile_write.click()

time.sleep(3)
user = driver.find_element(By.CSS_SELECTOR,'div.user_list')
pyperclip.copy(c)
pyautogui.hotkey('ctrl','v')

time.sleep(3)
title = driver.find_element(By.CSS_SELECTOR,'#subject_title')
title.click()
pyperclip.copy(to_subject)
pyautogui.hotkey('ctrl','v')

time.sleep(3)
# iframe 창으로 전환
iframe = driver.find_element(By.CSS_SELECTOR,"#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)

time.sleep(2)

mail_content = driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content")
mail_content.click()
pyperclip.copy(to_content)
pyautogui.hotkey('ctrl','v')


time.sleep(2)

driver.switch_to.default_content()

mail_content = driver.find_element(By.CSS_SELECTOR,'#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task')
#mail_content.click()