from selenium.webdriver.common.by import By


class homePage:
    def __init__(self, driver):
        self.driver = driver
        test = (By.CSS_SELECTOR, "#search-form > div > div.col-md-9.col-sm-6.col-xs-6.pad0 > div > span > button > span")

    def cleckSearch(self):
        self.driver.find_element(*homePage.test).click()