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
function = """
    CREATE OR REPLACE PROCEDURE delete(p_phone VARCHAR(255))
    AS $$
    BEGIN
    DELETE FROM phone_book WHERE phone_number = p_phone;
    END;
    $$
    LANGUAGE plpgsql;
"""

# Execute the function creation SQL
cur.execute(function)
conn.commit()

# Call the function
def delete_by_phone(phone):
    """Call the stored function and return the result"""
    cur.execute('CALL delete(%s)', (phone,))
    conn.commit()


pattern = input("Enter phone: ")
delete_by_phone(pattern)
