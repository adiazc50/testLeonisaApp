from sqlalchemy import create_engine, MetaData


#Me conecto a la base de datos
engine= create_engine("mysql+pymysql://root:toor@localhost:3306/biblioteca")



meta_data= MetaData()
