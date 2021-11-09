import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    # driver = webdriver.Chrome(executable_path="C:\\Users\\Felipe\\PycharmProjects\\pythonSeleniumFramework\\chromedriver.exe")

    driver = webdriver.Chrome(
        executable_path="/Users/felipechora/PycharmProjects/PythonSeleniumFramework/chromedriver")
    request.cls.driver = driver
    yield
    driver.close()

