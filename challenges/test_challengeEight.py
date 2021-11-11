import requests
import json

class Testchallenges():
    def test_challengeOne(self):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': 'toyota'}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.post(url, data=myobj,headers=headers)
        #print(x.text)
        data = json.loads(x.text)
        total = "returnCode" in data
        print(data['data']['results']['totalElements'])

        assert x.status_code == 200

