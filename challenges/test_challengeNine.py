import requests
import json

class Testchallenges():
    def test_challengeNine(self):
        print(self.validatDataApiRequest("Toyota camry"))

    def validatDataApiRequest(self, car):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': car}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.post(url, data=myobj, headers=headers)
        data = json.loads(x.text)

        dictionary = {}

        totalElementsSTR = data['data']['results']['totalElements']
        if type(totalElementsSTR) == int:
            print("totalElements is a valid int type")
            dictionary["totalElements"] = type(totalElementsSTR)
        else:
            print("totalElements is not a valid int type")

        realTime = data['data']['results']['realTime']
        if type(realTime) == bool:
            print("ln is a valid bool type")
            dictionary["realTime"] = type(realTime)
        else:
            print("ln is not a valid bool type")

        query = data['data']['query']['query']
        if type(query) == list:
            print("ln is a valid list type")
            dictionary["query"] = type(query)
        else:
            print("ln is not a list type")

        return dictionary
