# Import libraries required for connecting to MySQL
import mysql.connector

# Import libraries required for connecting to PostgreSql
import psycopg2


# ============================================================
# MySQL connection information
# ============================================================

mysql_user = 'root'
mysql_password = 'U0nuR8z3urF4w8knKRdX3Aw9'
mysql_host = '172.21.37.20'
mysql_database = 'sales'


# ============================================================
# PostgreSQL connection information
# ============================================================

postgres_user = 'postgres'
postgres_password = 'Xiov7p7GehRYIEB3zBfyMFka'
postgres_host = '172.21.192.246'
postgres_port = '5432'
postgres_database = 'postgres'


# ============================================================
# Connect to MySQL
# ============================================================

mysql_connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    host=mysql_host,
    database=mysql_database
)

mysql_cursor = mysql_connection.cursor()


# ============================================================
# Connect to PostgreSQL
# ============================================================

postgres_connection = psycopg2.connect(
    database=postgres_database,
    user=postgres_user,
    password=postgres_password,
    host=postgres_host,
    port=postgres_port
)

postgres_cursor = postgres_connection.cursor()


# ============================================================
# Find out the last rowid from PostgreSQL data warehouse
# ============================================================

def get_last_rowid():
    postgres_cursor.execute(
        "SELECT MAX(rowid) FROM sales_data"
    )

    result = postgres_cursor.fetchone()

    if result[0] is None:
        return 0

    return result[0]


last_row_id = get_last_rowid()

print("Last row id on production datawarehouse = ", last_row_id)


# ============================================================
# Get all records from MySQL with rowid greater than
# the last rowid in PostgreSQL
# ============================================================

def get_latest_records(rowid):

    mysql_cursor.execute(
        """
        SELECT rowid, product_id, customer_id, quantity
        FROM sales_data
        WHERE rowid > %s
        ORDER BY rowid
        """,
        (rowid,)
    )

    records = mysql_cursor.fetchall()

    return records


new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))


# ============================================================
# Insert the additional records into PostgreSQL
# ============================================================

def insert_records(records):

    SQL = """
        INSERT INTO sales_data
        (rowid, product_id, customer_id, quantity)
        VALUES (%s, %s, %s, %s)
    """

    for record in records:
        postgres_cursor.execute(SQL, record)

    postgres_connection.commit()


insert_records(new_records)

print(
    "New rows inserted into production datawarehouse = ",
    len(new_records)
)


# ============================================================
# Disconnect from MySQL warehouse
# ============================================================

mysql_cursor.close()
mysql_connection.close()


# ============================================================
# Disconnect from PostgreSQL data warehouse
# ============================================================

postgres_cursor.close()
postgres_connection.close()


# End of program