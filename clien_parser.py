from bs4 import BeautifulSoup
import requests

class ClienParser:
    def __init__(self, urls):
        self.urls = urls
        self.results = []
    
    def parseURLs(self):
        for url in self.urls:
            self.parse(url)
        return self.results

    def parse(self, url):
        print(url)
        r = requests.get(url)
        text = r.text
        # print(text)

        soup = BeautifulSoup(text, "html.parser")
        items = soup.select(".list_title")
        # items = soup.select(".subject_fixed.stretch_shortwidth.change_display")
        # items = soup.select(".list-title-text")

        for e, item in enumerate(items, 1):
            replyCount = item.select_one(".rSymph05")
            if replyCount is None or int(replyCount.text) < 10:
                # print("small")
                continue

            subject = item.select_one(".subject_fixed")
            if subject is None:
                # print("none")
                continue

            link = item.select_one(".list_subject").get("href")
            
            result = "<a href='https://clien.net" + link + "' target='blank'>" + subject.text + ", reply:" + replyCount.text + "</a><br /><br />"
            # print(subject.text, "reply", replyCount.text, "https://clien.net" + link)
            self.results.append(result)
            # print(subject.text, "reply", replyCount.text, link.get if link.get("href") is not None else "no link")
            # print(subject["title"])
            # print(link.get("href"))
            # print(f"{e} : {item.text}")

            # https://www.clien.net/service/board/cm_iphonien/17857855?od=T31&po=0&category=1000490&groupCd=
