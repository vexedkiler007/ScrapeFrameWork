import Sources
import Save
import Scrape

url_y = "https://www.google.com/"


@Scrape.async_request_scrape(url_y, Sources.AioHttpSource, Save.TextSaver)
def scrape(source: str) -> Save.TextSaver.TextSaverData:
    bytes_ = bytes(source, 'utf-8')
    return Save.TextSaver.TextSaverData(bytes_, 'cool')


Scrape.run()
