from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
app = Flask(__name__)

todos = []
# title, due_date, priority, completed, regdate

# @app.route('/', methods=['GET','POST'])
# def todo():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         due_date = request.form.get('due_date')
#         priority = request.form.get('priority')
#         todos.append({
#             'title':title,
#             'due_date':due_date,
#             'priority':priority,
#             'completed':False,
#             'regdate': datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#         })
#         return redirect("/")

#     return render_template('todo.html',todos=todos) # 뒤에 todos는 위쪽에 리스트 todos 앞에 todos 는 변수

# @app.route('/toggle/<int:index>')
# def toggle(index):
#     todos[index].completed = not todos[index].completed
#     return redirect(url_for('todo'))

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/')
def todo():
    return render_template ('todo.html',todos=todos)

@app.route('/append',methods=["POST"])
def append():
    if request.method == 'POST':
        title = request.form.get('title')
        due_date = request.form.get('due_date')
        priority = request.form.get('priority')
        todos.append({
            'title':title,
            'due_date':due_date,
            'priority':priority,
            'completed':False,
            'regdate': datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        })
        return redirect("/")

@app.route('/toggle/<int:index>')
def toggle(index):
    todos[index].completed = not todos[index].completed
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True)

