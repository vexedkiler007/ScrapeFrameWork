import typing
import bs4
from aiofile import AIOFile
import aiohttp



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
        for url, filename  in zip(self.data.list_urls, self.data.list_filenames):
                print(url)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        async with AIOFile(f'{filename}', 'wb') as afp:
                            await afp.write(await response.read())
                            await afp.fsync()

