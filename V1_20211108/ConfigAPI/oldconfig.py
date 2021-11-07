import os
from configparser import ConfigParser

parser = ConfigParser()
parser.read("./ConfigAPI/ConfigDB/configdb.ini")
rds_host = parser.get("SQLMariaDB", "host")
name = parser.get("SQLMariaDB", "name")
password = parser.get("SQLMariaDB", "password")        
port = int(parser.get("SQLMariaDB", "port"))
database = parser.get("SQLMariaDB", "database")
data_base = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)
database = parser.get("SQLMariaDB2", "database")
data_base2 = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)

class BaseConfig:
    """Base configuration."""
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SECRET_KEY = 'Loyola'
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = data_base
    SQLALCHEMY_BINDS ={
        'rt_database':    data_base2
    }