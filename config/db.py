from sqlalchemy import create_engine, MetaData

engine= create_engine("mysql+pymysql://administrador:leonisaApi1@testleonisaapi.mysql.database.azure.com:3306/biblioteca")

conn= engine.connect()

meta_data= MetaData()
