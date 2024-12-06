import sqlalchemy as _sql
from dotenv import load_dotenv
import os
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# DB Connetion and configurations
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
