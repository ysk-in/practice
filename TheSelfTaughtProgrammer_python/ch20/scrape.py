import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import os
import requests
import traceback

# 出力する記事情報の最大値
ARTICLE_MAX = 20


class Scraper:
    def __init__(self, url):
        self.url = url
        self.articles = dict()

    def add_article(self, index=0, title="none", url="none"):
        article = {
            "Article " + str(index).zfill(len(str(ARTICLE_MAX))): {
                'title': title,
                'url': url
            }
        }
        self.articles.update(article)

    def scrape(self):
        r = urllib.request.urlopen(self.url)
        html = r.read()
        sp = BeautifulSoup(html, "html.parser")
        article_index = 1
        for article in sp.find_all("article"):
            if is_valid_article(article):
                title = article.span.string
                url = get_redirect_destination_url(urllib.parse.urljoin(self.url, article.a.get('href')))
                print("Article {}\n\tTitle={}\n\tURL={}".format(article_index, title, url))
                self.add_article(article_index, title, url)
                article_index += 1
            if article_index > ARTICLE_MAX:
                # 適当なところで止める
                break

    def dump_article(self, file_path):
        c = input("File({})を上書きしてOK? (Y/n): ".format(file_path)).lower()
        if c == "n":
            return
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.articles, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))


def is_valid_article(article):
    if article is None:
        print("article is None")
        return False
    elif article.span is None:
        print("article.span is None")
        return False
    elif article.a is None:
        print("article.a is None")
        return False
    elif article.a.get('href') is None:
        print("article.a.href is None")
        return False
    return True


def get_redirect_destination_url(url):
    destination_url = requests.get(url).url
    print("リダイレクト先取得 url={}, dest={}".format(url, destination_url))
    return destination_url


def get_output_path():
    current_dir = os.getcwd()
    output_path = os.path.join(current_dir, "scrape.json")
    print("CurrentDirectory={}, OutFile={}".format(current_dir, output_path))
    return output_path


if __name__ == "__main__":
    try:
        s = Scraper("https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja")
        print("スクレイピング開始")
        s.scrape()
        s.dump_article(get_output_path())
    except BaseException as e:
        print("error e={}".format(str(e)))
        traceback.print_exc()
