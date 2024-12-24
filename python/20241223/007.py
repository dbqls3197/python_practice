from flask import Flask,url_for,request, render_template_string
from urllib.parse import unquote, quote # URL디코딩, 인코딩

app = Flask(__name__)

@app.route('/products')
def product_list():
    # URL 디코딩
    params = {k:unquote(v) for k, v in request.args.items()}
    #return request.args
    #return '상품 목록'

# with app.test_request_context():
#     print(url_for('product_list'))
#     print(url_for('product_list', search='노트북'))
#     print(url_for('product_list',
#                     search='노트북',
#                     min_price=1000000,
#                     max_price=2000000,
#                     sort='price_desc'))

    html = '''
    <h2>상품 리스트</h2>
    <table border='1'>
        <tr><th>파라미터</th><th>값</th></tr>
        {%for key, value in params2.items()%}
        <tr><td>{{key}}</td><td>{{value}}</td></tr>
        {% endfor %}
    '''
    return render_template_string(html)

    ### html 스트링(텍스트)을 템플릿 파일로
    # return render_tmplate_string(html,params2=params)

    ### html 파일을 템플릿 파일로
    return render_template_string(product1.html,params3=params)
if __name__ == '__main__':
    app.run(debug=True)