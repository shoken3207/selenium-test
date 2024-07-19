
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
driver_path = 'C:\\webdriver\\chromedriver.exe'
service = Service(driver_path)

email = "aa@aaaaa"
password = "aaaaaa"
driver = webdriver.Chrome(service=service)
driver.get('http://localhost:8080/hotmot/index.jsp')

try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email_field.send_keys(email)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, 'loginButton')
    login_button.click()
    
    time.sleep(1)
    
    print("ログイン成功")
except TimeoutException:
    print("ログインボタンが見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {e}")

tab1 =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="tab"])[1]'))
)
tab1.click()
time.sleep(1)
select_box1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[2]/select[@class="select"]'))
)
select1 = Select(select_box1)
select1.select_by_value('2')
add_button1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[1]/div/button[2]'))
)
for _ in range(2):
    add_button1.click()
cart_button1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[2]/div'))
)
cart_button1.click()
time.sleep(1)


tab2 =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="tab"])[2]'))
)
tab2.click()
time.sleep(1)
select_box2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/select[@class="select"]'))
)
select2 = Select(select_box2)
select2.select_by_value('2')
add_button2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[1]/div/button[2]'))
)
for _ in range(2):
    add_button2.click()
cart_button2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[2]/div'))
)
cart_button2.click()
time.sleep(1)



tab3 =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="tab"])[3]'))
)
tab3.click()
time.sleep(1)
select_box3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/select[@class="select"]'))
)
select3 = Select(select_box3)
select3.select_by_value('7')
add_button3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[1]/div/button[2]'))
)
for _ in range(2):
    add_button3.click()
cart_button3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[2]/div'))
)
cart_button3.click()
time.sleep(1)

tab4 =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="tab"])[4]'))
)
tab4.click()
time.sleep(1)
select_box4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/select[@class="select"]'))
)
select4 = Select(select_box4)
select4.select_by_value('7')
add_button4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[1]/div/button[2]'))
)
for _ in range(2):
    add_button4.click()
cart_button4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/div[2]/div'))
)
cart_button4.click()


tab5 =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="tab"])[1]'))
)
tab5.click()
time.sleep(1)

link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/a'))
)
link.click()
time.sleep(1)
first_add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="counter-group-child"])[1]//button[@class="add"]'))
)
for _ in range(2):
    first_add_button.click()

second_add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class="counter-group-child"])[2]//button[@class="add"]'))
)
for _ in range(3):
    second_add_button.click()
time.sleep(1)
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="cart-button"]'))
)
cart_button.click()
time.sleep(2)
driver.get('http://localhost:8080/hotmot/CartDetailListServlet?cartId=1')
time.sleep(1)
first_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//div[@class="cart-detail-list"]//div[@class="box"])[1]//input[@type="number"]'))
)
first_input.clear() 
first_input.send_keys('100')  

second_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//div[@class="cart-detail-list"]//div[@class="box"])[2]//input[@type="number"]'))
)
second_input.clear()  # 既存の値をクリア
second_input.send_keys('100')  # 新しい値を入力
time.sleep(1)
update_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@id="updateCart"]'))
)
update_cart_button.click()
time.sleep(3)
order_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@id="order"]'))
)
order_button.click()
time.sleep(3)