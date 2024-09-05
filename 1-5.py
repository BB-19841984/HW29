import psycopg2
 
 
def updateData(id, name):
    try:
        connection = psycopg2.connect(user="postgres",
                                     password="postgres",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="postgres_db")
 
        cursor = connection.cursor()
        sql_update_query = """Update exam set \
        name = %s where id = %s"""
        cursor.execute(sql_update_query,
                       (name,
                        id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
 
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
 
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
 
 
id = 1
name = 'Jimmy'
updateData(id, name)