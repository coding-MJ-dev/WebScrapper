from playwright.sync_api  import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # headless=False 가 되면 실제로 화면을 볼 수 있음 
#headless's default == true

page = browser.new_page()

page.goto('https://www.wanted.co.kr/')
time.sleep(3)

#Aside_searchButton__rajGo라는 class의 button을 누르시오
page.click("button.Aside_searchButton__rajGo")
time.sleep(3)


page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(2)

page.keyboard.down("Enter")
time.sleep(3)

#search_tab_position 를 id로 가진 a를 누르시오
page.click("a#search_tab_position")
time.sleep(3)

# can get the screenshot of a browser
# page.screenshot(path="screenshot.png")

for x in range(5):
  page.keyboard.down("End")
  time.sleep(3)

content = page.content()
p.stop()






