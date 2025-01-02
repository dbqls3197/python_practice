## 세션 정리

from flask import Flask, session
from datetime import timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

### 세션 유효시간 설정
# 5분 설정
app.permanent_session_lifetime = timedelta(minutes=5)
# 1시간 설정
app.permanent_session_lifetime = timedelta(hours=1)
# 7일 설정
app.permanent_session_lifetime = timedelta(days=7)

### 세션 설정 (다양한 데이터 타입)
@app.route('/set_data')
def set_session_data():
    session['user_id'] = 123
    session['username'] = 'test_user'
    session['is_admin'] = False
    session['preferences'] = {
        'theme' : 'dark',
        'language' : 'ko'
    }
    return '세션 데이터가 설정되었습니다.'

### 세션 확인
@app.route('/get_data')
def get_session_data():
    if 'user_id' in session:
        user_data = {
            'id' :session['user_id'],
            'name' :session['username'],
            'is_admin' :session['is_admin'],
            'preferences' :session['preferences']
        }
        return str(user_data)
    return '세션 데이터가 없습니다.'

### 세션 수정
@app.route('/update_data')
def update_session_data():
    if 'preferences' in session:
        session['preferences']['theme'] = 'light'
        session.modified = True  # 세션이 변경되었음을 명시적으로 설정
        # 라우트 단위로 만료기간 설정
        session.permanent
        app.permanent_session_lifetime = timedelta(hours=1)
        return '세션 데아터가 수정되었습니다.'
    return '수정할 세션 데이터가 없습니다.'

### 세션 삭제
@app.route('/delete_data')
def delete_session_data():
    # 특정 세션 데이터만 삭제
    session.pop('user_id',None)
    # 모든 세션 데이터 삭제
    session.clear()
    return '세션 데아터가 삭제되었습니다'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return '로그인이 필요합니다.',401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/protected')
@login_required
def protected_route():
    return '보호된 페이지입니다.'

if __name__ == '__main__':
    app.run(debug=True)