import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./comments.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
