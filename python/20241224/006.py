from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates/base.html') 

@app.route('/about')
def about():
    return render_template('templates/about.html')  

@app.route('/contact')
def contact():
    return render_template('templates/contact.html')  
@app.route('/service')
def services():
    return render_template('templates/service.html')  

if __name__ == '__main__':
    app.run(debug=True)
