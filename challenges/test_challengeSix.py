from pageObjects.copartMainPage import homePage
from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeSix(self):
        self.driver.get("https://www.copart.com/")
        self.driver.maximize_window()
        copa = homePage(self.driver)
        copa.searchCar("sfdgsfdg")
        copa.tryClickFirstResult()
