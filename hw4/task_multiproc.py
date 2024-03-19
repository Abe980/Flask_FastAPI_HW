import multiprocessing
import urllib.request
import time
import sys


def load_img(url_img):
    urllib.request.urlretrieve(url_img, f"./img/{url_img.split('/')[-1]}")



if __name__ == '__main__':

    url_list = sys.orig_argv[2:] if sys.orig_argv[2:] else [
    'https://www.opensourceforu.com/wp-content/uploads/2017/05/Python-12-Large2-768x545.jpg',
    'https://vodvore.net/demotivators/cr_009411642140897782807.jpg',
    'https://vodvore.net/demotivators/cr_168096714315257074324.jpg'
    ]

    start_time = time.time()
    multiproc = []

    for u in url_list:
        t = multiprocessing.Process(target=load_img, args=(u,))
        multiproc.append(t)
        t.start()

    for t in multiproc:
        t.join()


    print(time.time() - start_time)