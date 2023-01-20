from sqlalchemy import create_engine, MetaData

engine= create_engine("mysql+pymysql://root@localhost:3306/nombredb")



meta_data= MetaData()
