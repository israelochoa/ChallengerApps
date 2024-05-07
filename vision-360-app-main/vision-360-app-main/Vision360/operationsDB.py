import sqlite3

# Conéctate a la base de datos
conn = sqlite3.connect('db.sqlite3')

# Crea un cursor
cursor = conn.cursor()

# Ejecuta el comando para obtener todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Imprime todas las tablas
print(cursor.fetchall())

# Cierra la conexión
conn.close()
