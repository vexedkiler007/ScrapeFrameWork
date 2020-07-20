import typing
import aiohttp


class Source(typing.Protocol):
    data_type: typing.Type

    async def get_source(self):
        raise NotImplementedError()


class BaseSource:
    def __init__(self: Source, data) -> None:
        if not isinstance(data, self.data_type):
            raise ValueError("data is no good :(")


class AioHttpSource(Source, BaseSource):

    data_type = str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.data = data

    async def get_source(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.data) as response:
                return await response.text()


class ArcenicSource(Source, BaseSource):
    class ArcenicSourceData:
        def __init__(self, url: str) -> None:
            self.url = url

    data_type = ArcenicSourceData

    def __init__(self, data) -> None:
        super().__init__(data)

    async def get_source(self) -> str:
        pass
