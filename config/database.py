import pyodbc

server= 'testappleonisa.database.windows.net'
bd='nombredb'
usuario ='administraor'
contrasena='admin123'

try:

    conexion = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:testappleonisa.database.windows.net,1433;Database=nombredb;Uid=administrador;Pwd=admin123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    print('conectado')

except:
    print('Error de conexion')