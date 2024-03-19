import asyncio
import time
import urllib.request
import sys


async def load_img(url_img):
    urllib.request.urlretrieve(url_img, f"./img/{url_img.split('/')[-1]}")


async def main():
    for u in url_list:
        task = asyncio.create_task(load_img(u))
        await task


if __name__ == '__main__':

    url_list = sys.orig_argv[2:] if sys.orig_argv[2:] else [
    'https://www.opensourceforu.com/wp-content/uploads/2017/05/Python-12-Large2-768x545.jpg',
    'https://vodvore.net/demotivators/cr_009411642140897782807.jpg',
    'https://vodvore.net/demotivators/cr_168096714315257074324.jpg'
    ]

    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)