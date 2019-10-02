from flask import Flask, render_template, redirect, request
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import io
import base64
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#웹 앱 객체 생성
app = Flask(__name__)


@app.route('/form',methods=['POST'])

def form():
    pclass = request.form['pclass']
    sex = request.form['sex']
    age = request.form['age']

    load_model = joblib.load("c:/data/titanic_model.pkl")
    df = pd.DataFrame(
        data={'pclass': [pclass], 'sex': [sex], 'age': [age]},
        columns=['pclass', 'sex', 'age'])
    suv = str(load_model.predict(df)[0])

    return redirect('index?ret='+suv)

@app.route('/index',methods=['GET'])
def index():
    result = request.args.get('ret')
    result_temp =''
    if result=='0':
        result_temp ='당신은 죽을 확률이 높습니다.'
    elif result=='1':
        result_temp='당신은 살 확률이 높습니다.'

    colors = ['gold', 'yellowgreen', 'lightcoral', 'blue', 'red']
    labels = ['java', 'c언어', 'spring', 'python', 'sklearn']
    ratio = [20,50,39,59,80]
    explode = (0.0 , 0.1, 0.4, 0.0 , 0.0)

    font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font',family=font_name)

    plt.pie(ratio, explode = explode, labels=labels,colors=colors, autopct='%1.1f%%',shadow=True)
    # plt.show()
    #만들어진 그래프를 이미지로 변경해서 index.html로 값을 전달해서 표시
    plt.draw()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_url = base64.b64encode(img.getvalue()).decode()
    plt.close()


    return render_template('index.html',
                           title='그래프표시'
                           ,graph1='data:image/png;base64,{}'.format(img_url)
                           ,result_suv = result_temp)

if __name__=='__main__':
    app.run()
