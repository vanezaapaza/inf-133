from database import db

class Productos(db.Model):
    __tablename__ = "productos"

    id = db.column(db.integer, primary_key = True)
    name = db.column(db.string(100), nullable = False)
    descripcion = db.column(db.string(100), nullable =False)
    price = db.column(db.integer, primary_key = True)
    stock = db.column(db.integer, primary_key = True)

    def __init__(self, id, name, descripcion, price, stock):
        self.id = id
        self.name = name
        self.descripcion = descripcion
        self.price = price
        self.stock = stock

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Productos.query.all 