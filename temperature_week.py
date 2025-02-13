from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main():
    try:
        html = urlopen(r'https://www.meteoservice.ru/weather/hourly/moskva')
        bs = BeautifulSoup(html.read(), 'html.parser' )
        text = bs.find('div',{'id':'row-1739368800'}).find('div', {'class':'temperature'}).find('span', {'class':'value'}).text 
        print(f'Сегодня температура в Москве -> {text}')
        
    except HTTPError as e:
        print("Connecting is refused!")





if __name__ == '__main__':
    main()
