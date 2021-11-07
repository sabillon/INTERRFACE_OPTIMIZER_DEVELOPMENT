import os
from configparser import ConfigParser

parser = ConfigParser()
parser.read("./ConfigAPI/ConfigDB/configdb.ini")
rds_host = parser.get("PDB", "host")
name = parser.get("PDB", "name")
password = parser.get("PDB", "password")        
port = int(parser.get("PDB", "port"))
database = parser.get("PDB", "database")
PDB = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)   
database = parser.get("FDB", "database")
FDB = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)
database = parser.get("RTDB", "database")
RTDB = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)
database = parser.get("MDB", "database")
MDB = 'mysql+pymysql://'+str(name)+':'+str(password)+'@'+str(rds_host)+':'+str(port)+'/'+str(database)

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
    SQLALCHEMY_DATABASE_URI = PDB
    SQLALCHEMY_BINDS ={
        'FutureDB':   FDB,
        'RealTimeDB': RTDB,
        'ManagementDB': MDB

    }