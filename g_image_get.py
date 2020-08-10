from bs4 import BeautifulSoup
import requests

def imge_google(serch,num) :
    j=int(num)
    url = 'https://www.google.co.kr/search?newwindow=1&hl=ko&authuser=0&tbm=isch&sxsrf=ALeKk01k4sUyRmtGA9DHBCUIS2sg78zJjg%3A1597044270672&source=hp&biw=905&bih=770&ei=LvYwX8a4JoG1mAXfr6CADA&q={}&oq=&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQ6gIQJzoICAAQsQMQgwFQ5QtY7hNgrRVoAnAAeAGAAYcCiAGnC5IBBTAuNC4zmAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img&ved=0ahUKEwjGh8TDjZDrAhWBGqYKHd8XCMAQ4dUDCAc&uact=5'.format(serch)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup)
    img = soup.find_all('img') # img태그로 크롤링
    #print(img)
    img_src=[]

    for i in img:

            src = i['src']  # 주소가 src에 있음.   
            img_src.append(src)
            if len(img_src) == j:
                break
            
        # print(src)

    #print(img_src[1:])
    return img_src[1:]


if __name__ == "__main__":
   print(imge_google('강아지',20))

