from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index3.html') 

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/products')
def contact():
    return render_template('products.html')  



if __name__ == '__main__':
    app.run(debug=True)
