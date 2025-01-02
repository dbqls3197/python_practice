from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
import uuid
app = Flask(__name__)

memos = []

@app.route('/', methods=['GET','POST'])
def memo():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        memoid = str(uuid.uuid4())[:12] 
        memos.append({
            'title':title,
            'content':content,
            'category':category,
            'regdate': datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
            'id' : memoid
        })
        return redirect(url_for('memo'))
    return render_template('memo.html',memos=memos) 

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(memos):
        del memos[index]
    return redirect(url_for('memo'))

# @app.route('/delete/<string:id>')
# def delete(id):
#     for memo in memos:
#         if memo['id'] == id:
#             memos.remove(memo)
#             break
#     return redirect(url_for('memo'))


if __name__ == '__main__':
    app.run(debug=True)