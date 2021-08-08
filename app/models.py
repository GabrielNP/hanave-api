from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB

from app.utils.db import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    __tablename__ = 'products'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'image    ': self.image,
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    address = db.Column(JSONB, nullable=True)

    __tablename__ = 'users'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'phone': self.phone,
            'address': self.address,
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now())
    products = db.Column(JSONB, nullable=False)

    __tablename__ = 'carts'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'products': self.products,
        }

