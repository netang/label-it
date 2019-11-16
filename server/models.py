from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Numeric, Float, ForeignKey, String, Column, Date, Boolean, DateTime, BigInteger

db = SQLAlchemy()

class Tasks(db.Model):
    """Tasks"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    name = Column(String)
    description = Column(String)
    initiator_id = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'             : self.id,
            'name'           : self.name,
            'description'    : self.description,
            'initiator_id'   : self.initiator_id
        }