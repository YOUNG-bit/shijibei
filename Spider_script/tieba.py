import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=200)
        r.raise_for_status()
        return r.text
    except:
        print(0)
        return ""

def get_data(lst,text):
    demo = text
    soup = BeautifulSoup(demo, 'html.parser')
    div = soup.find_all('div')
    for i in div:
        try:
            if 'threadlist_abs' in i.attrs['class']:
                lst.append(i.string)
        except:
            continue
    return lst

def Spider(url,page):
    print("现在只支撑爬去bit贴吧的数据")
    lst = []
    url = 'https://tieba.baidu.com/f?kw=%E5%8C%97%E4%BA%AC%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
    for i in range(page+1):
        if i== 0 : continue
        print(i)
        url = url + str(i*50)
        text = getHTMLText(url)
        get_data(lst,text)
    return lst

