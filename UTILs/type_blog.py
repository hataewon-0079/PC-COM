# 크롬을 이용해서 웹사이트에 로그인 한다.

from selenium import webdriver
import time

# 크롬 드라이버 로드
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.naver.com')

# 로그인 버튼 클릭
login_btn = driver.find_element_by_class_name('link_login')
login_btn.click()

# 아이디, 비밀번호 입력
time.sleep(1)
driver.find_element_by_id('id').send_keys('test')
time.sleep(1)
driver.find_element_by_id('pw').send_keys('test')

# 로그인 버튼 클릭
time.sleep(1)
driver.find_element_by_class_name('btn_global').click()

# 웹사이트에서 글쓰기 버튼 클릭
time.sleep(1)
write_btn = driver.find_element_by_class_name('write_btn')


# c:\text.txt 파일어서 내용을 읽어서 웹사이트에 타이핑한다.
# 타이핑 속도는 0.5~0.8초에 한 글자씩 타이핑한다.
# 타이핑이 완료되면 엔터를 친다.

# 글쓰기 버튼 클릭
write_btn.click()
time.sleep(1)

# 파일 읽기
with open('c:\\text.txt', 'r') as file:
    contents = file.read()

# 글쓰기
for content in contents:
    driver.find_element_by_class_name('content').send_keys(content)
    time.sleep(0.5)

# 엔터
driver.find_element_by_class_name('content').send_keys(Keys.RETURN)

# 웹사이트에서 로그아웃 버튼 클릭





