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

#Define the function
insert_function = """
    CREATE OR REPLACE PROCEDURE insert_multiple_users(p_names VARCHAR(255)[], p_cities VARCHAR(255)[], 
        p_work VARCHAR(255)[],  p_phones VARCHAR(255)[])
    AS $$
    DECLARE
        i INT;
        phone_ok BOOLEAN;
    BEGIN
        FOR i IN 1..array_length(p_names, 1) LOOP
            IF NOT EXISTS (SELECT * FROM phone_book WHERE phone_number = p_phones[i]) THEN
                phone_ok := (LENGTH(p_phones[i]) >= 12);
                IF phone_ok THEN
                    INSERT INTO phone_book(name, city, job, phone_number) VALUES(p_names[i], p_cities[i], p_work[i], p_phones[i]);
                ELSE
                    RAISE NOTICE 'Invalid phone number for user: %', p_names[i];
                END IF;
                
            END IF;
        END LOOP;
    END;
    $$ 
    LANGUAGE plpgsql;
"""

# Execute the function creation SQL
cur.execute(insert_function)
conn.commit()

# Call the function
def insert_update(names, cities, jobs, phones):
    """Call the stored function and return the result"""
    cur.execute('CALL insert_multiple_users(%s,%s,%s,%s)', (names, cities, jobs, phones))
    conn.commit()


n = int(input("Enter number of new users: "))
names, cities, jobs, phones = [], [], [], []
for i in range(n):
    p = input("Enter name, city, job and phone: ").split()
    names.append(p[0])
    cities.append(p[1])
    jobs.append(p[2])
    phones.append(p[3])

insert_update(names, cities, jobs, phones)
