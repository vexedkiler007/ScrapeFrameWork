import asyncio
import aiohttp
from aiofile import AIOFile
import datetime
import Save
list_coro = []


async def fetch_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def save_text_html(bytes, file_name):
    async with AIOFile(f"{file_name}.html", 'wb') as afp:
        await afp.write(bytes)
        await afp.fsync()


# cols = ("col_name1", "col_name2", col_name3 ...)
# data = ((col_data, col_data, col_data), (col_data, col_data, col_data) ....)
async def save_to_database(cols, data):
    pass


# list_url = ("google.com/cool.jpg", ....)
async def save_images(list_url):
    pass


async def save_videos(list_url):
    pass


async def driver(url):
    pass


def get_name(url):
    return "".join([char for char in url if char.isalpha()]) + "_" + str(datetime.datetime.now().timestamp())


def async_request_scrape(url, save="html", source_type="text"):
    def create_coroutine(function):
        file_name = get_name(url)

        async def coro():
            source = await fetch_text(url)
            string = bytes(function(source), 'utf-8')
            await save_text_html(string, file_name)

        list_coro.append(coro())
        return function

    return create_coroutine


@async_request_scrape(url="https://www.google.com/")
def hi(source: str) -> :

    return source


@async_request_scrape(url="https://www.google.com/")
def hello(source):
    return source


async def gather(list_coro):
    await asyncio.gather(*list_coro)


loop = asyncio.get_event_loop()
loop.run_until_complete(gather(list_coro))
