from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Features')
def features():
    return render_template('Features.html')

@app.route('/Support')
def support():
    return render_template('Support.html')

@app.route('/Downloads')
def downloads():
    return render_template('Downloads.html')

@app.route('/Contacts')
def contacts():
    return render_template('Contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
