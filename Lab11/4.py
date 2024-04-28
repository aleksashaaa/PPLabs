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
    CREATE OR REPLACE FUNCTION pagination(lim INT, off INT)
    RETURNS SETOF phone_book AS
    $$
    BEGIN
    RETURN QUERY
    SELECT * FROM phone_book ORDER BY name
    LIMIT lim OFFSET off;

    END;
    $$
    LANGUAGE plpgsql;
"""

# Execute the function creation SQL
cur.execute(function)
conn.commit()

# Call the function
def pagin(limit, offset):
    """Call the stored function and return the result"""
    cur.callproc('pagination', (limit, offset,))
    # Fetch all rows from the result set
    rows = cur.fetchall()
    return rows


limit = input("Enter limit: ")
offset = input("Enter offset: ")
result = pagin(limit, offset)
print(result)
