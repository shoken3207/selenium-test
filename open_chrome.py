import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # これを追加

driver_path = 'C:\\webdriver\\chromedriver.exe'

service = Service(driver_path)

driver = webdriver.Chrome(service=service)

driver.get('http://localhost:8080/hotmot/index.jsp')

# メールアドレスとパスワードを入力
email = 'aa@aaaaa'
password = 'aaaaaa'

# メールアドレスの入力フィールドを探して値を入力
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
print(email_field)
email_field.send_keys(email)

# パスワードの入力フィールドを探して値を入力
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)
password_field.send_keys(password)

# ログインボタンをクリック (異なる方法で試す)
try:
    # 方法1: CSSセレクタ
    login_button = driver.find_element(By.ID, 'loginButton')
    print(login_button)
    login_button.click()
    driver.implicitly_wait(10)  # 10秒待つ
    time.sleep(3)
except TimeoutException:
    print("方法1: ログインボタンが見つかりませんでした。")

# element = driver.find_element(By.NAME, 'q')
# element.send_keys('KCS鹿児島情報専門学校')
# element.send_keys(Keys.RETURN)


# element = driver.find_element(By.PARTIAL_LINK_TEXT, 'KCS鹿児島情報専門学校')
# element.send_keys(Keys.RETURN)
# driver.save_screenshot(r'C:\\webdriver\screenshot.png')