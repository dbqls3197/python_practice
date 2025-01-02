from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)

memos = []

@app.route('/', methods=['GET','POST'])
def memo():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        memos.append({
            'title':title,
            'content':content,
            'category':category,
            'regdate': datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
        })
        return redirect(url_for('memo'))

    return render_template('marry.html',memos=memos) 


if __name__ == '__main__':
    app.run(debug=True)