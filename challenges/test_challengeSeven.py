from pageObjects.copartMainPage import homePage
from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeSeven(self):
        self.driver.get("https://www.copart.com/")
        copa = homePage(self.driver)
        copa.getMakes()
        #test1.cleckSearch()
        print("Hello world")

        # This one looks a bit off to me.
        # Line 9 has something that seems to be leftover from troubleshooting possibly.
        # If this is no longer needed lets remove it.
        # I see that it prints the Make and URL associated this looks good.
        # It then does an assert on only one entry, from what I can see, in the Dictionary and prints that one.
        # I believe one of the challenge requirements is to verify all the elements go to the correct URL.
        # The extra Hello World could be taken out but is really fine.
        # If you have time to look at this and get a fix in before we meet that would be great.
