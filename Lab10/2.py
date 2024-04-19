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

# Update students
cur.execute("""UPDATE phone_book
            SET name = 'Dmitry'
            WHERE phone_number = '+77473332211';
""")
conn.commit()

# Get students
cur.execute('SELECT name, city, job, phone_number FROM phone_book')
print(cur.fetchall())

# Delete students
cur.execute("""DELETE FROM phone_book
            WHERE LENGTH(phone_number) < 11;
""")
conn.commit()

# Get students
cur.execute('SELECT name, city, job, phone_number FROM phone_book')
print(cur.fetchall())

conn.commit()