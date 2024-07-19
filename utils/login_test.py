from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver_path = 'C:\\webdriver\\chromedriver.exe'
service = Service(driver_path)

def login():
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
    # finally:
    #     driver.quit()
