import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Felipe\\PycharmProjects\\pythonSeleniumFramework\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.close()

