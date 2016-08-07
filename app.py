# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
import math
from flask_paginate import Pagination
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:13167118553@localhost/movie'
db = SQLAlchemy(app)
session = db.session()

# Base = declarative_base()
# engine = create_engine('mysql+mysqlconnector://root:13167118553@localhost:3306/movie')
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
#新闻首页
class News(db.Model):   #News(Base)
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)
    count = Column(Integer, default = 0)
    def __init__(self, title, source, content, time, count):
        self.title = title
        self.source = source
        self.content = content
        self.time = time
        self.count = count


@app.route('/', methods=['GET','POST'])
def index():
    #分页功能
    page = int(request.args.get('page','1'))
    POSTS_PER_PAGE = 15
    if page<1:
        page = 1
        paginate = News.query.order_by(News.id).paginate(page,POSTS_PER_PAGE,False)
    else:
        paginate = News.query.order_by(News.id).paginate(page, POSTS_PER_PAGE, False)
    #newsList = session.query(News).all();
    newsList = paginate.items;
    totalNum = paginate.total #总的新闻数目
    totalPage = int(math.ceil(totalNum/float(POSTS_PER_PAGE))) #总的页数

    return render_template('index.html',new=newsList,
            pagination=paginate, POSTS_PER_PAGE = POSTS_PER_PAGE, total = totalPage)

@app.route('/rec/<title>')
def rec(title):
    rec = session.query(News).filter_by(title = title).first()
    rec.count  = rec.count+1
    session.add(rec)
    session.commit()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)

class Ent(db.Model):
    __tablename__ = 'ent'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/ent', methods=['GET','POST'])
def entindex():
    newsList = session.query(Ent).all();
    return render_template('indexEnt.html',new=newsList)

@app.route('/ent/<title>')
def entrec(title):
    rec = session.query(Ent).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)
class Sports(db.Model):
    __tablename__ = 'sports'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/sports', methods=['GET','POST'])
def sportsIndex():
    newsList = session.query(Sports).all();
    return render_template('indexSports.html',new=newsList)

@app.route('/sports/<title>')
def sports(title):
    rec = session.query(Sports).filter_by(title = title).first()

    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)

class Auto(db.Model):
    __tablename__ = 'auto'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/auto', methods=['GET','POST'])
def autoIndex():
    newsList = session.query(Auto).all();
    return render_template('indexAuto.html',new=newsList)

@app.route('/auto/<title>')
def auto(title):
    rec = session.query(Auto).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)

class Money(db.Model):
    __tablename__ = 'money'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/money', methods=['GET','POST'])
def moneyIndex():
    newsList = session.query(Money).all();
    return render_template('indexMoney.html',new=newsList)

@app.route('/money/<title>')
def money(title):
    rec = session.query(Money).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)

class Tech(db.Model):
    __tablename__ = 'tech'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/tech', methods=['GET','POST'])
def techIndex():
    newsList = session.query(Tech).all();
    return render_template('indexTech.html',new=newsList)

@app.route('/tech/<title>')
def tech(title):
    rec = session.query(Tech).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)

class War(db.Model):
    __tablename__ = 'war'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)

@app.route('/war', methods=['GET','POST'])
def warIndex():
    newsList = session.query(War).all();
    return render_template('indexWar.html',new=newsList)

@app.route('/war/<title>')
def war(title):
    rec = session.query(War).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)
if __name__ == '__main__':
    #可以让局域网内的人都可以访问到
    app.run(host='0.0.0.0')
    #app.run(debug=True)

