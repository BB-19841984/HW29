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

    records_one = cursor.fetchone()
    print ("Вывод первой записи", records_one)

    records_two = cursor.fetchone()
    print("Вывод второй записи", records_two)

      
    
except (Exception, Error) as error:
    print (" ошибка при работе с PostgresSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgresSQL закрыто")

    