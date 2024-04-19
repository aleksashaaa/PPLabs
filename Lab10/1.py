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

# Delete table
cur.execute('DROP TABLE phone_book;')
conn.commit()

# Create a new table
cur.execute("""CREATE TABLE phone_book (
            name VARCHAR(255),
            city VARCHAR(255),
            job VARCHAR(255),
            phone_number VARCHAR(20) PRIMARY KEY
);
""")

conn.commit()

# Create new students from input
values = input().split()
cur.execute(f"""INSERT INTO phone_book (name, city, job, phone_number) VALUES 
            ('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}');
""")
conn.commit()

#Creating from csv file
import csv

filename = 'people.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, city, job, phone_number = row
        # Create new people
        cur.execute(f"""INSERT INTO phone_book (name, city, job, phone_number) VALUES 
                    ('{name}', '{city}', '{job}', '{phone_number}');
        """)
        conn.commit()

# Get students
cur.execute('SELECT name, city, job, phone_number FROM phone_book')
print(cur.fetchall())


conn.commit()