# config/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@localhost/finance_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
