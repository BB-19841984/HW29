import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user="postgres",
                                     password="postgres",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="postgres_db")
    
    cursor = connection.cursor()
        
    postgresql_select_query = "select * from exam"
    cursor.execute(postgresql_select_query)

    records = cursor.fetchall()
    for i in records:
        print(i)
   
    
except (Exception, Error) as error:
    print (" ошибка при работе с PostgresSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgresSQL закрыто")

    

