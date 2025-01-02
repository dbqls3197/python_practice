from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)

surveys = []

questions = [
    '이 서비스에 대해 얼마나 만족하십니까?',
    '이 서비스를 다른 사람에게 추천하시겠습니까?',
    '서비스 개선을 위한 제안사항이 있으십니까?'
]

# 설문시작
@app.route('/')
def survey():
    return render_template('survey.html',questions=questions)

# 설문종료
@app.route('/dosurvey',methods=["POST"])
def dosurvey():
    responses = []
    for i in range(len(questions)):
        responses.append(request.form.get(f'q{i}'))
    surveys.append({
        'response' : responses,
        'regdate':datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    })
    return render_template('finish.html')

# 설문결과
@app.route('/results')
def results():
    return render_template('results.html', surveys=surveys, questions=questions)


if __name__ == '__main__':
    app.run(debug=True)
