import sys
sys.path.append('/Users/genosho/Documents/automation')
import pytest
from selenium import webdriver
from pages.google_search_page import GoogleSearchPage


@pytest.fixture
def browser():
    # 初始化 WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # 測試結束後關閉瀏覽器
    driver.quit()

def test_google_search(browser):
    # 使用 Page Object 來進行測試
    search_page = GoogleSearchPage(browser)
    search_page.load()

    search_page.search('OpenAI')

    # 確認結果
    assert 'OpenAI' in browser.page_source
