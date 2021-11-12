import requests
import json

class Testchallenges():
    def test_challengeEight(self):
        with open('CarInStock.txt', 'w') as file:
            file.write(self.getTotalCarsInStock("Toyota camry") + "\n")
            file.write(self.getTotalCarsInStock("Toyota camry")+ "\n")
            file.write(self.getTotalCarsInStock("Challenger")+ "\n")
            file.write(self.getTotalCarsInStock("camaro")+ "\n")
            file.write(self.getTotalCarsInStock("Ram")+ "\n")
            file.write(self.getTotalCarsInStock("CADILLAC ESCALADE")+ "\n")
            file.write(self.getTotalCarsInStock("4Runner")+ "\n")
            file.write(self.getTotalCarsInStock("JEEP GRAND CHEROKEE")+ "\n")
            file.write(self.getTotalCarsInStock("370z")+ "\n")
            file.write(self.getTotalCarsInStock("Corvette")+ "\n")
            file.write(self.getTotalCarsInStock("Mustang")+ "\n")


    def getTotalCarsInStock(self, car):
        url = "https://www.copart.com/public/lots/search"
        myobj = {'query': car}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.post(url, data=myobj, headers=headers)
        data = json.loads(x.text)
        print("{}, {}".format(car,data['data']['results']['totalElements']))
        return ("{}, {}".format(car,data['data']['results']['totalElements']))