import requests

class Testchallenges():
    def test_challengeOne(self):
        def test_challengeOne(self):
            url = 'https://www.copart.com/public/lotSearchResultsPage'
            myobj = {'query': 'toyota camry'}

            x = requests.post(url, data=myobj)

            print("Test")

            print(x.text)

