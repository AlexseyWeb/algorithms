from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main():
    try:
        html = urlopen('https://pogoda.mail.ru/prognoz/moskva/14dney/')
        bs = BeautifulSoup(html.read(), 'html.parser' )
        nameList = bs.find_all('span', {'class': 'hdr__inner'})
        for name in nameList:
            print(name.get_text())
    except HTTPError as e:
        print("Connecting is refused!")





if __name__ == '__main__':
    main()
