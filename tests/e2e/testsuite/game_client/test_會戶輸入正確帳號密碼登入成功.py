# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    userAccount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/form[1]/input[1]"))
    )
    userAccount.send_keys("gtest")

    pwd = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/form[1]/input[2]"))
    )
    pwd.send_keys("Qaz12345")
    # 確認密碼已填入
    assert pwd.get_attribute('value') == 'Qaz12345'

    time.sleep(1)
    btn_submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".l-button"))
    )
    
    # 當 "password" 輸入完成後，模擬按下 Enter 以提交表單
    btn_submit.click()
    # 驗證登入是否成功，例如，檢查某個特定元素是否出現在頁面上
    
    assert "balance text-white" in driver.page_source

    driver.quit()

