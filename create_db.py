# One time setup - execute all queries and exit connection
import pymysql

# Create a connection
databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server
databaseUserName = "root"  # User name of the database server
databaseUserPassword = ""  # Password for the database user
newDatabaseName = "sindi_db"  # Name of the database that is to be created
charSet = "utf8mb4"  # Character set
cusrorType = pymysql.cursors.DictCursor
connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
                                     charset=charSet, cursorclass=cusrorType)

try:
    # Create a cursor object
    cursorInstance = connectionInstance.cursor()
    # SQL Statement to create database
    sqlStatement = "CREATE DATABASE " + newDatabaseName
    # Execute the create database SQL statement through the cursor instance
    cursorInstance.execute(sqlStatement)
    # Select DB
    sqlStatement = "USE sindi_db;"
    cursorInstance.execute(sqlStatement)
    # SQL Statement to create table
    sqlStatement = "CREATE TABLE user_bot_chat(id varchar(300), User_input varchar(500), Bot_output varchar(500))"
    # Execute the sqlQuery
    cursorInstance.execute(sqlStatement)
    print("Successfuly created DB!")


except Exception as e:
    print("Exception occurred:{}".format(e))
    print("You need to have a localhost server running (WAMP or XAMPP)! Please do so and retry installation.")

finally:
    connectionInstance.close()
