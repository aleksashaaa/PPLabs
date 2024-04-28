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
    CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR(255), p_phone VARCHAR(255))
    AS $$
    BEGIN
    IF EXISTS (SELECT * FROM phone_book WHERE name = p_name) THEN
        UPDATE phone_book 
        SET phone_number = p_phone WHERE name = p_name;
        
    ELSE
        INSERT INTO phone_book(name, phone_number) VALUES(p_name, p_phone);
    END IF;
    END;
    $$
    LANGUAGE plpgsql;
"""

# Execute the function creation SQL
cur.execute(insert_function)
conn.commit()

# Call the function
def insert_update(name, phone):
    """Call the stored function and return the result"""
    cur.execute('CALL insert_or_update_user(%s,%s)', (name, phone))
    conn.commit()


pattern = input("Enter name and phone: ").split()
insert_update(pattern[0], pattern[1])
