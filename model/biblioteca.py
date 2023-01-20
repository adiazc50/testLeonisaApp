from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import engine, meta_data

#Creo la tabla para la DB en caso de que no exista.
biblioteca= Table("biblioteca", meta_data,
                Column("isbnId", Integer, primary_key=True),
                Column("titulo",String(255), nullable=False),
                Column("autor",String(255), nullable=False),
                Column("editorial",String(255), nullable=False),
                Column("coleccion",String(255), nullable=False),
                Column("cantidad",Integer, nullable=False),
                Column("diponible",Integer , nullable=False))

meta_data.create_all(engine)

