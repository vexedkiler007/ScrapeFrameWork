import asyncio
import Sources
from typing import Callable, Coroutine

list_coro = []


def async_request_scrape(url: str, source_getter, saver) -> Callable:
    def create_coroutine(parser):
        coro = build_coroutine(source_getter(url), parser, saver)
        list_coro.append(coro)
        return parser

    return create_coroutine


def build_coroutine( source_getter, parser, saver) -> Coroutine:
    async def coro():
        source = await source_getter.get_source()
        result = parser(source)
        await saver(result).save()

    return coro()


async def gather(list_coro: list) -> None:
    await asyncio.gather(*list_coro)


def run() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather(list_coro))