from flask import Flask, render_template, request

app = Flask(__name__)
        #__name__ 현재 실행 중인 모듈의 이름을 전달, 임의의 문자열로 변경 가능

@app.route('/abc')      #http://127.0.0.1:5000/abc
def index():
    return 'Hello world 정상운'

@app.route('/')      #http://127.0.0.1:5000/
def index1():
    return 'Hello world 정상운!'

@app.route('/user/<username>')      #http://127.0.0.1:5000/user/쏼라쏼라
def user(username):
    return 'user: %s' %username

@app.route('/user/<username>/<int:age>')      #http://127.0.0.1:5000/user/정상운/27
def user1(username, age):
    return render_template('index.html',username=username,age=age)

@app.route('/forminput/') 
def forminput():
    return render_template('forminput.html')

@app.route('/method/', methods=['GET','POST']) 
def method():
    if request.method == 'POST':
        return "Post"
    else:
        return "Get"

@app.route('/form_input/') 
def form_input():
    return render_template('form_input.html')

@app.route('/login/', methods=['GET']) 
def login():        #http://127.0.0.1:5000/login?name=정상운
    username = request.args.get('name')
    return render_template('index.html',username=username)

@app.route('/login/', methods=['POST']) 
def login_post():
    username = request.form['username']
    password = request.form['password']
    return render_template('index1.html',username=username,password=password)


if __name__=='__main__':
    app.run()



#app.run(host=0.0.0.0) 다른 컴퓨터도 접속 가능함
#app.run(port=80) 기본적으로는 5000번에서 실행 다른곳을 원하면 port 지정