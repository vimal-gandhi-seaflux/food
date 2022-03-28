# Importing libraries
import imp
import logging
from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
import os
# Initialization
meta = MetaData()


# Creating engine
auth = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
database = f"{os.getenv('DATABASE_URL')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
db = create_engine(f"mysql+pymysql://{auth}@{database}", pool_recycle=3600)

# Connecting db
try:
    db.connect()
    logging.info("Database connected successfully.")
except Exception as e: 
    logging.error(e)
