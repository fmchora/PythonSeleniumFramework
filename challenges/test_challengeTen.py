import requests
import json

class Testchallenges():
    def test_challengeEight(self):
        excel_data_df = pandas.read_excel('test10.xlsx')
        columns = excel_data_df.columns.size
        rows = excel_data_df.index.size
        dictionary = {}

        for y in range(rows):
            words = ""
            test = excel_data_df.iloc[y].tolist()
            for x in test:
                if x == x:
                    words = words + " "+ str(x)
            dictionary[y] = words
            words = ""

        for key, value in dictionary.items():
            self.getTotalCarsInStock(value)


    def getTotalCarsInStock(self, car):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': car}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.post(url, data=myobj, headers=headers)
        data = json.loads(x.text)
        print("{}, {}".format(car,data['data']['results']['totalElements']))
        self.validatDataApiRequest(car)
        return ("{}, {}".format(car,data['data']['results']['totalElements']))

    def validatDataApiRequest(self, car):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': car}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.post(url, data=myobj, headers=headers)
        data = json.loads(x.text)

        dictionary = {}

        totalElementsSTR = data['data']['results']['totalElements']
        assert type(totalElementsSTR) == int
        if type(totalElementsSTR) == int:
            print("totalElements is a valid int type")
            dictionary["totalElements"] = type(totalElementsSTR)
        else:
            print("totalElements is not a valid int type")

        realTime = data['data']['results']['realTime']
        assert type(realTime) == bool
        if type(realTime) == bool:
            print("ln is a valid bool type")
            dictionary["realTime"] = type(realTime)
        else:
            print("ln is not a valid bool type")

        query = data['data']['query']['query']
        assert type(query) == list
        if type(query) == list:
            print("ln is a valid list type")
            dictionary["query"] = type(query)
        else:
            print("ln is not a list type")

        return dictionary