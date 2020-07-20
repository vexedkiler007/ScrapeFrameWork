import typing
from aiofile import AIOFile


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
