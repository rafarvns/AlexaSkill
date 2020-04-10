import mysql.connector
from mysql.connector import Error

def get_a_random_word():
    word = None
    try:
        connection = mysql.connector.connect(host='mysql',
                                            database='soletrando',
                                            user='root',
                                            password='123456')

        if connection.is_connected():
            db_Info = connection.get_server_info()       
            cursor = connection.cursor()
            cursor.execute("select palavra, palavra_comp from soletrando order by rand() limit 1;")
            word = cursor.fetchall()
            

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return word