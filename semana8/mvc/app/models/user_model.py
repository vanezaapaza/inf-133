from database import db
# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
class User(db.Model):
    __tablename__ = 'users'
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    Fecha_nacimiento = db.Column(db.Date, nullable=False)

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, email, contraseña, Fecha_nacimiento):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contraseña = contraseña
        self.Fecha_nacimiento = Fecha_nacimiento

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()