#/board?page=2&category=notice&search=공지&sort=recent
from flask import Flask,url_for,request, render_template_string,render_template
# request  : GET, POST 값 가져올 때
# url_for : 라우터 URL과 매핑된 함수 호출, 매개변수 쿼리스트링
# render_template : 템플릿용 html 파일
# render_template_string : 템플릿 html 스트링

from urllib.parse import unquote, quote

# unquote : URL 디코딩
# quote : URL 인코딩

app = Flask(__name__)

@app.route('/board')
def board():
    params = {k:unquote(v) for k, v in request.args.items()}

    return render_template("board1.html",paramsboard=params)


if __name__ == '__main__':
    app.run(debug=True)
