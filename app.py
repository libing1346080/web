# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, abort

app = Flask(__name__)


Base = declarative_base()

class News(Base):
    __tablename__ = 'ent'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True)
    source = Column(String(1500),unique=True)
    content = Column(String(10000),unique=True)
    time = Column(String(300),unique=True)
    # def __init__(self,title,source,content,time):
    #     self.title = title
    #     self.source = source
    #     self.content = content
    #     self.time = time


engine = create_engine('mysql+mysqlconnector://root:13167118553@localhost:3306/movie')
DBSession = sessionmaker(bind=engine)
session = DBSession()
# new_user = News( title='libing',source='libing',content='libing',time='libing')
# session.add(new_user)
# session.commit()
# session.close()
#user = session.query(News).filter(News.id==51).one()
# new = session.query(News).all()
# for news in new:
#     print news.title


@app.route('/', methods=['GET','POST'])
def index():
    new = session.query(News).all();
    return render_template('index.html',new=new)

@app.route('/rec/<title>')
def rec(title):
    rec = session.query(News).filter_by(title = title).first()
    if rec is None:
        abort(404)
    return render_template('article.html',rec = rec)
if __name__ == '__main__':
    app.run(debug=True)

