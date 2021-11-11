from pageObjects.copartMainPage import homePage
from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeThree(self):
        self.driver.get("https://www.copart.com/")

        copa = homePage(self.driver)
        copa.getPopularVehicles()

