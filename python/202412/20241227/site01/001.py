from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/assets/css/<path:filename>')
def css_file(filename):
    return send_from_directory('static/assets/css', filename)

@app.route('/assets/js/<path:filename>')
def js_file(filename):
    return send_from_directory('static/assets/js', filename)

@app.route('/assets/images/<path:filename>')
def images_file(filename):
    return send_from_directory('static/assets/images', filename)

@app.route('/assets/fonts/<path:filename>')
def fonts_file(filename):
    return send_from_directory('static/assets/fonts', filename)

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/courses.html')
def courses():
    return render_template('courses.html')

@app.route('/price.html')
def price():
    return render_template('price.html')

@app.route('/videos.html')
def videos():
    return render_template('videos.html')

@app.route('/sidebar-right.html')
def pages():
    return render_template('sidebar-right.html')
    
@app.route('/contact.html')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
