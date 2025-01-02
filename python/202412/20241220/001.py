### route

from flask import Flask

# set FLASK_APP=app.py  # --- 윈도우 환경변수       
# export FLASK_APP=app.py  # ---맥/리눅스 환경변수(bash)
#print(__name__)
app = Flask(__name__)

@app.route('/') # /를 home()함수와 연결 : 라우팅
@app.route('/home')  # /home 를 home2()함수와 연결: 라우팅

def home():
    return "Hello, World!!!"

@app.route('/user')
def user():
    return "<b>Hello</b>, User!!"

if __name__ == '__main__':
    app.run(debug=True)
    # host = '127.0.0.1' (기본값) -localhost
    # host = '0.0.0.0'  - 모든 대역대 ip에서 접근
    # host = '10.0.66.200' - 특정 ip에서만 접근

    # [debug]
    # True: 오류정보 표시, 소스수정시 재시작 
    # False: (기본값)

    # [Reload]
    # True: 소스수정시 재시작
    # Flase (기본값)

    # [port]
    # 5000 (기본값)

