from flask import Flask, render_template
from flask import send_from_directory


app = Flask(__name__)

@app.route('/css/<path:filename>')
def css_file(filename):
    return send_from_directory('static/css', filename)

@app.route('/js/<path:filename>')
def js_file(filename):
    return send_from_directory('static/js', filename)

@app.route('/images/<path:filename>')
def images_file(filename):
    return send_from_directory('static/images', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news.html')
def new():
    return render_template('news.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)




