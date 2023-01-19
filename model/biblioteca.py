from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

#Creamos la tabla

bibliotecas= Table("bibliotecas", meta_data,
                Column("isbnId", String, primary_key=True),
                Column("titulo",String(255), nullable=False),
                Column("autor",String(255), nullable=False),
                Column("editorial",String(255), nullable=False),
                Column("coleccion",String(255), nullable=False),
                Column("cantidad",int, nullable=False),
                Column("diponible",bool , nullable=False))

meta_data.create_all(engine)

