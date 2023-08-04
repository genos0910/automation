import pytest
from py._xmlgen import html
from selenium import webdriver

# 啟動和關閉 Selenium WebDriver
@pytest.fixture(scope="session")
def driver():
    print("\nstart  browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit  browser..")
    driver.quit()

# 資料庫連接：你可以創建一個 fixture 來管理資料庫連接。例如，你可以在測試開始時建立連接，並在測試結束時關閉連接。這也有助於在每次測試之前清理和重置資料庫。
# import mydatabase

# @pytest.fixture(scope="module")
# def db():
#     print("setup database connection")
#     db = mydatabase.connect()
#     yield db
#     print("close database connection")
#     db.close()


# 網站用戶：如果你的網站需要使用者登錄，你可能需要一個 fixture 來創建和管理用戶會話。例如，你可以在測試開始時登錄用戶，並在測試結束時退出登錄。
# import mywebsite

# @pytest.fixture(scope="module")
# def user():
#     print("log in user")
#     user = mywebsite.login(username="test", password="test")
#     yield user
#     print("log out user")
#     mywebsite.logout(user)

# 文件或資源：如果你的測試需要訪問文件或其他資源（如圖片、PDF文件等），你可以創建一個 fixture 來管理這些資源。例如，你可以在測試開始時打開文件，並在測試結束時關閉文件。

@pytest.fixture(scope="module")
def open_file():
    print("open file")
    file = open("test_file.txt")
    yield file
    print("close file")
    file.close()

# 測試數據：如果你有一些測試案例共享的數據，你可以將這些數據放在一個 fixture 中。這樣，你可以避免在每個測試案例中重複這些數據。


@pytest.fixture(scope="module")
def test_data():
    return {"username": "test", "password": "test"}





@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    getattr(report, 'extra', [])
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解決亂碼
