from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

# name = '中村大空'
# email = 'bb@bbbb'
# password = 'bbbbbb'
# confirmPassword = 'bbbbbb'
register_user = {
    'name': '中村大空',
    'email': 'bb@bbbb',
    'password': 'bbbbbb',
    'confirmPassword': 'bbbbbb'
}
driver_path = 'C:\\webdriver\\chromedriver.exe'
service = Service(driver_path)


driver = webdriver.Chrome(service=service)
driver.get('http://localhost:8080/hotmot/index.jsp')

def wait_and_send_keys(locator, keys):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    element.send_keys(keys)

def wait_and_click(locator):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()

def select_from_dropdown(xpath, value):
    select_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    select = Select(select_box)
    select.select_by_value(value)

def add_items(tab_index, select_value, add_count):
    tab_xpath = f'(//div[@class="tab"])[{tab_index}]'
    select_xpath = '(//div[@class="list-item show"])[1]/select[@class="select"]'
    add_button_xpath = '(//div[@class="list-item show"])[1]/div[1]/div/button[2]'
    cart_button_xpath = '(//div[@class="list-item show"])[1]/div[2]/div'

    wait_and_click((By.XPATH, tab_xpath))
    time.sleep(1)  # Ensure the page has loaded
    select_from_dropdown(select_xpath, select_value)
    
    for _ in range(add_count):
        wait_and_click((By.XPATH, add_button_xpath))
    
    wait_and_click((By.XPATH, cart_button_xpath))
    time.sleep(1)  # Ensure the action is processed

def update_cart_item(xpath, quantity):
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    input_element.clear()
    input_element.send_keys(quantity)

def main():
    try:
         try:
            # 方法1: CSSセレクタ
            btn_register = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.register'))
            )
            btn_register.click()
            time.sleep(3)
        except TimeoutException:
            print("方法1: 新規登録ボタンが見つかりませんでした。")
        for field_id, text in register_user.items():
            wait_and_send_keys( (By.ID, field_id), text)

        try:
            # Locate the submit button using the input type
            register_button = driver.find_element(By.XPATH,"//div[@class='btn register']/input[@type='submit']")

            #ボタンをクリック
            register_button.click()
            time.sleep(3)
        except TimeoutException:
            print("方法1: 新規登録ボタンが見つかりませんでした。")

        # ログイン処理
        wait_and_send_keys((By.ID, 'email'), register_user['email'])
        wait_and_send_keys((By.ID, 'password'), register_user['password'])
        time.sleep(5)
        wait_and_click((By.ID, 'loginButton'))

        print("ログイン成功")
        time.sleep(1)
        listsAdd_button1 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
        listsAdd_button2 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[2]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
        listsAdd_button3 = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[3]//i[@class="fa-regular fa-bookmark bookmark-button fa-2x"]')
        listsAdd_button1.click()
        time.sleep(1)
        listsAdd_button2.click()
        time.sleep(1)
        listsAdd_button3.click()
        time.sleep(1)
        listsDelete_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
        listsDelete_button.click()
        time.sleep(1)

        productDetailLink = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]/a')
        productDetailLink.click()
        time.sleep(1)

        bookmark_button = driver.find_element(By.XPATH, '(//div[@class="top"])//i')
        bookmark_button.click()
        time.sleep(1)
        # deleteBookmarkList_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
        # deleteBookmarkList_button.click()

        # bookmarkList_button = driver.find_element(By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/a')
        # bookmarkList_button.click()
        bookMarkScreenLink = driver.find_element(By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/a')
        bookMarkScreenLink.click()
        time.sleep(1)
        # driver.get('http://localhost:8080/hotmot/BookMarkServlet?userId=1')
        
        deleteBookMarkIcon = driver.find_element(By.XPATH, '//*[@id="lists"]/div[1]/div/i')
        deleteBookMarkIcon.click()
        time.sleep(1)
        driver.refresh()
        # time.sleep(3)
        # bookmarkList_button = driver.find_element(By.XPATH, '(//*[@id="sp"]/nav/ul/li[2]/a)')
        # bookmarkList_button.click()
        # time.sleep(3)
        # deleteBookmarkList_button = driver.find_element(By.XPATH, '(//div[@class="list-item show"])[1]//i[@class="fa-solid fa-bookmark bookmark-button fa-2x"]')
        # deleteBookmarkList_button.click()
        time.sleep(3)

        driver.get('http://localhost:8080/hotmot/ProductListServlet?userId=1')
        time.sleep(1)
        add_items(1, '2', 2)
        add_items(2, '2', 2)
        add_items(3, '7', 2)
        add_items(4, '7', 2)

        # Add items from tab 1
        wait_and_click((By.XPATH, '(//div[@class="tab"])[1]'))
        time.sleep(1)
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@class="list-item show"])[1]/a'))
        )
        link.click()
        time.sleep(1)
        
        first_add_button_xpath = '(//div[@class="counter-group-child"])[1]//button[@class="add"]'
        second_add_button_xpath = '(//div[@class="counter-group-child"])[2]//button[@class="add"]'
        cart_button_xpath = '//div[@class="cart-button"]'
        
        for _ in range(2):
            wait_and_click((By.XPATH, first_add_button_xpath))
        for _ in range(3):
            wait_and_click((By.XPATH, second_add_button_xpath))
        wait_and_click((By.XPATH, cart_button_xpath))
        time.sleep(2)
        
        driver.get('http://localhost:8080/hotmot/CartDetailListServlet?cartId=1')
        time.sleep(1)
        
        update_cart_item('(//div[@class="cart-detail-list"]//div[@class="box"])[1]//input[@type="number"]', '100')
        update_cart_item('(//div[@class="cart-detail-list"]//div[@class="box"])[2]//input[@type="number"]', '100')

        wait_and_click((By.XPATH, '//button[@id="updateCart"]'))
        time.sleep(3)
        wait_and_click((By.XPATH, '//button[@id="order"]'))
        time.sleep(3)

    except TimeoutException:
        print("タイムアウトエラーが発生しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
