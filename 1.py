import psycopg2

from psycopg2 import Error, DatabaseError

try:
    with psycopg2.connect(user="postgres",
                          password="postgres",
                          host="127.0.0.1",
                          port="5432",
                          database="postgres_db",
    ) as connection:
        with connection.cursor() as cursor:
            query = """
        CREATE TABLE IF NOT EXISTS Exam (
        id SERIAL PRIMARY KEY, name VARCHAR(255), 
        score DECIMAL(10, 2));
        """
        cursor.execute(query)
    
except(Exception, Error, DatabaseError) as error:
    print (" ошибка при работе с postgres", error)
