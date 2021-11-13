import requests
from bs4 import BeautifulSoup
from pageObjects.copartMainPage import homePage
from utilities.BaseClass import BaseClass

class Testchallenges(BaseClass):
    def test_challengeEleven(self):
        urlList = self.getUrlsForPage()
        print(urlList)
        for url in urlList:
            self.driver.get(url)
            self.driver.implicitly_wait(5)  # seconds

    def getUrlsForPage(self):
        url = "https://www.copart.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        x = requests.get(url, headers=headers)
        soup = BeautifulSoup(x.text, features="html.parser")
        urlList = []
        for link in soup.find_all('a', {'class': 'menu_click'},href=True):
            href = link.get('href')
            if href.startswith('./'):
                url = href.replace("./", "")
                #print("https://www.copart.com/" + url)
                urlList.append("https://www.copart.com/" + url)
        return urlList

