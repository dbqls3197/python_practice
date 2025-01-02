from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')


def home():
    return "Hello, World!!!"
@app.route('/user/<string:user_name>/<int:user_id>')


def user(user_name,user_id):
        return f"{user_name}({user_id})님 안녕하세요"

if __name__ == '__main__':
    app.run(debug=True)