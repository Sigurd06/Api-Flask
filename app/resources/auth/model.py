from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import BaseModelMixin

class User(BaseModelMixin):
    __tablename__ = 'users'

    username = Column(String(25), nullable=False, unique=True)
    password_hash = Column(String(120), nullable=False)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def __str__(self):
        return f'<User> {self.username}'
    
    def __repr__(self):
        return f'<User> {self.id}/{self.username}'