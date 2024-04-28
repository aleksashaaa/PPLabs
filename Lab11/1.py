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
return_function = """
    CREATE OR REPLACE FUNCTION return_data(name1 VARCHAR(255))
    RETURNS SETOF phone_book AS
    $$
    BEGIN
    RETURN QUERY
    SELECT * FROM phone_book
    WHERE phone_book.name LIKE name1 || '%';

    END;
    $$
    LANGUAGE plpgsql;
"""

# Execute the function creation SQL
cur.execute(return_function)
conn.commit()

# Call the function
def get_data_by_name(name1):
    """Call the stored function and return the result"""
    cur.callproc('return_data', (name1,))
    # Fetch all rows from the result set
    rows = cur.fetchall()
    return rows


name_pattern = input("Enter name pattern: ")
result = get_data_by_name(name_pattern)
print(result)
