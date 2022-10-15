import requests
import bs4
from fake_useragent import UserAgent


def finder(words, text):
    for word in words:
        if word in text:
            return True


ua = UserAgent()
KEYWORDS = input('Введите ключевые слова через запятую с пробелом: ').split(', ')
URL = 'https://habr.com/ru/all/'
response = requests.get(URL, headers={"User-Agent": ua.random})
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_="tm-article-snippet")
for arcticle in articles:
    name = arcticle.find(class_="tm-article-snippet__title-link").find("span").text
    date = arcticle.find("time").attrs["title"]
    href = f'https://habr.com{arcticle.find(class_="tm-article-snippet__title-link").attrs["href"]}'
    if arcticle.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2"):
        preview = arcticle.find\
        (class_="article-formatted-body article-formatted-body article-formatted-body_version-2").find_all("p")
        previewstr = " "
        for text in preview:
            previewstr += text.text
        if finder(KEYWORDS, previewstr) is True:
            print(f'{date} | {name}\n{href}\n')
