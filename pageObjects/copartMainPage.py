from selenium.webdriver.common.by import By


class homePage:
    def __init__(self, driver):
        self.driver = driver

    test = (By.CSS_SELECTOR, "#search-form > div > div.col-md-9.col-sm-6.col-xs-6.pad0 > div > span > button > span")
    makes_homePage = (By.XPATH, "//*[@id='Serverside Quickpicks']/div/div/div[1]/ul/li[1]/a")

    def cleckSearch(self):
        self.driver.find_element(*homePage.test).click()

    def getMakes(self):
        e = self.driver.find_element(*homePage.makes_homePage)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        elements = self.driver.find_elements_by_xpath("//*[@id='tabMakes']/div/span")
        size = len(elements)
        for x in range(size):
            text = self.driver.find_element_by_xpath("//*[@id='tabMakes']/div/span[" + str(x + 1) +"]/span/a").text
            e = self.driver.find_element_by_xpath("//*[@id='tabMakes']/div/span[" + str(x + 1) + "]/span/a")
            link = e.get_attribute('href')
            print(text)
            print(link)


