import requests

class Testchallenges():
    def test_challengeOne(self):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': 'toyota'}

        x = requests.post(url, data=myobj)
        print(x.text)
        assert x.status_code == 200

