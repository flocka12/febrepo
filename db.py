import os
import psycopg2

def establish_connection():
    """Establish a database connection"""
    database_url = os.getenv("DATABASE_URL")
    try:
        connection = psycopg2.connect(database_url)
    except psycopg2.DatabaseError as error:
        print("error {}".format(error))
    return(connection)  

def create_table_queries():
    "SQL Queries to create tables"
    users = """CREATE TABLE IF NOT EXISTS "users"(
        ID SERIAL PRIMARY KEY,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        othername VARCHAR(50) NOT NULL,
        email VARCHAR(254) UNIQUE NOT NULL,
        phone_number VARCHAR(12) NOT NULL,
        username VARCHAR(50) UNIQUE NOT NULL,
        registered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE,
        password VARCHAR(100) NOT NULL
        )"""
    redflags = """CREATE TABLE IF NOT EXISTS "redflags"(
        ID SERIAL PRIMARY KEY,
        created_by INT NOT NULL,
        created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        TYPE VARCHAR(50) NOT NULL,
        comment VARCHAR(300) NOT NULL,
        location VARCHAR(50) NOT NULL,
        images VARCHAR [] DEFAULT '{}',
        videos VARCHAR [] DEFAULT '{}',
        status VARCHAR [] DEFAULT '{}',
        FOREIGN KEY (question_id) REFERENCES redflags (id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        )"""
    queries = [users, redflags]
    return queries

def drop_table_queries():
    """SQL queries to drop tables"""
    drop_queries = [
        "DROP TABLE IF EXISTS users CASCADE",
        "DROP TABLE IF EXISTS redflags CASCADE"
    ]
    return drop_queries
def create_tables(connection):
    """Create the database tables"""
    database_url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    queries = create_table_queries()
    for query in queries:
        cursor.execute(query)
    connection.commit()

def destroy(database_url):
    """Drop database table entries"""
    database_url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    queries = drop_table_queries()
    for query in queries:
        cursor.execute(query)
    connection.commit()
