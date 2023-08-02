from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    # 創建一個新的 Firefox 瀏覽器實例
    driver = webdriver.Chrome()
    yield driver
    # 測試結束後，關閉瀏覽器
    driver.quit()

def test_login(driver):
    # 讓瀏覽器轉到指定網址
    driver.get("https://wt-live.fb-games-stage.cc/#/")
    time.sleep(2)
    # 找到 "name" 和 "password" 元素並輸入相應的文字
    driver.find_element(By.ID, "username").send_keys("gtest")
    driver.find_element(By.ID, "password").send_keys("Qaz12345")
    # 當 "password" 輸入完成後，模擬按下 Enter 以提交表單
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(2)
    # 驗證登入是否成功，例如，檢查某個特定元素是否出現在頁面上
    print(driver.page_source)
    assert "expected_element" in driver.page_source
