from genelmudur.models.chats import Chats
from genelmudur.models.users import Users
from genelmudur.models.federations import Federations
from genelmudur.models.membership import Memberships

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser, SectionProxy

sqlconfig: ConfigParser = ConfigParser()
sqlconfig.read("sql.ini")
csql: SectionProxy = sqlconfig["SQLSETTINGS"]

ConnectionString = f"{csql['DB_ENGINE']}://{csql['DB_USERNAME']}:{csql['DB_PASSWORD']}@{csql['DB_ADRESSES']}:{csql['DB_PORT']}/{csql['DB_DATABASE']}"
DbEngine = create_engine(ConnectionString)
Base: declarative_base = declarative_base()

Chats.__table__.create(bind=DbEngine, checkfirst=True)
Users.__table__.create(bind=DbEngine, checkfirst=True)
Federations.__table__.create(bind=DbEngine, checkfirst=True)
Memberships.__table__.create(bind=DbEngine, checkfirst=True)

Session: sessionmaker = sessionmaker(DbEngine)
session = Session()
