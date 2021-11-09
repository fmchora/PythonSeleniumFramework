from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeOne(self):
        self.driver.get("https://www.google.com/")
        title = self.driver.title
        print(title)
        assert "Google" in title
