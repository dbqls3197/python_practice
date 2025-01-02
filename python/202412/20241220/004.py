from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "홈페이지"

@app.route('/about')
def aboutfunc():
    return "정보페이지"

# url_for : 라우팅 되어 있는 함수 호출하여 매핑된 URL 값 가져오기
@app.route('/redirect')
def redirect_to_about():
    return f'<a href="{url_for("aboutfunc")}"> 정보 페이지로 이동</a>'
    #return '<a href="/about"> 정보 페이지로 이동</a>'

@app.route('/user/<username>')
def user_profile(username):
    return f'사용자: {username}'

@app.route('/go_to_user/<username>')
def go_to_user(username):
    return f'<a href="{url_for("user_profile",username=username)}">{username}의 프로필로 이동</a>'

@app.route('/user/<username>/<int:user_id>')
def user_profile2(username, user_id):
    return f'사용자: {username}, 사용자 ID: {user_id}'

@app.route('/go_to_user/<username>/<int:user_id>')
def go_to_user2(username, user_id):
    return f'<a href="{url_for("user_profile2",username=username,user_id=user_id)}">{username}의 프로필로 이동</a>'
    
# [url_for]
# 1) / : 리소스 경로를 정의
#           /user/홍길동
#           매개변수 형태가 <username> 식일 때
# 2) ? : 추가 정보를 전달
#           /search?q=Flask
#           매개변수 형태가 /search 처럼 없으면서 값을 q=Flask 형태로 넘길때 
# @app.route('/search')
# def search():
#     query = request.args.get('q')    #get방식으로 넘어온 값 받아오기
#     return f'검색어 : {query}'

# @app.route('/search_link')
# def search_link():
#     return f'<a href="{url_for("search", q="Flask")}">Flask검색하기</a>'


@app.route('/search')  
#@app.route('/search',methods=['GET']) 
#@app.route('/search',methods=['GET','POST'])
def search():
     # GET방식으로 넘어온 값 받을 때(기본값은 빈 문자열)
    search_term = request.args.get('search_term','')

    ## POST방식으로 넘어온 값 받을 때
    #search_term = request.form['search_term']
    return f'검색어: {search_term}'

@app.route('/search_link')
def search_link():
    return '''
        <form action='/search' method='get'>
        <input type='text' name='search_term'
        placeholder='검색어를 입력하세요'>
        <input type='submit' value='검색'>
    '''


@app.route('/etc')
def etc():
    return'''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문</p>
    <a target='blank' href='https://flask.palletsprojects.com'>Flask 홈페이지 바로가기 </a> 
    '''

if __name__ == '__main__':
    app.run(debug=True)