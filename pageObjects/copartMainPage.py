from selenium.webdriver.common.by import By

class homePage:
    def __init__(self, driver):
        self.driver = driver

    test = (By.CSS_SELECTOR, "#search-form > div > div.col-md-9.col-sm-6.col-xs-6.pad0 > div > span > button > span")
    makes_homePage = (By.XPATH, "//*[@id='Serverside Quickpicks']/div/div/div[1]/ul/li[1]/a")

    searchBar = (By.XPATH, "//*[@id='input-search']")
    searchButton = (By.XPATH, "//*[@id='search-form']/div/div[1]/div/span/button/span")
    popularVehicles = (By.XPATH, "//*[@id='Search Rec Engine']/div/div/div/div/div/recommendation-engine/div/div/div/div/div/h2/span")
    dropdownEntries = (By.XPATH, "//*[@id='serverSideDataTable_length']/label/select")
    onehundredEntries = (By.XPATH, "//*[@id='serverSideDataTable_length']/label/select/option[3]")
    firstResult = (By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[2]/div[1]/a/img")

    def getTotalModel(self,model):
        self.driver.implicitly_wait(1)  # seconds
        self.driver.find_element(*homePage.dropdownEntries).click()
        self.driver.find_element(*homePage.onehundredEntries).click()
        self.driver.implicitly_wait(10)  # seconds
        elements = self.driver.find_elements_by_xpath("//*[@id='serverSideDataTable']/tbody/tr/td[5]/span")
        size = len(elements)
        dictionary = {}
        dictionary2 = {"REAR END":0,"FRONT END":0,"MINOR DENT/SCRATCHES":0,"UNDERCARRIAGE":0,"MISC":0}
        for x in range(99):
            e = self.driver.find_element_by_xpath("//*[@id='serverSideDataTable']/tbody/tr[" + str(x + 1) +"]/td[6]/span")
            make = e.text
            self.driver.execute_script("arguments[0].scrollIntoView();", e)
            if make in dictionary:
                dictionary[make] = dictionary[make] + 1
            else:
                dictionary[make] = 1

            d = self.driver.find_element_by_xpath("//*[@id='serverSideDataTable']/tbody/tr[" + str(x + 1) +"]/td[12]/span")
            damages = d.text
            if damages == "REAR END":
                dictionary2["REAR END"] = dictionary2["REAR END"] + 1
            elif damages == "FRONT END":
                dictionary2["FRONT END"] = dictionary2["FRONT END"] + 1
            elif damages == "MINOR DENT/SCRATCHES":
                dictionary2["MINOR DENT/SCRATCHES"] = dictionary2["MINOR DENT/SCRATCHES"] + 1
            elif damages == "UNDERCARRIAGE":
                dictionary2["UNDERCARRIAGE"] = dictionary2["UNDERCARRIAGE"] + 1
            else:
                dictionary2["MISC"] = dictionary2["MISC"] + 1

        for key, value in dictionary.items():
                print(key, ' : ', value)
        for key, value in dictionary2.items():
            print(key, ' : ', value)


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
        self.driver.implicitly_wait(1)  # seconds
        self.driver.find_element(*homePage.searchBar).send_keys(car)
        self.driver.find_element(*homePage.searchButton).click()
        self.driver.implicitly_wait(1)  # seconds

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

    def getPopularVehicles(self):
        # e = self.driver.find_element(*homePage.popularVehicles)
        # self.driver.execute_script("arguments[0].scrollIntoView();", e)
        y = 1
        dictionary = {}
        for y in range(3):
            elements = self.driver.find_elements_by_xpath("//*[@id='Search Rec Engine']/div/div/div/div/div/recommendation-engine/div/div/div/div/span/span")
            size = len(elements)
            for x in range(size):
                m = self.driver.find_element_by_xpath("//*[@id='Search Rec Engine']/div/div/div/div/div/recommendation-engine/div/div/div/div/span/span["+str(x + 1)+"]/span/div/div[2]/div[1]/div[1]/strong")
                make = m.text
                l = self.driver.find_element_by_xpath("//*[@id='Search Rec Engine']/div/div/div/div/div/recommendation-engine/div/div/div/div/span/span["+str(x + 1)+"]/span/div/div[2]/div[2]/div[1]/a")
                link = l.get_attribute('href')
                print(make + " - " + link)
                dictionary[make] = link
            self.driver.implicitly_wait(1)  # seconds
            nextButton = self.driver.find_element_by_xpath("//*[@id='Search Rec Engine']/div/div/div/div/div/recommendation-engine/div/div/div/div/div/span/span[3]")
            nextButton.click()
        #print(dictionary)

    def tryClickFirstResult(self):
        try:
            self.driver.find_element(*homePage.firstResult).click()
        except Exception as inst:
            self.driver.save_screenshot('ss.png')













