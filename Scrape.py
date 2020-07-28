import asyncio
from typing import Callable, Coroutine
from Sources import Proxy
list_coro = []


def async_request_scrape(url: str, source_getter: Callable, saver: Callable, proxy: Proxy = None) -> Callable:
    def create_coroutine(parser):
        coro = build_coroutine(source_getter(url, proxy), parser, saver, proxy)
        list_coro.append(coro)
        return parser

    return create_coroutine


def build_coroutine(source_getter_url, parser: Callable, saver: Callable, proxy: Proxy = None) -> Coroutine:
    async def coro():
        source = await source_getter_url.get_source()
        result = parser(source, proxy)
        print(result)
        await saver(result).save()

    return coro()


async def gather(list_coro: list) -> None:
    await asyncio.gather(*list_coro)


def run() -> None:
    print(list_coro)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather(list_coro))
