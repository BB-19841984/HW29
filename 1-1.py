import psycopg2

from psycopg2 import Error, DatabaseError

try:
    with psycopg2.connect(
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
        database="postgres_db",
    ) as connection:
        connection.autocommit = False
        with connection.cursor() as cursor:
            query = f"""
        INSERT INTO Exam (id, name, score) VALUES
                            (1, 'Din', 10),
                            (2, 'Ali', 9),
                            (3, 'Mayk', 8),
                            (4, 'Jim', 10)"""
            
            cursor.execute(query)
        connection.commit()
        print("Транзакция успешна завершена.")
        
               
except(Exception, Error, DatabaseError) as error:
    print ("Ошибка в транзакции. Отмена всех остальных операций", error)
    connection.rollback()
