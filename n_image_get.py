from bs4 import BeautifulSoup
import requests


def image_naver(serch,num):
    j = int(num)  # 가져올 리스트를 정할 변수 받아오기.
    img_src = []  # 링크 담을 리스트 생성.
    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(
        serch)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup.text)

    #이미지 클라스로 크롤링.
    #https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2F20151008_244%2Fjulian1366_1444257965387vMopW_JPEG%2Fmug_obj_201510080746057102.jpg&type=b400
    img = soup.find_all(class_='_img')

    # 링크 리스트로 가져오기(변수로 몇개 가져올지 확인)
    for i in img:
        src = i['data-source']  # 주소가 데이터소스에 있음.
        #print(src)
        img_src.append(src)
        if len(img_src) == j:
            break

    #print(img_src)
    return img_src


# if __name__ == "__main__":
#    print(image_naver('강아지',20))
