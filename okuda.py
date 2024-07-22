from utils.login_test import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver_path = 'C:\\webdriver\\chromedriver.exe'
service = Service(driver_path)

email = "aa@aaaaa"
password = "aaaaaa"
driver = webdriver.Chrome(service=service)
driver.get('http://localhost:8080/hotmot/index.jsp')

try:
    # メールアドレスの入力フィールドを探して値を入力
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email_field.send_keys(email)

    # パスワードの入力フィールドを探して値を入力
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys(password)

    # ログインボタンをクリック
    login_button = driver.find_element(By.ID, 'loginButton')
    login_button.click()
    
    driver.implicitly_wait(10)  # 10秒待つ
    time.sleep(3)
    
    print("ログイン成功")
except TimeoutException:
    print("ログインボタンが見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {e}")
try:
    listsAdd_button1 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
    listsAdd_button2 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[2]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
    listsAdd_button3 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[3]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
    listsAdd_button1.click()
    time.sleep(1)
    listsAdd_button2.click()
    time.sleep(1)
    listsAdd_button3.click()
    # bookmark_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[3]//i[contains(@class, "fa-bookmark bookmark-button fa-2x")]')
    # bookmark_button.click()
    # bookmark_button.click()
    driver.save_screenshot(r'C:\\webdriver\screenshot_addBookmark.png')
    print("商品一覧上でブックマーク追加")
    time.sleep(3)

    listsDelete_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
    listsDelete_button.click()
    driver.save_screenshot(r'C:\\webdriver\screenshot_deleteBookmark.png')
    print("商品一覧上でブックマーク削除")
    time.sleep(3)

    detailDelete_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]/a')
    detailDelete_button.click()
    time.sleep(3)

    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="top"])//i')
    bookmark_button.click()
    driver.save_screenshot(r'C:\\webdriver\screenshot_detail_addBookmark.png')
    print("詳細画面上でブックマーク追加")
    time.sleep(3)

    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="top"])//i')
    bookmark_button.click()
    driver.save_screenshot(r'C:\\webdriver\screenshot_detail_deleteBookmark.png')
    print("詳細画面上でブックマーク削除")
    time.sleep(3)
    
    bookmarkList_button = driver.find_element(By.XPATH, '(//div[@class="header-container"])//div[@class="hamburger"]')
    bookmarkList_button.click()
    time.sleep(3)
    bookmarkList_button = driver.find_element(By.XPATH, '(//*[@id="sp"]/nav/ul/li[2]/a)')
    bookmarkList_button.click()
    time.sleep(3)
    deleteBookmarkList_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
    deleteBookmarkList_button.click()
    time.sleep(3)
    driver.refresh()
    driver.save_screenshot(r'C:\\webdriver\screenshot_dispBookmarkList.png')
    print("ブックマーク一覧画面表示")
    time.sleep(3)

    print("ブックマーク登録完了")
except TimeoutException:
    print("ログインボタンが見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    driver.quit()
