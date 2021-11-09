from selenium.webdriver.common.by import By


class homePage:
    def __init__(self, driver):
        self.driver = driver

    test = (By.CSS_SELECTOR, "#search-form > div > div.col-md-9.col-sm-6.col-xs-6.pad0 > div > span > button > span")
    makes_homePage = (By.XPATH, "//*[@id='Serverside Quickpicks']/div/div/div[1]/ul/li[1]/a")

    searchBar = (By.XPATH, "//*[@id='input-search']")
    searchButton = (By.XPATH, "//*[@id='search-form']/div/div[1]/div/span/button/span")
    text = ""



    def cleckSearch(self):
        self.driver.find_element(*homePage.test).click()

    def getMakes(self):

        dictionary = {}
        keyToNavigate = ""

        e = self.driver.find_element(*homePage.makes_homePage)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        elements = self.driver.find_elements_by_xpath("//*[@id='tabMakes']/div/span")
        size = len(elements)
        for x in range(size):
            e = self.driver.find_element_by_xpath("//*[@id='tabMakes']/div/span[" + str(x + 1) +"]/span/a")
            make = e.text
            link = e.get_attribute('href')
            #print(make)
            #print(link)
            dictionary[make] = link
            keyToNavigate =  make

        for key, value in dictionary.items():
            print(key, ' : ', value)

        if keyToNavigate in dictionary.keys():
            print(f"Yes, key: '{keyToNavigate}' exists in dictionary")
            self.driver.get(dictionary[keyToNavigate])
            self.driver.implicitly_wait(5)  # seconds
            text = self.driver.find_element_by_xpath("//*[@id='searchResultsHeader']/span").text
            assert keyToNavigate in text
        else:
            print(f"No, key: '{keyToNavigate}' does not exists in dictionary")

    def searchCar(self, car):
        self.driver.find_element(*homePage.searchBar).send_keys(car)
        self.driver.find_element(*homePage.searchButton).click()

    def findIfModelExist(self, carModel):
        elements = self.driver.find_elements_by_xpath("//*[@id='serverSideDataTable']/tbody/tr[3]/td")
        size = len(elements)
        for x in range(size):
            e = self.driver.find_element_by_xpath("//*[@id='serverSideDataTable']/tbody/tr["+str(x + 1)+"]/td[5]/span")
            make = e.text

            if carModel == make:
                assert make == "PORSCHE"
                break
            else:
                print("Model not founded")












