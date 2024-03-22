import psycopg2


db_inform = {
    "dbname": "test",
    "user": "jimin",
    "password": "1234",
    "host": "000.000.0.000",
    "port": "0000",
} 


def connect_to_database(db_inform):
    global conn, cur
    try:
        conn = psycopg2.connect(**db_inform)
        cur = conn.cursor()
        print("Database connection established successfully!")
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as error:
        print(f"Error connecting to the database: {error}")
        print(f"Database Unconnected")


def main():
    query = f"SELECT * FROM test.operation LIMIT 2"
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)

    cur.close()
    conn.close()
    print("Database connection is closed")

    return True


if __name__ == "__main__":
    connect_to_database(db_inform)
    main()