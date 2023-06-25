import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warning": True
}

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        database = "movies",
        user = "movies_user",
        password = "popcorn"
    )

    print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    input("\n\n press a key to continue ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")
    
    else:
        print(err)

finally:
    mydb.close()