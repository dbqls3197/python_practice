from flask import Flask,url_for,request, render_template_string,render_template
app = Flask(__name__)

@app.route('/')
def notifications():
    notifications =[
        {'type':'success','message':'작업이 성공적으로 완료되었습니다.'},
        {'type':'warning','message':' 주의가 필요한 상황입니다.'},
        {'type':'error','message':' 오류가 발생했습니다.'},
        {'type':'info','message':'새로운 업데이트가 있습니다.'}
    ]
    emojis = {
        'bell': '🔔️',
        'success': '✅️',
        'warning': '⚠️️',
        'error': '❌️',
        'info': 'ℹ️️'
    }
    return render_template('notifications.html',
    notifications=notifications,emojis=emojis)

if __name__ == '__main__':
    app.run(debug=True)