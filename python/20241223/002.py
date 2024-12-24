### 동적 URL 구성

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
     return 'Hello, World!!!'

# 동적 URL: string, int, float (함수의 인자로 사용)
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name='홍길동',user_id='3'):
    return f"Hello,{user_name}({user_id})!"

if __name__== '__main__':
    app.run(debug=True)