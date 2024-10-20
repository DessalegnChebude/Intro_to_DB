import mysql.connector
import mysql.connector.Error

def databseCreation(mydb):
    try:
        # mydb = mysql.connector.connect()
        mycursor = mydb.cursor()
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        mycursor.execute(query)

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"failed to create database: {e}")

    finally:
        mycursor.close()



if __name__ == "__main__":
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@alx2024",
        database="mydb"
        )

        databseCreation(mydb)

    except mysql.connector.Error as e:
        print(f"Error Connecting to MYSQL: {e}")

    finally:
        if mydb.is_connected:
            mydb.close()
            print("MYSQL connection closed.")



