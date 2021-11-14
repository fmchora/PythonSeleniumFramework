import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

