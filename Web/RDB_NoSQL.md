# Database

4 주 - sql, 5주 mongoDB

SQL/DB FLASK와 연결하는 것

회원정보 가게정보 등 하나하나 데이터 왕창 모아둔것 DB임.

관리하기 어려워서 → DBMS 마리아DB, MYSQL, SQLITE, MongoDB 등.. 다 DBMS

## DBMS(Data Base Management System)

- 관계형 (Relation): 일종의 표 형식으로 저장 MySQL
- 문서형(Document): 인덱스를 제외하고 아무거나 넣을 수 있다. MongoDB
- 그 외
  - 키-값형(KV store): 모든 데이터를 키와 값의 쌍으로 매핑
  - 객체형 (Object): 데이터를 객체처럼 사용한다.

### SQL(Structured Query Language) : MYSQL 등 관계형데이터베이스에서 자료 처리하기위해 사용되는 언어

### NOSQL 비관계형 데이터베이스를 제외한 대부분의 DB에서 사용함

mongoDB

JSON형식의 데이터 구조를 갖고 있다. 제약조건없고 자유롭게 확장 가능하다

## 데이터 베이스와 서버

대형 회사 데이터베이스 서버와 일반 서버는 분리되어있다.

서로 분리되어 통신하므로 서버는 DB와 연결이 되어야 함

pymysql이나 pymongo 등으로 연결해줬었지.

## ORM(Object Relation Mapping)

SQL은 table,,, 표단위로 움직인다.

Python 테이블이 없어서 '객체' 로 움직임

데이터베이스도 객체로 다루면 좋지 않을까?

그래서 ORM 사용하는 것

객체의 관계를 인식하여 python으로 데이터베이스의 데이터를 자동 매핑,, sql로 자동 생성해준다

db.session.add()

db.session. ... orm역할

ORM통해 코드를 작성했다면,

### 장점

python → orm → MySQL, postgreSQL 등등

관계형 DB인 경우 DBMS가 바뀌어도 그대로 사용할 수 있다.

연결 과정만 바꿔주면 된다.

SQLAlchemy - ORM의 python버전.

## SQL

기본키, 외래키, 복합키, NOT NULL, UNIQUE 등 제약 조건성이 크다.

기본 키

왜래 키

복합 키

조건이 많다보니, 아무 데이터나 넣어버리면 Mysql에서 안받아줄테니,

## python → 1차 검증 → ORM→ DBMS

이런 검증 과정을 거친다. 여기서 1차 검증은 model.py

### models.py

각 데이터베이스 테이블의 정보. 다 정의

이 제약조건 파이썬에서 미리 검증하기 위해 적어놓은 것임.

## request.form/ and*, or*

페이지에 폼이 있다. (그리고 클라이언트 뒤에 서버가 있고?)

### 1. **request.form** 폼 데이터 가져옴


**request**
flask는 이걸 받아요.
클라이언트가 post로 무엇을 보내면
request 안에 정보가 담긴다
 - > 시간, ip, 운영체제, 브라우저 정보 등등
```
from flask import Blueprint, render_template, request, url_for, session, flash
from rabbit_delivery.models import *
from werkzeug.utils import redirect
```
request.form - 유사 dict형태로 받아옴
```
request.form['user_id]
```
이런식으로 가져온다.

### 2. **and*, or*** 정보 <-> DB
form 에서는 name을 가지고 온다.
search.html
```
  <body>
    <form action="/search" method="POST">
      <p>이름<input type="text" id="keyword" name="keyword1" /></p>
      <p>나이<input type="text" id="keyword" name="keyword2" /></p>
      <p>
        <input type="radio" name="condition" value="1" checked="checked" />and
        <input type="radio" name="condition" value="2" />or
      </p>
      <input type="submit" value="검색" />
    </form>
  </body>
```
api.py
```
from flask import redirect, request, render_template, jsonify, Blueprint
from models import User
from db_connect import db
from sqlalchemy import and_, or_


friends = Blueprint('friends',__name__)

@friends.route('/search', methods=['GET', 'POST'])
def user_search():
    if request.method == 'POST':
        key1 = request.form['keyword1']
        key2 = request.form['keyword2']
        #radio box 사용
        con = request.form['condition']
        if(con=='1'): #and
            user_list = User.query.filter(or_(User.name == key1, User.age ==key2)).all()
        elif(con=='2'):
            user_list = User.query.filter(or_(User.name == key1,User.age ==key2)).all()
        return render_template('member_list.html', user_list=user_list)
    else:
        return render_template('search.html')


@friends.route('/list')
def user_list():
    user_list = User.query.all()
    return render_template('member_list.html', user_list=user_list)

```

user_search() 함수 기능
and 및 or 검색 결과



### 3. 가져온 정보 RETURN 해주기