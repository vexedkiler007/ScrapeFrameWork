import typing
import asyncio
from aiofile import AIOFile
import aiohttp
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData, create_engine


class Saver(typing.Protocol):
    data_type: typing.Type

    async def save(self):
        raise NotImplementedError()


class BaseSaver:

    def __init__(self: Saver, data) -> None:
        if not isinstance(data, self.data_type):
            raise ValueError("data is no good :(")


class TextSaver(BaseSaver, Saver):
    class TextSaverData:
        def __init__(self, bytes_: bytes, filename: str) -> None:
            self.bytes_ = bytes_
            self.filename = filename

    data_type = TextSaverData

    def __init__(self, data) -> None:
        super().__init__(data)
        self.data = data

    async def save(self) -> None:
        async with AIOFile(f"{self.data.filename}.html", 'wb') as afp:
            await afp.write(self.data.bytes_)
            await afp.fsync()


class ImageSaver(BaseSaver, Saver):
    class ImageSaverData:
        def __init__(self, list_urls: typing.List[str], list_filenames: typing.List[str]):
            self.list_urls = list_urls
            self.list_filenames = list_filenames
    data_type = ImageSaverData

    def __init__(self, data):
        super().__init__(data)
        self.data = data

    async def save(self):
        async with aiohttp.ClientSession() as session:
            coros = []
            for url, filename  in zip(self.data.list_urls, self.data.list_filenames):
                async with session.get(url) as response:
                    async with AIOFile(f'{filename}', 'wb') as afp:
                        await afp.write(await response.read())
                        await afp.fsync()

            await asyncio.gather(*coros)


class TextDataBaseGinoSaver(BaseSaver, Saver):
    class TextDataBaseSaverData:
        def __init__(self, cols_name: typing.Tuple,data_kind: typing.Tuple, rows: typing.Tuple):
            self.cols_name = cols_name
            self.data_kind = data_kind
            self.rows = rows
    data_type = TextDataBaseSaverData

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        # engine = sqlalchemy.create_engine("postgresql://postgres:password@localhost/postgres")

    async def save(self):
        pass


class TextDataBaseSQLalchemySaver(BaseSaver, Saver):
    class TextDataBaseSQLalchemySaverData:
        def __init__(self, sql_engine: create_engine,
                     meta_data: MetaData,
                     cols_list: list,
                     rows: list,
                     table_name: str,) -> None:
            self.sql_engine = sql_engine
            self.meta_data = meta_data
            self.cols_list = cols_list
            self.rows = rows
            self.table_name = table_name
    data_type = TextDataBaseSQLalchemySaverData

    def __init__(self, data):
        super().__init__(data)
        self.data = data

    async def save(self):
        cols_names = [col.__dict__['name'] for col in self.data.cols_list]
        args = [self.data.table_name, self.data.meta_data] + self.data.cols_list
        table = Table(*args)
        self.data.meta_data.create_all(self.data.sql_engine)
        many_rows_format = [{key: val for key, val in zip(cols_names, row)} for row in self.data.rows]
        print(many_rows_format)
        conn = self.data.sql_engine.connect()
        conn.execute(table.insert(), many_rows_format)
        conn.close()

