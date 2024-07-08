from sqlalchemy import create_engine, MetaData

# Datos de conexión
dbname = "foretagbi"
user = "postgres"
password = "Foretagbi"
host = "localhost"

# Crear una URL de conexión para SQLAlchemy
# connection_url = f"postgresql://{user}:{password}@{host}/{dbname}"
# connection_url = f"postgresql://foretagbi:foretagbi@localhost/foretagbi"
connection_url = f"postgresql://postgres:Foretagbi@localhost/postgres"


# Crear una instancia de motor SQLAlchemy
engine = create_engine(connection_url)

# Conectar al motor
conn = engine.connect()

# Crear un objeto MetaData
metadata = MetaData()

# Listar todas las tablas en la base de datos
metadata.reflect(bind=engine)

# Obtener las tablas
tables = metadata.tables

# Iterar sobre las tablas e imprimir sus nombres
for table_name in tables:
    print(table_name)

# Cerrar la conexión
conn.close()
