from sqlalchemy import MetaData, create_engine, Column, Integer, String
import Sources
import Save
import Scrape
from bs4 import BeautifulSoup
import os

# urls = ["http://127.0.0.1:5000/static/test.html","http://127.0.0.1:5000/static/test.html","http://127.0.0.1:5000/static/test.html"]
# for url in urls:
#     @Scrape.async_request_scrape(url, Sources.AioHttpSource, Save.TextSaver)
#     def scrape(source: str, proxy: Sources.Proxy) -> Save.TextSaver.TextSaverData:
#         bytes_ = bytes(source, 'utf-8')
#         return Save.TextSaver.TextSaverData(bytes_, 'cool')
#
# urls = ["http://127.0.0.1:5000/static/test.html","http://127.0.0.1:5000/static/test.html","http://127.0.0.1:5000/static/test.html"]
# for url in urls:
#     @Scrape.async_request_scrape(url, Sources.AioHttpSource, Save.ImageVideoSaver)
#     def scrapeImages(source: str) -> Save.ImageVideoSaver.ImageVideoSaverData:
#         soup = BeautifulSoup(source, 'html.parser')
#         container = soup.find(class_="rpBJOHq2PR60pnwJlUyP0")
#         link_list = []
#         file_list = []
#         for img in container.find_all('img'):
#             endings = ['jpg', 'png']
#             try:
#                 link = img['src']
#                 file_name = os.path.basename(link)
#                 file_name_list = file_name.split('.')
#                 if file_name_list[-1] not in endings:
#                     if 'png' in file_name_list[-1]:
#                         file_name_list[-1] = '.png'
#                         file_name = "".join(file_name_list)
#                     if 'jpg' in file_name_list[-1]:
#                         file_name_list[-1] = '.jpg'
#                         file_name = "".join(file_name_list)
#                 link_list.append(link)
#                 file_list.append(file_name)
#
#             except KeyError as e:
#                 print(str(e) + " image")
#
#         return Save.ImageVideoSaver.ImageVideoSaverData(link_list, file_list)



urls = ["http://127.0.0.1:5000/static/test.html",
        "http://127.0.0.1:5000/static/test.html",
        "http://127.0.0.1:5000/static/test.html"]
for url in urls:
    @Scrape.async_request_scrape(url, Sources.AioHttpSource, Save.TextDataBaseSQLalchemySaver)
    def saveDataBase(source: str, proxies=None) -> Save.TextDataBaseSQLalchemySaver.TextDataBaseSQLalchemySaverData:
        meta = MetaData()
        engine = create_engine('sqlite:///school_exp.db')
        id_col = Column('id', Integer)
        name_col = Column('name', String)
        school_name_col = Column('school_name', String)
        major_col = Column('major', String)
        cols_ = [id_col, name_col, school_name_col, major_col]
        rows = [(1, 'steve', 'SJSU', 'chemistry'), (2, "Susu", "MIT", "biology"),
                (3, "Belle", "UCLA", "Simpology")]

        data = Save.TextDataBaseSQLalchemySaver.TextDataBaseSQLalchemySaverData(engine, meta, cols_, rows, 'test')
        return data

Scrape.run()
