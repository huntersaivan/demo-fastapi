from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f"{settings.database_type}://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"#?driver={settings.database_driver}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         # connect to postgresql
#         # conn = psycopg2.connect(host='localhost', database='fastapi',
#         #                         user='sa', password='intertaiment', cursor_factory=RealDictCursor)
#         server = 'localhost'
#         database = 'fastapi'
#         username = 'sa'
#         password = 'intertaiment'
#         conn = pyodbc.connect(
#             f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
#         cursor = conn.cursor()
#         print("Database connection is succesfuly!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)
