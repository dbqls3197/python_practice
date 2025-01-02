from flask import Flask,url_for,request, render_template_string,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)