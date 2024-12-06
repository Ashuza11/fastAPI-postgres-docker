import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# DB Connetion and configurations
# DATABASE_URL = "postgresql://myuser:password@localhost/fastapi_database"
DATABASE_URL = "postgresql://myuser:password@localhost:5433/fastapi_database"


engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()