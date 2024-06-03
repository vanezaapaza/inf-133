import json
from flask_login import UserMixin
from database import db
class User(UserMixin, db.model):
    __tablename__ = "users"

    id = db.column(db.integer, primary_key = False)
    name = db.column(db.string(50) unique = True , nullable = False)
    descripcion = db.column(db.string(100) nullable = False)
    price = db.column(db.integer, primary_key = False)
    stock = db.column() 