from flask import Flask, render_template, request, url_for, redirect, session
from flask_session import Session 
from datetime import timedelta
app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_USE_SIGNER'] = True
app.config["SECRET_KEY"] = 'your_secret_key'

Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_session')
def set_session():
    session['user'] = 'username'
    session['info'] = 'info'
    return '세션 생성됨 : <a href="/">Home</a>'

@app.route('/get_session')
def get_session():
    user = session.get('user','로그인정보 없음')
    return f'사용자 정보 : {user} <a href="/">Home</a>'

@app.route('/del_session')
def del_session():
    user = session.get('user')
    session.pop('user',None)
    return f'사용자 삭제 : {user} <a href="/">Home</a>'

@app.route('/del_sessionAll')
def del_sessionAll():
    session.clear()
    return f'전체 삭제됨 :  <a href="/">Home</a>'

if __name__ == '__main__':
    app.run(debug=True)