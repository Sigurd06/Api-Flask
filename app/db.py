from sqlalchemy import Column, Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModelMixin(db.Model):
    __abstract__ = True
    
    id = Column(Integer(), primary_key=True, unique=True, nullable=False)

    # created_at = Column(DateTime, default=func.now())
    # updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()