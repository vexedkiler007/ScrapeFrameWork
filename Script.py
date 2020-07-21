import Sources
import Save
import Scrape
from bs4 import BeautifulSoup
import os

url_y = "https://www.google.com/"


@Scrape.async_request_scrape(url_y, Sources.AioHttpSource, Save.TextSaver)
def scrape(source: str) -> Save.TextSaver.TextSaverData:
    bytes_ = bytes(source, 'utf-8')
    return Save.TextSaver.TextSaverData(bytes_, 'cool')


@Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.ImageSaver)
def scrapeImages(source: str) -> Save.ImageSaver.ImageSaverData:
    soup = BeautifulSoup(source, 'html.parser')
    container = soup.find(class_="rpBJOHq2PR60pnwJlUyP0")
    link_list = []
    file_list = []
    for img in container.find_all('img'):
        endings = ['jpg', 'png']
        try:
            link = img['src']
            file_name = os.path.basename(link)
            file_name_list = file_name.split('.')
            if file_name_list[-1] not in endings:
                if 'png' in file_name_list[-1]:
                    file_name_list[-1] = '.png'
                    file_name = "".join(file_name_list)
                if 'jpg' in file_name_list[-1]:
                    file_name_list[-1] = '.jpg'
                    file_name = "".join(file_name_list)
            link_list.append(link)
            file_list.append(file_name)

        except KeyError as e:
            print(str(e) + " image")

    return Save.ImageSaver.ImageSaverData(link_list, file_list)

@Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.ImageSaver)
def scrapeImagess(source: str) -> Save.ImageSaver.ImageSaverData:
    soup = BeautifulSoup(source, 'html.parser')
    container = soup.find(class_="rpBJOHq2PR60pnwJlUyP0")
    link_list = []
    file_list = []
    for img in container.find_all('img'):
        endings = ['jpg', 'png']
        try:
            link = img['src']
            file_name = os.path.basename(link)
            file_name_list = file_name.split('.')
            if file_name_list[-1] not in endings:
                if 'png' in file_name_list[-1]:
                    file_name_list[-1] = '.png'
                    file_name = "".join(file_name_list)
                if 'jpg' in file_name_list[-1]:
                    file_name_list[-1] = '.jpg'
                    file_name = "".join(file_name_list)
            link_list.append(link)
            file_list.append(file_name+"1")

        except KeyError as e:
            print(str(e) + " image")

    return Save.ImageSaver.ImageSaverData(link_list, file_list)

Scrape.run()
