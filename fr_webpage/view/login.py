from flask import Flask, Blueprint, request, render_template, flash, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user, logout_user
from control.user_mgmt import User
import datetime
from db_model.mysql import conn_mysqldb

login_test = Blueprint('login', __name__)


@login_test.route('/set_id', methods=['GET', 'POST'])
def set_id():
    if request.method == 'GET':
        # print('set_id', request.headers)
        #print('set_id', request.args.get('user_id'))
        return redirect(url_for('login.test_login'))
    else:
        # print('set_id', request.headers)
        # content type 이 application/json 인 경우
        # print('set_id', request.get_json())
        print('set_id', request.form['user_id'], request.form['user_pw'])
        if User.find(request.form['user_id'], request.form['user_pw'])==None:
            flash('아이디 비번이 틀렸습니다')
            return render_template("login.html")
        else:
            user = User.find(request.form['user_id'], request.form['user_pw'])
            # https://docs.python.org/3/library/datetime.html#timedelta-objects
            login_user(user, remember=True, duration=datetime.timedelta(days=365))
            print(current_user.user_id)
            return redirect(url_for('login.test_login'))

    # return redirect('/ryureeru/test_login')
    # return make_response(jsonify(success=True), 200)


@login_test.route('/logout')
def logout():
    #User.delete(current_user.id) 탈퇴
    logout_user()
    return redirect(url_for('login.test_login'))

'''
@login_test.route("/signup")
def signup():
    return render_template("signup.html")


@login_test.route('/test_signup', methods=['GET', 'POST'])
def test_signup():
    if request.method == 'POST':
        if User.find2(request.form['user_id_tmp'])!=None:
            flash('회원가입이 된 아이디가 있습니다')
            return render_template("signup.html")
        else:
            User.create2(request.form['user_id_tmp'], request.form['user_pw_tmp'])
            flash('회원가입을 성공했습니다')
            return render_template("signup.html")
    else:
        return redirect(url_for('login.signup'))
'''

@login_test.route('/test_login')
def test_login():
    if current_user.is_authenticated: #권한이 있으면
        print(current_user.user_id)
        return render_template('index.html', user_id=current_user.user_id) #index로 넘어갈 수 있음
    else:
        print("x")
        return render_template('login.html') #권한이 없으면 login.html


# 로그인된 후 page 조회
@login_test.route('/check', methods=['GET', 'POST']) # 로그인 된 후 홈 화면
def check():
    mysql_db = conn_mysqldb()
    db_cursor = mysql_db.cursor()

    sql = "SELECT * FROM user_check WHERE USER_ID = '" + current_user.user_id + "'"
    db_cursor.execute(sql)
    
    content = db_cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
    if not content:
        print('xxx')
        return make_response(jsonify(success=False), 401)

    else:
        content_list = []
 
        for obj in content: # 튜플 안의 데이터를 하나씩 조회해서
            data_dic = { # 딕셔너리 형태로
                # 요소들을 하나씩 넣음
                'week': obj[0],
                'date_check': obj[2],
                'check_check':obj[3]
            }
            content_list.append(data_dic) # 완성된 딕셔너리를 list에 넣음
 
        return render_template('page.html', data_list=content_list, user_id=current_user.user_id) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
