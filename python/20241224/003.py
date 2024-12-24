from flask import Flask,url_for,request, render_template_string,render_template
app = Flask(__name__)

# 이모지 딕셔너리
emojis = {
    'trophy': '🏆',
    'star': '⭐',
    'heart': '❤️',
    'check': '✅',
    'warning': '⚠️',
    'rocket': '🚀',
    'fire': '🔥',
    'clock': '⏰',
    'smile': '😊',
    'thumbs_up': '👍',
    'new': '🆕',
    'pencil': '✏️'
}

@app.route('/')
def home():
    return render_template('index.html',emojis=emojis)

if __name__ == '__main__':
    app.run(debug=True)