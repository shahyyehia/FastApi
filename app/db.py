from sqlalchemy import create_engine, MetaData
import pymysql
engine = create_engine('mysql+pymysql://root@localhost/newdb')
meta=MetaData()
conn=engine.connect()
