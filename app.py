from flask import Flask, render_template, request
import n_image_get
import g_image_get

# 플라스크 앱 서버 인스턴스
app = Flask(__name__)

# url 패턴 - 라우터 설정


@app.route('/')
def index():

    #return render_template('index.html') 기본 리턴문
    serch =request.args.get('serch') #값 불러오기.
    num =request.args.get('serch_num') #값 불러오기.
    if not serch : # 최초 값이 없을 때 빈 화면 출력하기 위한 조건문.
        return render_template('index.html')
    
    n_data=n_image_get.image_naver(serch,num)

    if not n_data: # 빈 값을 받아왔을 때 빈화면 출력하기 위한 조건문.
        return render_template('index.html')
    
    #g_data = g_image_get.imge_google(serch,num)
    
    return render_template('index.html') #, n_data=n_data, g_data=g_data  검색 삭제

# 메인 테스트
if __name__ == "__main__":
    app.run(debug=True)