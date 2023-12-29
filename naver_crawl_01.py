from bs4 import BeautifulSoup
import requests

baseURL = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
keyword = input("input some: ")
searchURL = baseURL + keyword

r = requests.get(searchURL)

text = r.text
# print(text)

soup = BeautifulSoup(text, "html.parser")
items = soup.select(".news_tit")

for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")

# print(items[0].text)

# <a class="news_tit" href="http://www.stoo.com/article.php?aid=85019650489" onclick="return goOtherCR(this, 'a=nws*b.tit&amp;r=1&amp;i=88155e74_000000000000000000778155&amp;g=5348.0000778155&amp;u='+urlencode(this.href));" target="_blank" title="리버풀-첼시, '단두대 매치'서 0-0 무승부"><mark>리버풀</mark>-첼시, '단두대 매치'서 0-0 무승부</a>