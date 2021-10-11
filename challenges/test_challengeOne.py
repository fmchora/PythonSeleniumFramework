
import pytest

from Utilities.baseClass import BaseClass
from pageObjects.copartMainPage import homePage


class Testchallenges(BaseClass):
    def test_challengeOne(self):
        self.driver.get("https://www.copart.com/")
        #test1 = homePage(self.driver)
        #test1.cleckSearch()
        print("Hello world")