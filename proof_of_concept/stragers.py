import typing


class Saver(typing.Protocol):
    data_type: typing.Type

    def save(self):
        raise NotImplementedError()


class BaseSaver:

    def __init__(self: Saver, data) -> None:
        if not isinstance(data, self.data_type):
            raise ValueError("data is no good :(")


class TextSaver(BaseSaver, Saver):
    class TextSaverData:
        def __init__(self, bytes_):
            self.bytes_ = bytes_

    data_type = TextSaverData

    def __init__(self, data) -> None:
        super().__init__(data)
        print(f"TextSaver got data: {data}")

    def save(self):
        pass




TextSaver(TextSaver.TextSaverData(bytes_='b'))