import psycopg2
 
def deleteData(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                     password="postgres",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="postgres_db")
        cursor = connection.cursor()
 
        sql_delete_query = """Delete from exam\
        where id = %s"""
        cursor.execute(sql_delete_query, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
 
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
 
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
 
 
id = 2
deleteData(id)