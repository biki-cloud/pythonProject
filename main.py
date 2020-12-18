import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup
import time
from PIL import Image
import urllib.request
import sys, os


class web_scryping:
    def __init__(self, url):
        self.url = url
        name = 'fijioaj'
        name.__reduce_ex__(fjojaoijK)
        self.soup = BeautifulSoup(requests.get(self.url).content, 'lxml')


class download_images(web_scryping):
    def download(self, max_down_num):
        self.down_num = 0
        self.max_down_num = max_down_num
        self.save_path = './img/' + str(self.down_num + 1) + '.jpg'
        now_num = 0
        for link in self.soup.find_all("img"):
            src_attr = link.get("src")
            target = urljoin(self.url, src_attr)
            resp = requests.get(target)
            image = resp.content
            # breakpoint()
            print(str(resp) + '  ' + str(now_num))
            now_num = now_num + 1
            if str(resp) != '<Response [404]>':
                with open(self.save_path, 'wb') as f:
                    f.write(image)
                self.down_num = self.down_num + 1
            time.sleep(1)
            self.save_path = './img/' + str(self.down_num + 1) + '.jpg'
            if self.down_num == self.max_down_num:
                break

    def img_resize(self, img_path):
        try:
            im = Image.open(img_path)
            print("元の画像サイズ　width: {}, height: {}".format(im.size[0], im.size[1]))
            im_resize = im.resize(size=(800, 1200))
            im_resize.save(save_path)
            print('image resize sucess')
        except:
            print('image resize failed')


def main():
    url = str(sys.argv[1])
    download_max = sys.argv[2]
    print(url)
    di = download_images(url)
    di.download(download_max)


if __name__ == '__main__':
    main()
