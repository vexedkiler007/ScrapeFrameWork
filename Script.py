from sqlalchemy import MetaData, create_engine, Column, Integer, String
import Sources
import Save
import Scrape
from bs4 import BeautifulSoup
import os



# @Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.TextSaver)
# def scrape(source: str) -> Save.TextSaver.TextSaverData:
#     bytes_ = bytes(source, 'utf-8')
#     return Save.TextSaver.TextSaverData(bytes_, 'cool')
#
#
# @Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.ImageSaver)
# def scrapeImages(source: str) -> Save.ImageSaver.ImageSaverData:
#     soup = BeautifulSoup(source, 'html.parser')
#     container = soup.find(class_="rpBJOHq2PR60pnwJlUyP0")
#     link_list = []
#     file_list = []
#     for img in container.find_all('img'):
#         endings = ['jpg', 'png']
#         try:
#             link = img['src']
#             file_name = os.path.basename(link)
#             file_name_list = file_name.split('.')
#             if file_name_list[-1] not in endings:
#                 if 'png' in file_name_list[-1]:
#                     file_name_list[-1] = '.png'
#                     file_name = "".join(file_name_list)
#                 if 'jpg' in file_name_list[-1]:
#                     file_name_list[-1] = '.jpg'
#                     file_name = "".join(file_name_list)
#             link_list.append(link)
#             file_list.append(file_name)
#
#         except KeyError as e:
#             print(str(e) + " image")
#
#     return Save.ImageSaver.ImageSaverData(link_list, file_list)


# @Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.TextDataBaseSaver)
# def saveDataBase(source: str) -> Save.TextDataBaseSaver.TextDataBaseSaverData:
#     soup = BeautifulSoup(source, 'html.parser')
#     names = ('Titles', 'Likes', 'SubReddit')
#     types_ = ('String', 'String', 'String')
#     container = soup.find(class_="rpBJOHq2PR60pnwJlUyP0")
#
#     rows = []
#     for num, child in enumerate(container.find_all(class_ = 'scrollerItem')):
#         try:
#             title = child.find(class_ = '_2SdHzo12ISmrC8H86TgSCp').text
#             like = child.find(class_ = '_1E9mcoVn4MYnuBQSVDt1gC').text
#             subreddit = child.find(class_ = "_2mHuuvyV9doV3zwbZPtIPG").text
#             print(title)
#             print(like)
#             print(subreddit)
#             rows.append((title, like, subreddit))
#
#         except AttributeError as e:
#             print(f'__{e}__')
#     print(rows)
#     rows = tuple(rows)
#     print(rows)
#     return Save.TextDataBaseSaver.TextDataBaseSaverData(names, types_, rows)

@Scrape.async_request_scrape("http://127.0.0.1:5000/static/test.html", Sources.AioHttpSource, Save.TextDataBaseSQLalchemySaver)
def saveDataBase(source: str) -> Save.TextDataBaseSQLalchemySaver.TextDataBaseSQLalchemySaverData:
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
