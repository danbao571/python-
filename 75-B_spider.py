import requests
from bs4 import BeautifulSoup
import json


class BSpider(object):
    def __init__(self):
        self.url = "https://search.bilibili.com/all?" \
                   "keyword=%E8%89%BA%E6%9C%AF%E5%AE%B6%E9%98%BF%E5%85%8B%E6%9B%BC&page={}"
        self.headrs = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        }
        self.detail_list = []

    # 获取网页url
    def get_url(self):
        url_list = []
        for i in range(1, 5):
            url_list.append(self.url.format(i))
        return url_list

    # 解析网页内容
    def parse_response(self, url):
        response = requests.get(url, headers=self.headrs).content.decode()
        soup = BeautifulSoup(response, 'lxml')
        tag_a = soup.select('a[class="img-anchor"]')

        for i in range(len(tag_a)):
            title = tag_a[i].get('title')
            url = tag_a[i].get('href')[2:]
            info_dict = {
                'title': title,
                'url': url,
            }
            self.detail_list.append(info_dict)

    # 保存数据
    def save_data(self):
        json.dump(self.detail_list, open('b_data.json', 'w', encoding='utf-8'), ensure_ascii=False)

    # 统筹调用
    def start(self):
        url_list = self.get_url()
        for url in url_list:
            self.parse_response(url)
        self.save_data()


BSpider().start()
