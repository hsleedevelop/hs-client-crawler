# import clien_parser
from datetime import datetime
from clien_parser import ClienParser

# baseURL = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
modu = "https://www.clien.net/service/board/park?&od=T31&category=0&po="
iphone = "https://www.clien.net/service/board/cm_iphonien?&od=T31&category=0&po="
news = "https://www.clien.net/service/board/news?&od=T31&category=0&po="
tips = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
use = "https://www.clien.net/service/board/use?&od=T31&category=0&po="

def write(results, subject):
    filename = "[" + subject + "]" + str(datetime.now()) + ".html".replace(" ", ".")
    with open("/Users/hsleeathome/Downloads/" + filename, "w") as text_file:
        for result in results:
            text_file.write("[" + subject + "]" + result)

def crawling(url, max, subject):
    lists = []
    for i in range(max): 
        lists.append(url + str(i))
    
    parser = ClienParser(lists)
    results = parser.parseURLs()
    write(results, subject)

crawling(modu, 10, "modu")
print("=========================================")
crawling(iphone, 5, "iphone")
print("=========================================")
crawling(news, 10, "news")
print("=========================================")
crawling(tips, 5, "tips")
print("=========================================")
crawling(use, 5, "use")

