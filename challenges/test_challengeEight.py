from pageObjects.copartMainPage import homePage
from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeOne(self):
        self.driver.get("https://www.copart.com/")
        copa = homePage(self.driver)
        copa.getMakes()
        #test1.cleckSearch()
        print("Hello world")