import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='hS36a1L2'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Get students
cur.execute('SELECT name, city, job, phone_number FROM phone_book ORDER BY name')
print(*cur.fetchall())

# Get students
cur.execute('SELECT name, city, job, phone_number FROM phone_book ORDER BY city')
print(*cur.fetchall())

conn.commit()