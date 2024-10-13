# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:P4ng0l1n854@181.79.5.78:33306/audicheck?charset=utf8mb4'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones y seguridad
