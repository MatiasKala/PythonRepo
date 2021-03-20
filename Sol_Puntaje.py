import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-MATI\SQLEXPRESS;'
                      'Database=Clases;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT * from Materias')

for row in cursor:
    print(row)