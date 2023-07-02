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

    #print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")
    
    else:
        print(err)

# Query 1: select all the fields for the studio
cursor = mydb.cursor()
cursor.execute("SELECT * from studio")

print("-- DISPLAYING Studio RECORDS --")
studio = cursor.fetchall()

for studio_id, studio_name in studio:
  print(f"Studio ID: {studio_id}\nStudio Name: {studio_name}\n".format(studio))

# Query 2: select all the fields for the genre
cursor2 = mydb.cursor()
cursor2.execute("SELECT * from genre")

print("-- DISPLAYING Genre RECORDS --")
genre = cursor2.fetchall()

for genre_id, genre_name in genre:
  print(f"Genre ID: {genre_id}\nGenre Name: {genre_name}\n".format(genre))

# Query 3: select the movie names for those movies that have a run time of less than two hours
cursor3 = mydb.cursor()
cursor3.execute("SELECT film_name, film_runtime from film where film_runtime < 120")

print("-- DISPLAYING Short film RECORDS --")
film = cursor3.fetchall()

for film_name, film_runtime in film:
    print(f"Film Name: {film_name}\nFilm Runtime: {film_runtime}\n".format(film))

# Query 4: get a list of film names, and directors ordered by director
cursor4 = mydb.cursor()
cursor4.execute("SELECT film_name, film_director from film order by film_director")

print("-- DISPLAYING Director RECORDS in Order--")
film = cursor4.fetchall()

for film_name, film_director in film:
    print(f"Film Name: {film_name}\nDirector: {film_director}\n".format(film))