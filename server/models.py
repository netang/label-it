from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Numeric, Float, ForeignKey, String, Column, Date, Boolean, DateTime, BigInteger

db = SQLAlchemy()

class Tasks(db.Model):
    """Tasks"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    name = Column(String)
    filename = Column(String)
    created = Column(DateTime)
    answer_type = Column(String)
    count_of_texts = Column(Integer)
    count_of_links = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'             : self.id,
            'name'           : self.name,
            'filename'       : self.filename,
            'created'        : self.created,
            'answer_type'    : self.answer_type,
            'count_of_texts' : self.count_of_texts,
            'count_of_links' : self.count_of_links,
        }

class Users(db.Model):
    """Users"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    password_salt = Column(String)
    password = Column(String)
    created = Column(DateTime)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'             : self.id,
            'name'           : self.name,
            'email'          : self.email,
            'created'        : self.created,
        }

class SourceData(db.Model):
    """SourceData"""
    __tablename__ = 'source_data'
    id = db.Column(db.Integer, primary_key = True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    text_1 = Column(String)
    text_2 = Column(String)
    text_3 = Column(String)
    link_1 = Column(String)
    link_2 = Column(String)
    link_3 = Column(String)
    answer = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'             : self.id,
            'task_id'        : self.task_id,
            'text_1'         : self.text_1,
            'text_2'         : self.text_2,
            'text_3'         : self.text_3,
            'link_1'         : self.link_1,
            'link_2'         : self.link_2,
            'link_3'         : self.link_3,
            'answer'         : self.answer,
        }