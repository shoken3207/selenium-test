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

# driver.get('http://localhost:8080/hotmot/ProductListServlet?userId=1')
# print("try前")
try:
    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
    bookmark_button.click()
    driver.save_screenshot(r'C:\Users\st20214139\Desktop\スクショ\screenshot_addBookmark.png')
    print("リスト上でブックマーク追加")
    time.sleep(3)

    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
    bookmark_button.click()
    driver.save_screenshot(r'C:\Users\st20214139\Desktop\スクショ\screenshot_deleteBookmark.png')
    print("リスト上でブックマーク削除")
    time.sleep(3)

    detail_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//a')
    detail_button.click()
    time.sleep(3)

    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="top"])//i')
    bookmark_button.click()
    driver.save_screenshot(r'C:\Users\st20214139\Desktop\スクショ\screenshot_deleteBookmark.png')
    print("詳細画面でブックマーク追加")
    time.sleep(3)

    bookmark_button = driver.find_element(By.XPATH, '(//div[@class="top"])//i')
    bookmark_button.click()
    driver.save_screenshot(r'C:\Users\st20214139\Desktop\スクショ\screenshot_deleteBookmark.png')
    print("詳細画面でブックマーク削除")
    time.sleep(3)
    

    print("ブックマーク登録完了")
except TimeoutException:
    print("ログインボタンが見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    driver.quit()
