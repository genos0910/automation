from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=10):
    """
    等待網頁元素出現。

    :param driver: WebDriver對象
    :param by: 要查找元素的方式，例如By.ID, By.NAME, By.XPATH等
    :param value: 要查找的元素的值
    :param timeout: 最長等待時間（秒）
    :return: 找到的網頁元素
    """
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    return element

def input_text(driver, by, value, text):
    """
    在指定的網頁元素中輸入文字。

    :param driver: WebDriver對象
    :param by: 要查找元素的方式，例如By.ID, By.NAME, By.XPATH等
    :param value: 要查找的元素的值
    :param text: 要輸入的文字
    """
    element = wait_for_element(driver, by, value)
    element.clear()
    element.send_keys(text)
