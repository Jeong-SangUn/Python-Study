from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
        #__name__ 현재 실행 중인 모듈의 이름을 전달, 임의의 문자열로 변경 가능

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
    username = request.args.get('name')                     #Get 방식으로 넘어온 데이터 받을때
    return render_template('index.html',username=username)

@app.route('/login/', methods=['POST']) 
def login_post():
    username = request.form['username']
    password = request.form['password']
    return render_template('index1.html',username=username,password=password)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/home/') 
def home():
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute("select min(no) from stocks")
    page=c.fetchone()
    conn.commit()
    conn.close()
    return render_template('manualSelect.html',page=page[0])       
    #현재 page 안에 튜플 형식으로 들어 있으므로 page[0]
    #만약 fetchone() 말고 fetchall() 썻으면 [(3,)] 리스트 안에 튜플이라서 page[0][0] 했어야함

@app.route('/manualSelect/' , methods=['GET']) 
def manualSelect():
    page = request.args.get('page') 
    print(page)
    return render_template('manualSelect.html',page=page)       

@app.route('/infoInput/<page>') 
def infoInput(page):
    return render_template('infoInput.html',page=page)

@app.route('/infoSelect/', methods=['POST']) 
def infoSelect():
    select = request.form['select']
    page = request.form['page']
    
    if select == "고객정보입력":
        return redirect(url_for('infoInput', page = page))
    elif select == "전체 고객정보 조회":
        return redirect(url_for('allinfo', page = page))
    elif select == "현재 고객정보 조회":
        return redirect(url_for('info', page = page , state = "now"))
    elif select == "이전 고객정보 조회":
        return redirect(url_for('info', page = page , state = "pre"))
    elif select == "다음 고객정보 조회":
        return redirect(url_for('info', page = page , state = "next"))
    elif select == "현재 고객 정보 수정":
        return redirect(url_for('updateinfo', page = page))
    elif select == "현재 고객 정보 삭제":
        return redirect(url_for('deleteinfo', page = page))
    elif select == "프로그램종료":
        return redirect('/exit')

@app.route('/exit')      #http://127.0.0.1:5000/
def exit():
    return '프로그램 종료!'

@app.route('/info/<page>/<state>') 
def info(page,state):
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    if state == "now":
        page = page
    elif state == "pre":
        c.execute("select max(no) from stocks where no < ?",page)
        pageno=c.fetchone()
        if pageno[0] != None:
            page = pageno[0]
        else:
            conn.commit()
            conn.close()
            return render_template('noOutput.html',state=state,page=page)
    elif state == "next":
        print(page)
        c.execute("select min(no) from stocks where no > ?",page)
        pageno=c.fetchone()
        if pageno[0] != None:
            page = pageno[0]
        else:
            conn.commit()
            conn.close()
            return render_template('noOutput.html',state=state,page=page)
    c.execute("select * from stocks where no = ?",str(page))
    result=c.fetchall()
    conn.commit()
    conn.close()
    return render_template('infoOutput.html',result=result,page=page)

@app.route('/updateinfo/<page>') 
def updateinfo(page):
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute("select * from stocks where no = ?",page)
    result=c.fetchone()
    conn.commit()
    conn.close()
    return render_template('updateinfo.html',result=result,page=page)

@app.route('/deleteinfo/<page>') 
def deleteinfo(page):
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute("select * from stocks where no = ?",page)
    result=c.fetchone()
    conn.commit()
    conn.close()
    return render_template('deleteinfo.html',result=result,page=page)

@app.route('/updateinfo_post/' ,methods=['POST']) 
def updateinfo_post():
    page = request.form['page']
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    year = request.form['year']

    temp = (name, gender, email, year, page)
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    
    c.execute("update stocks set name=?,gender=?,email=?,year=? where no = ?",temp)
    conn.commit()
    conn.close()
    return render_template('manualSelect.html',page=page)

@app.route('/deleteinfo_post/' ,methods=['POST']) 
def deleteinfo_post():
    page = request.form['page']
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute("delete from stocks where no = ?",page)
    conn.commit()
    conn.close()
    return render_template('manualSelect.html',page=page)

@app.route('/allinfo/<page>') 
def allinfo(page):
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute("select * from stocks")
    result=c.fetchall()
    conn.commit()
    conn.close()
    return render_template('infoOutput.html',result=result,page=page)

@app.route('/infoInput/', methods=['POST']) 
def infoInput_post():
    page = request.form['page']
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    year = request.form['year']
    conn=sqlite3.connect('webinfo.db')
    c = conn.cursor()
    c.execute('''
    insert into stocks(name,gender,email,year)
    values(?,?,?,?)
    ''',(name,gender,email,year))
    conn.commit()
    conn.close()
    return render_template('manualSelect.html',page=page)


if __name__=='__main__':
    app.run(debug=True)



#app.run(host=0.0.0.0) 다른 컴퓨터도 접속 가능함
#app.run(port=80) 기본적으로는 5000번에서 실행 다른곳을 원하면 port 지정