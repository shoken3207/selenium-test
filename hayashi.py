import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.login_test import login
login()

# convenienceモジュールのsave_image関数を仮定します。必要に応じて定義またはインポートしてください。
# from convenience import save_image

# WebDriverのパスを指定します
driver_path = 'C:\\webdriver\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get('http://localhost:8080/hotmot/index.jsp')

    # メールアドレスとパスワードを入力
    email = 'aa@aaaaa'
    password = 'aaaaaa'

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

    # ログインボタンをクリック (異なる方法で試す)
    try:
        # 方法1: CSSセレクタ
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'loginButton'))
        )
        login_button.click()
        driver.implicitly_wait(10)  # 10秒待つ
        time.sleep(3)
    except TimeoutException:
        print("方法1: ログインボタンが見つかりませんでした。")
        # ログイン失敗時にスクリーンショットを保存
        driver.save_screenshot('login_failed_screenshot.png')

    # ログイン後の確認 (必要に応じて実装)
    # ... (追加の処理)

except Exception as e:
    print(f"エラーが発生しました: {e}")
    # スクリーンショットを保存
    driver.save_screenshot('error_screenshot.png')


try:
    driver.get('http://localhost:8080/hotmot/index.jsp')

    # ログインボタンをクリック (異なる方法で試す)
    try:
        # 方法1: CSSセレクタ
        btn_register = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.register'))
        )
        btn_register.click()
        driver.implicitly_wait(5)  # 5秒待つ
        time.sleep(3)
    except TimeoutException:
        print("方法1: 新規登録ボタンが見つかりませんでした。")
        # 新規登録失敗時にスクリーンショットを保存
        driver.save_screenshot('btn_register_screenshot.png')

    # メールアドレスとパスワードを入力
    name = '中村大空'
    email = 'bb@bbbb'
    password = 'bbbbbb'
    confirmPassword = 'bbbbbb'

    # 名前の入力フィールドを探して値を入力
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'name'))
    )
    name_field.send_keys(name)

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

    # 確認用パスワードの入力フィールドを探して値を入力
    confirmPassword_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'confirmPassword'))
    )
    confirmPassword_field.send_keys(confirmPassword)

    # ログインボタンをクリック (異なる方法で試す)
    try:
        # Locate the submit button using the input type
        register_button = driver.find_element(By.XPATH,"//div[@class='btn register']/input[@type='submit']")

        #ボタンをクリック
        register_button.click()
        driver.implicitly_wait(3)  # 5秒待つ
        time.sleep(3)
    except TimeoutException:
        print("方法1: 新規登録ボタンが見つかりませんでした。")
        # 新規登録失敗時にスクリーンショットを保存
        driver.save_screenshot('btn_register_screenshot.png')

except Exception as e:
    print(f"エラーが発生しました: {e}")
    # スクリーンショットを保存
    driver.save_screenshot('error_screenshot.png')