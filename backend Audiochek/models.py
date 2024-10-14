# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir el modelo de la tabla usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.String(256), primary_key=True)  # ID como hash (string)
    name = db.Column(db.String(50), nullable=False)   # Nombre del usuario
    email = db.Column(db.String(100), nullable=False, unique=True)  # Email único
    date = db.Column(db.String(10), nullable=False)   # Fecha de nacimiento como VARCHAR
    gender = db.Column(db.String(10), nullable=False) # Género del usuario
    occupation = db.Column(db.String(50), nullable=False)  # Ocupación

# Otros modelos pueden ser definidos aquí en el futuro si lo necesitas
class AudiometriaSimple(db.Model):
    __tablename__ = 'audiometria_simple'
    
    Id_aud_simp = db.Column(db.String(300), nullable=False)  # Hash seguido por la fecha
    fecha = db.Column(db.String(30), primary_key=True)
    db_max_8000 = db.Column(db.Float, nullable=True)
    db_max_10000 = db.Column(db.Float, nullable=True)
    db_max_12000 = db.Column(db.Float, nullable=True)
    db_max_15000 = db.Column(db.Float, nullable=True)
    db_max_16000 = db.Column(db.Float, nullable=True)
    db_max_17000 = db.Column(db.Float, nullable=True)
    db_max_18000 = db.Column(db.Float, nullable=True)
    db_max_19000 = db.Column(db.Float, nullable=True)
    db_max_20000 = db.Column(db.Float, nullable=True)

class AudiometriaCompleta(db.Model):
    __tablename__ = 'audimetria_completa'
    
    Id_aud_comp = db.Column(db.String(300), nullable=False)
    fecha = db.Column(db.String(30), primary_key=True)
    db_max_right_8000 = db.Column(db.Float, nullable=True)
    db_max_left_8000 = db.Column(db.Float, nullable=True)
    db_max_right_10000 = db.Column(db.Float, nullable=True)
    db_max_left_10000 = db.Column(db.Float, nullable=True)
    db_max_right_12000 = db.Column(db.Float, nullable=True)
    db_max_left_12000 = db.Column(db.Float, nullable=True)
    db_max_right_15000 = db.Column(db.Float, nullable=True)
    db_max_left_15000 = db.Column(db.Float, nullable=True)
    db_max_right_16000 = db.Column(db.Float, nullable=True)
    db_max_left_16000 = db.Column(db.Float, nullable=True)
    db_max_right_17000 = db.Column(db.Float, nullable=True)
    db_max_left_17000 = db.Column(db.Float, nullable=True)
    db_max_right_18000 = db.Column(db.Float, nullable=True)
    db_max_left_18000 = db.Column(db.Float, nullable=True)
    db_max_right_19000 = db.Column(db.Float, nullable=True)
    db_max_left_19000 = db.Column(db.Float, nullable=True)
    db_max_right_20000 = db.Column(db.Float, nullable=True)
    db_max_left_20000 = db.Column(db.Float, nullable=True)
